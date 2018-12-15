from collections import defaultdict, Counter
from copy import deepcopy


# (0, 0), (0, 1), (0, 2)
# (1, 0), (1, 1), (1, 2)
# (2, 0), (2, 1), (2, 2)
# (3, 0), (3, 1), (3, 2)


def combcoordsvec(v1, v2):
    return (v1[0] + v2[0], v1[1] + v2[1])


def by_coords(nodes, vec):
    for n in nodes:
        if n.x == vec[0] and n.y == vec[1]:
            return n


def by_id(nodes, id):
    for n in nodes:
        if n.id == id:
            return n


ADJ_VEC = ((-1, 0), (0, -1), (0, 1), (1, 0))
ENEMY = {"G": "E", "E": "G"}


class Node:
    def __init__(self, x, y, c, id):
        self.x = x
        self.y = y
        self.c = c
        self.t = "live" if c in "GE" else c
        self.id = id
        if self.t:
            self.hp = 200
            self.attack_points = 3

    def __repr__(self):
        return f"N({self.x}, {self.y}, {self.c})"

    def link_neighbours(self, nodes):

        if self.t == "#":
            self.adj = []
            return
        neiall = [by_coords(nodes, combcoordsvec((self.x, self.y), v)) for v in ADJ_VEC]
        nei = [x for x in neiall if x and x.t != "#"]
        self.adj = nei

    def deal_damage(self, x):
        self.hp -= x
        if self.hp <= 0:
            self.t = "."
            self.c = "."
            return "dead"

    def set_attack_points(self, l):
        self.attack_points = l(self.c)


def read_nodes():
    with open("data3.txt") as f:
        org_nodes = []
        count, hei = 0, 0  # count is also unique id
        for x, r in enumerate(f.readlines()):
            r = r.strip()
            hei += 1
            for y, c in enumerate(r):
                count += 1
                org_nodes.append(Node(x, y, c, count))
        wid = count // hei

        for n in org_nodes:
            n.link_neighbours(org_nodes)

    return org_nodes, hei, wid


def get_order(nodes, hei, wid):
    order = []
    for x in range(hei):
        for y in range(wid):
            n = by_coords(nodes, (x, y))
            if n.t == "live":
                order.append(n.id)

    return order


def turn(nodes, hei, wid):
    order = get_order(nodes, hei, wid)
    dead_ids = set()
    # print(order)
    for node_id in order:
        if node_id in dead_ids:
            continue
        n = by_id(nodes, node_id)
        all_enemies = {x for x in nodes if x.t == "live" and x.c == ENEMY[n.c]}

        if not all_enemies:
            return False

        adj_enemies = all_enemies & set(n.adj)
        if not n.adj:
            continue

        if not adj_enemies:  # move
            in_range = {x for enemy in all_enemies for x in enemy.adj if x.t == "."}
            in_range_ids = {x.id for x in in_range}

            visited = set()
            to_visit = {x for x in n.adj if x.t == "."}

            while to_visit:
                t = to_visit.pop()
                visited.add(t)
                possible_in_range = {x for x in t.adj if x.t == "."}
                to_visit |= possible_in_range
                to_visit -= visited

            reachable_ids = {x.id for x in (visited & in_range)}
            reachable = visited & in_range
            if not reachable_ids:
                continue

            lst = []

            for first_alpha in reachable:
                visited = set()
                to_visit = [(first_alpha, 0)]

                while to_visit:
                    new_to_visit = []
                    to_visit_set = set()
                    for t, dst in to_visit:
                        visited.add(t)
                        lst.append((t, dst))

                    for t, dst in to_visit:
                        for a in t.adj:
                            if (
                                a.t == "."
                                and (a not in visited)
                                and (a not in to_visit_set)
                            ):
                                new_to_visit.append((a, dst + 1))
                                to_visit_set.add(a)

                    to_visit = new_to_visit
                    # print(to_visit, lst)

            # return

            lst = [x for x in lst if x[0] in n.adj]

            min_dst = min(lst, key=lambda x: x[1])[1]
            steps = [x for x, dst in lst if dst == min_dst]

            step_to_take = min(steps, key=lambda h: h.x * 1000 + h.y)
            # print(n, lst, step_to_take)

            ###
            xn, yn = n.x, n.y
            xs, ys = step_to_take.x, step_to_take.y
            n.x, n.y = xs, ys
            step_to_take.x, step_to_take.y = xn, yn

            for n in nodes:
                n.link_neighbours(nodes)

        n = by_id(nodes, node_id)
        adj_enemies = {x for x in n.adj if x.t == "live" and x.c == ENEMY[n.c]}
        if adj_enemies:  # attack
            adj_enemies = sorted(list(adj_enemies), key=lambda x: x.hp)
            m = adj_enemies[0].hp
            poss = [e for e in adj_enemies if e.hp == m]

            first_alpha = min([r for r in poss], key=lambda h: h.x * 1000 + h.y)

            dead = first_alpha.deal_damage(n.attack_points)

            if dead == "dead":
                dead_ids.add(first_alpha.id)
                for n in nodes:
                    n.link_neighbours(nodes)


def print_board(i, nodes, hei, wid):
    print()
    print(i)
    for x in range(hei):
        for y in range(wid):
            n = by_coords(nodes, (x, y))
            print(n.c, end="")
        print()

    print()


def part1():
    nodes, hei, wid = read_nodes()
    i = 0
    out = True
    while out != False:
        if i > 10:
            pass

        # print_board(i, nodes, hei, wid)

        for n in nodes:
            n.link_neighbours(nodes)

        out = turn(nodes, hei, wid)
        i += 1

    rounds = i - 1

    s = sum(n.hp for n in nodes if n.t == "live")
    # print(rounds)
    # print(s)

    return s * rounds


def part2():
    nodes, hei, wid = read_nodes()

    count_elves = sum(n.c == "E" for n in nodes)
    # print(count_elves)

    i = 4
    while True:
        # print(i)
        l = lambda x: 3 if x == "G" else i
        nodes, hei, wid = read_nodes()

        for n in nodes:
            n.set_attack_points(l)

        c = 0
        out = True
        while out != False:
            for n in nodes:
                n.link_neighbours(nodes)
            out = turn(nodes, hei, wid)
            c += 1

        count_elves_left = sum(n.c == "E" for n in nodes)

        if count_elves == count_elves_left:
            rounds = c - 1
            print(rounds)

            s = sum(n.hp for n in nodes if n.t == "live" and n.c == "E")
            print(sorted([n.hp for n in nodes if n.t == "live" and n.c == "E"]))
            print(s)
            print(i)
            return rounds * s

        i += 1


print("1)", part1(), "\n2)", part2())

