from collections import defaultdict
from copy import deepcopy

with open("data.txt") as f:
    data = defaultdict(lambda: defaultdict(lambda: None))

    for x, r in enumerate(f.readlines()):
        r = r.strip()
        for y, c in enumerate(r):
            data[x][y] = c

    size = len(data)


def adjecent(x, y, data):
    adj = []
    for dx in (-1, 0, 1):
        for dy in (-1, 0, 1):
            if dx == 0 and dy == 0:
                continue
            adj.append(data[x + dx][y + dy])

    return [z for z in adj if z]


def hash_board(d):
    return hash("".join(["".join(r.values()) for r in d.values()]))


def run_sim(minutes, find_cycle=False):
    board = deepcopy(data)

    m = defaultdict(list)
    for minute in range(minutes):
        if find_cycle:
            m[hash_board(board)].append(minute)

        new_board = deepcopy(board)
        for x in range(size):
            for y in range(size):
                adj = adjecent(x, y, board)
                field = board[x][y]

                if field == "." and adj.count("|") >= 3:
                    new_board[x][y] = "|"

                elif field == "|" and adj.count("#") >= 3:
                    new_board[x][y] = "#"

                elif field == "#" and ("#" not in adj or "|" not in adj):
                    new_board[x][y] = "."

        board = new_board

        if find_cycle:
            if any(len(v) > 1 for v in m.values()):
                return [v for v in m.values() if len(v) > 1][0]

    wood = sum(a == "|" for r in board.values() for a in r.values())
    lumb = sum(a == "#" for r in board.values() for a in r.values())

    return wood * lumb


def part2():
    cycle_data = run_sim(minutes=1000, find_cycle=True)
    cycle_start = min(cycle_data)
    cycle_len = max(cycle_data) - min(cycle_data)

    minute = 1000 * 1000 * 1000
    minute = cycle_start + ((minute - cycle_start) % cycle_len)

    return run_sim(minutes=minute)


print("1)", run_sim(minutes=10), "\n2)", part2())
