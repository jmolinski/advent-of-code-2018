from collections import defaultdict, Counter
from copy import deepcopy


def calc_power(x, y, serial):
    rackid = x + 10
    power = ((rackid * y) + serial) * rackid
    power = int(("00" + str(power))[-3])
    power -= 5

    return power


assert calc_power(122, 79, 57) == -5
assert calc_power(217, 196, 39) == 0
assert calc_power(101, 153, 71) == 4

serial = 6303
box_side = 300
board = dict()
for i in range(1, box_side):
    for j in range(1, box_side):
        board[(i, j)] = calc_power(i, j, serial)


def subgrid_power(x, y, si):
    p = 0

    for j in range(x, x + si):
        for i in range(y, y + si):
            p += board[(j, i)]
    return p


def get_max_tot_power_sq(si_range):
    max_power = ((0, 0, 0), 0)
    for si in si_range:
        # print(si)
        for i in range(1, box_side + 1 - si):
            for j in range(1, box_side + 1 - si):
                pow = subgrid_power(i, j, si)
                if pow > max_power[1]:
                    max_power = ((i, j, si), pow)

    return max_power


def part1():
    max_pow = get_max_tot_power_sq(si_range=(3,))
    x, y = max_pow[0][0], max_pow[0][1]
    return f"{x},{y}"


def part2():
    max_pow = get_max_tot_power_sq(si_range=range(16))
    x, y, size = max_pow[0][0], max_pow[0][1], max_pow[0][2]
    return f"{x},{y},{size}"


print("1)", part1(), "\n2)", part2())
