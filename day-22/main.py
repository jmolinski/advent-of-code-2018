from collections import defaultdict

with open("data.txt") as f:
    DEPTH = int(f.readline().split()[1])
    TARGET = list(map(int, f.readline().strip().split()[1].split(",")))

# (0, 0) (1, 0) (2, 0) (3, 0)
# (0, 1) (1, 1) (2, 1) (3, 1)
# (0, 2) (1, 2) (2, 2) (3, 2)

N, S, W, E = (0, -1), (0, 1), (-1, 0), (1, 0)


def find_node(node_grid, x, y, dir=(0, 0)):
    dx, dy = dir
    nx, ny = x + dx, y + dy

    return node_grid.get(nx, dict()).get(ny, None)


class Node:
    def __init__(self, x, y, c="@"):
        self.x = x
        self.y = y
        self.c = c
        self.geo_ind_cache = -1

    def link_nei(self, node_grid):
        fn = lambda dir: find_node(node_grid, self.x, self.y, dir)

        self.n = fn(N)
        self.s = fn(S)
        self.w = fn(W)
        self.e = fn(E)

        self.adj = [x for x in [self.n, self.s, self.w, self.e] if x]

    def __repr__(self):
        return f"N({self.x}, {self.y}, {self.c})"

    def geo_index(self):
        if self.geo_ind_cache != -1:
            return self.geo_ind_cache

        geo_ind = -1
        if self.x == self.y == 0:
            geo_ind = 0
        elif self.x == TARGET[0] and self.y == TARGET[1]:
            geo_ind = 0
        elif self.y == 0:
            geo_ind = self.x * 16807
        elif self.x == 0:
            geo_ind = self.y * 48271
        else:
            geo_ind = self.w.erosion_level() * self.n.erosion_level()

        self.geo_ind_cache = geo_ind
        return geo_ind

    def erosion_level(self):
        return (self.geo_index() + DEPTH) % 20183

    def determine_type(self):
        t = self.erosion_level() % 3
        if t == 0:
            self.c = "."
        if t == 1:
            self.c = "="
        if t == 2:
            self.c = "|"

        self.acc_tools = {".": "ct", "=": "cn", "|": "tn"}[self.c]


def make_grid():
    nodes = []
    nodes_grid = defaultdict(dict)

    for y in range(TARGET[1] + 50):
        for x in range(TARGET[0] * 6):
            n = Node(x, y)
            nodes_grid[x][y] = n
            nodes.append(n)

    for n in nodes:
        n.link_nei(nodes_grid)

    for n in nodes:
        n.determine_type()

    return nodes_grid


def calc_risk(nodes_grid):
    risk = 0
    risk_map = {".": 0, "=": 1, "|": 2}
    for x in range(TARGET[0] + 1):
        for y in range(TARGET[1] + 1):
            risk += risk_map.get(nodes_grid[x][y].c, 0)
    return risk


def quickest_path_time(nodes_grid):
    past_workers = []
    workers = [(0, 0, "t", 0)]  # x y tool time
    paths = dict()
    found_target = False
    time_to_target = -1

    while workers:
        new_workers = []

        for x, y, tool, time in workers:
            if not (paths.get((x, y, tool), 10e9) > time):
                past_workers.append((x, y, tool, time))
                continue

            paths[(x, y, tool)] = time

            if found_target and time > time_to_target:
                past_workers.append((x, y, tool, time))
                continue

            if x == TARGET[0] and y == TARGET[1]:
                past_workers.append((x, y, tool, time))
                if found_target:
                    time_to_target = min(time_to_target, time)
                else:
                    found_target = True
                    time_to_target = time
                continue

            # spawn new workers
            this_node = nodes_grid[x][y]
            for n in this_node.adj:
                if tool in n.acc_tools:
                    new_workers.append((n.x, n.y, tool, time + 1))
                else:
                    for acc_tool in n.acc_tools:
                        new_workers.append((n.x, n.y, acc_tool, time + 8))

        workers = new_workers

    times = [t for x, y, _, t in past_workers if x == TARGET[0] and y == TARGET[1]]

    return times[-2]


def run_simulation():
    nodes_grid = make_grid()
    nodes_grid[TARGET[0]][TARGET[1]].acc_tools = "t"

    return calc_risk(nodes_grid), quickest_path_time(nodes_grid)


part1, part2 = run_simulation()
print("1)", part1, "\n2)", part2)

