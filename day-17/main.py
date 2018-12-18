from collections import defaultdict

with open("data.txt") as f:
    data = []
    for l in f.readlines():
        l = sorted(l.strip().split(", "))
        l[0] = l[0][2:]
        l[1] = l[1][2:]

        l = [list(map(int, i.split(".."))) for i in l]

        data.append(l)

    miny = min(min(y[1]) for y in data)
    maxy = max(max(y[1]) for y in data)
    minx = min(min(x[0]) for x in data) - 5
    maxx = max(max(x[0]) for x in data) + 5


def make_board():
    board = defaultdict(lambda: defaultdict(lambda: "."))

    board[500][0] = "+"

    for xr, yr in data:
        for x in range(min(xr), max(xr) + 1):
            for y in range(min(yr), max(yr) + 1):
                board[x][y] = "#"

    return board


# (0, 0) (1, 0) (2, 0) (3, 0)
# (0, 1) (1, 1) (2, 1) (3, 1)
# (0, 2) (1, 2) (2, 2) (3, 2)

UP, DOWN, RIGHT, LEFT = (0, -1), (0, 1), (1, 0), (-1, 0)


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

        self.up = fn(UP)
        self.down = fn(DOWN)
        self.left = fn(LEFT)
        self.right = fn(RIGHT)

        self.adj = [x for x in [self.up, self.down, self.left, self.right] if x]

    def __repr__(self):
        return f"N({self.x}, {self.y}, {self.c})"

    def set(self, nc):
        self.c = nc


def parse_grid(board):
    nodes = []
    nodes_grid = defaultdict(dict)
    for x in range(minx, maxx + 1):
        for y in range(maxy + 1):
            n = Node(x, y, board[x][y])
            nodes.append(n)
            nodes_grid[x][y] = n

    for n in nodes:
        n.link_nei(nodes_grid)

    return nodes, nodes_grid


def find_walls(n):
    lbond, rbond = n, n

    if not lbond.left or not rbond.right:
        return None, None

    while True:
        if not lbond.down or lbond.down.c in "|.":
            return None, None

        if lbond.left.c == "|":
            lbond = lbond.left

        if not lbond.left or lbond.left.c == ".":
            return None, None

        if lbond.left.c == "#":
            break  # found lbond

    while True:
        if not rbond.down or rbond.down.c in "|.":
            return None, None

        if rbond.right.c == "|":
            rbond = rbond.right

        if not rbond.right or rbond.right.c == ".":
            return None, None

        if rbond.right.c == "#":
            break  # found rbond

    return lbond, rbond


def run_simulation():
    board = make_board()
    nodes, _ = parse_grid(board)

    spring = [n for n in nodes if n.c == "+"][0]
    spring.down.set("|")
    running = [spring.down]
    resting = []

    while True:
        for n in running:
            if not n.down or not (n.c == "|"):
                continue

            if n.down.c == ".":
                n.down.set("|")
                continue

            if n.down.c == "|":
                continue

            if n.down.c in "~#":
                if not n.left or not n.right:
                    continue
                if n.left.c == ".":
                    n.left.set("|")
                if n.right.c == ".":
                    n.right.set("|")

            if n.down.c in "~#":
                lbond, rbond = find_walls(n)
                if lbond and rbond:
                    while lbond.x <= rbond.x:
                        lbond.set("~")
                        lbond = lbond.right

        new_running = [n for n in nodes if n.c == "|"]
        new_resting = [n for n in nodes if n.c == "~"]

        if len(new_resting) == len(resting) and len(new_running) == len(running):
            break

        resting, running = new_resting, new_running

    running_in_range_y = [n for n in running if miny <= n.y <= maxy]
    return len(resting) + len(running_in_range_y), len(resting)


total_reachable, resting = run_simulation()
print("1)", total_reachable, "\n2)", resting)
