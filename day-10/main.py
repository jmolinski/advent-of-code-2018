def make_position_func(l):
    l = list(map(int, l.split()))
    return lambda s: (l[0] + s * l[2], l[1] + s * l[3])


with open("data.txt") as f:
    sanit = (
        lambda x: x.replace("position=<", "")
        .replace(",", "")
        .replace(">", "")
        .replace("velocity=<", "")
    )
    dat = [make_position_func(sanit(l)) for l in f.readlines()]

    board_nth_sec = lambda n: {x(n) for x in dat}


def max_dst(l):
    m = []
    for x1, y1 in l:
        for x2, y2 in l:
            m.append((x1 - x2) ** 2 + (y1 - y2) ** 2)
    return max(m)


def get_possible_sec_range(start, stop, step):
    min_sec_r, max_sec_r = sorted(
        [(n, max_dst(board_nth_sec(n))) for n in range(start, stop, step)],
        key=lambda x: x[1],
    )[:2]
    return sorted([min_sec_r[0], max_sec_r[0]])


def solution():
    min_s, max_s, step = 0, 100 * 1000, 10000

    while step > 0:
        min_s, max_s = get_possible_sec_range(min_s, max_s + 1, step)
        step //= 10

    sec = min(
        [(n, max_dst(board_nth_sec(n))) for n in range(min_s, max_s + 1, 1)],
        key=lambda x: x[1],
    )[0]

    board = board_nth_sec(sec)
    min_x, *_, max_x = sorted(a[1] for a in board)
    min_y, *_, max_y = sorted(a[0] for a in board)

    print("part1:")
    for x in range(min_x, max_x + 1):
        for y in range(min_y, max_y + 1):
            ch = "#" if (y, x) in board else " "
            print(ch, sep="", end="")
        print()

    print("\npart2:", max_s)


solution()

