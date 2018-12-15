from collections import defaultdict
from copy import deepcopy

# (0, 0), (0, 1), (0, 2)
# (1, 0), (1, 1), (1, 2)
# (2, 0), (2, 1), (2, 2)
# (3, 0), (3, 1), (3, 2)

UP, DOWN, LEFT, RIGHT = (-1, 0), (1, 0), (0, -1), (0, 1)
CHR_TO_VEC = {">": RIGHT, "<": LEFT, "v": DOWN, "^": UP}
VEC_TO_CHR = {v: k for k, v in CHR_TO_VEC.items()}


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


class Node:
    def __init__(self, x, y, c, id):
        self.x = x
        self.y = y
        self.xy = (x, y)
        self.c = c
        self.t = "cart" if c in "<>^v" else c
        self.d = {">": "-", "<": "-", "^": "|", "v": "|"}.get(c, c)
        self.id = id

        self.cart = None
        if self.t == "cart":
            self.cart = (CHR_TO_VEC[c], -1)

    def __repr__(self):
        return f"N({self.x}, {self.y}, {self.c})"


def read_nodes():
    with open("data.txt") as f:
        org_nodes = []
        count, hei = 0, 0  # count is also unique id
        for x, r in enumerate(f.readlines()):
            r = [x for x in r if x != "\n"]
            hei += 1
            for y, c in enumerate(r):
                count += 1
                if c in r"^v></\-|+":
                    org_nodes.append(Node(x, y, c, count))
        wid = count // hei

    return org_nodes, hei, wid


def get_order(nodes, hei, wid):
    carts = [n for n in nodes if n.cart]
    carts.sort(key=lambda n: n.x * 1000 + n.y)
    return [n.id for n in carts]


def tick(nodes, hei, wid, remove_colliding=False):
    order = get_order(nodes, hei, wid)
    collision = None

    for node_id in order:
        n = by_id(nodes, node_id)

        if n.cart is None:
            continue

        next_node = by_coords(nodes, combcoordsvec(n.xy, n.cart[0]))

        # print(n, next_node)

        if next_node.cart:
            collision = next_node.xy

            if remove_colliding:
                n.cart = None
                n.c = n.d
                n.t = n.c
                next_node.cart = None
                next_node.c = next_node.d
                next_node.t = next_node.c

                continue
            else:
                return collision

        if next_node.c == "+":
            next_i = (n.cart[1] + 1) % 3
            new_dir = None

            if next_i == 1:
                new_dir = n.cart[0]
            else:
                m = {
                    LEFT: {UP: LEFT, DOWN: RIGHT, LEFT: DOWN, RIGHT: UP},
                    RIGHT: {UP: RIGHT, DOWN: LEFT, RIGHT: DOWN, LEFT: UP},
                }
                abs_change = LEFT if next_i == 0 else RIGHT
                new_dir = m[abs_change][n.cart[0]]

            t = (new_dir, next_i)
            n.cart = t

        if next_node.c == r"\\"[0]:
            m = {UP: LEFT, RIGHT: DOWN, DOWN: RIGHT, LEFT: UP}
            n.cart = (m[n.cart[0]], n.cart[1])

        if next_node.c == r"/":
            m = {UP: RIGHT, RIGHT: UP, DOWN: LEFT, LEFT: DOWN}
            n.cart = (m[n.cart[0]], n.cart[1])

        n.c = n.d
        n.t = n.c
        next_node.cart = n.cart
        n.cart = None

        next_node.c = VEC_TO_CHR[next_node.cart[0]]
        next_node.t = "cart"

    return collision


def print_board(i, nodes, hei, wid):
    print()
    print(i)
    for x in range(hei):
        for y in range(20):
            n = by_coords(nodes, (x, y))
            if n:
                c = n.c if not n.cart else VEC_TO_CHR[n.cart[0]]
                print(c, end="")
            else:
                print(" ", end="")
        print()

    print()


def part1():
    nodes, hei, wid = read_nodes()

    collision = False
    while not collision:
        collision = tick(nodes, hei, wid)

    return collision[::-1]


def part2():
    nodes, hei, wid = read_nodes()
    i = 0
    coll = None

    # order_org = get_order(nodes, hei, wid)
    # print(order_org)
    # return
    while True:
        i += 1
        if i > 80:
            pass

        carts = {n for n in nodes if n.cart}
        count_carts = len(carts)
        # print(i, count_carts, coll, carts)
        if count_carts == 1:
            return [n for n in nodes if n.cart][0].xy[::-1]

        # print_board(i, nodes, hei, wid)
        coll = tick(nodes, hei, wid, remove_colliding=True)


print("1)", part1(), "\n2)", part2())
