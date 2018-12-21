from collections import defaultdict
import re

# it's a maze!

with open("data.txt") as f:
    s_reg = f.read().strip()[1:-1]


# (0, 0) (1, 0) (2, 0) (3, 0)
# (0, 1) (1, 1) (2, 1) (3, 1)
# (0, 2) (1, 2) (2, 2) (3, 2)

N, S, W, E = (0, -1), (0, 1), (-1, 0), (1, 0)


def find_node(node_grid, x, y, dir=(0, 0)):
    dx, dy = dir
    nx, ny = x + dx, y + dy

    return node_grid.get(nx, dict()).get(ny, None)


class Node:
    def __init__(self, x, y, c):
        self.x = x
        self.y = y
        self.c = c

    def link_nei(self, node_grid):
        fn = lambda dir: find_node(node_grid, self.x, self.y, dir)

        self.n = fn(N)
        self.s = fn(S)
        self.w = fn(W)
        self.e = fn(E)

        self.adj = [x for x in [self.n, self.s, self.w, self.e] if x]

    def __repr__(self):
        return f"N({self.x}, {self.y}, {self.c})"

    def set(self, nc):
        self.c = nc


def print_map(node_grid):
    minx = min(node_grid.keys())
    maxx = max(node_grid.keys())
    miny = min(min(row.keys()) for row in node_grid.values())
    maxy = max(max(row.keys()) for row in node_grid.values())

    for x in range(minx - 1, maxx + 2):
        for y in range(miny - 1, maxy + 2):
            n = find_node(node_grid, x, y)
            print(n.c if n else "#", end="")
        print()
    print()


def get_possible_paths():
    pattern = re.compile(r"\([NSWE|]+\)")
    p = s_reg

    while p.count("("):
        split = re.search(pattern, p)
        txt, (start, end) = split.group(), split.span()
        poss_end = txt[1:-1].split("|")

        start_beg = start - 1
        while start_beg > -1:
            if p[start_beg] in "|()":
                start_beg += 1
                break
            start_beg -= 1

        start_beg = max(0, start_beg)
        sub = p[start_beg:start]

        zam = "|".join([sub + p for p in poss_end])

        p = p[0:start_beg] + zam + p[end:]

    return set(p.split("|"))


def make_grid(root):
    nodes = [root]
    nodes_grid = defaultdict(dict)
    nodes_grid[0][0] = root

    paths_str = get_possible_paths()

    dirs = {"N": N, "W": W, "S": S, "E": E}

    for path in paths_str:
        x, y = 0, 0

        for d_name in path:
            dx, dy = dirs[d_name]
            x += dx
            y += dy
            n = find_node(nodes_grid, x, y)

            if not n:
                n = Node(x, y, "-" if d_name in "WE" else "|")
                nodes_grid[x][y] = n
                nodes.append(n)

            x += dx
            y += dy
            n = find_node(nodes_grid, x, y)

            if not n:
                n = Node(x, y, ".")
                nodes_grid[x][y] = n
                nodes.append(n)

    for n in nodes:
        n.link_nei(nodes_grid)

    return nodes_grid


def run_simulation():
    root = Node(0, 0, "+")
    nodes_grid = make_grid(root)

    path_lengths = {(0, 0): 0}
    to_visit = [root]

    while to_visit:
        node = to_visit.pop()
        dst = path_lengths[(node.x, node.y)]

        for n in node.adj:
            xy = (n.x, n.y)
            if xy in path_lengths:
                continue

            path_lengths[xy] = dst + 1
            to_visit.append(n)

    path_lengths = [
        v // 2
        for n_xy, v in path_lengths.items()
        if find_node(nodes_grid, *n_xy).c == "."
    ]

    longest_path = max(path_lengths)
    paths_over_1000 = sum(dst >= 1000 for dst in path_lengths)

    return longest_path, paths_over_1000


part1, part2 = run_simulation()
print("1)", part1, "\n2)", part2)

