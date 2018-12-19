from collections import defaultdict
import re


def read_data():
    with open("data.txt") as f:
        ip = int(f.readline().split()[1])

        data = []
        for l in f.readlines():
            op, a, b, c = l.strip().split()
            data.append([op, int(a), int(b), int(c)])

    return ip, data


def exec_op(fn):
    def op(reg, a, b, c):
        nreg = [x for x in reg]  # because lists are mutable
        nreg[c] = fn(reg, a, b)
        return nreg

    return op


OPERATIONS = {
    "addr": exec_op(lambda reg, x, y: reg[x] + reg[y]),
    "addi": exec_op(lambda reg, x, y: reg[x] + y),
    "mulr": exec_op(lambda reg, x, y: reg[x] * reg[y]),
    "muli": exec_op(lambda reg, x, y: reg[x] * y),
    "banr": exec_op(lambda reg, x, y: reg[x] & reg[y]),
    "bani": exec_op(lambda reg, x, y: reg[x] & y),
    "borr": exec_op(lambda reg, x, y: reg[x] | reg[y]),
    "bori": exec_op(lambda reg, x, y: reg[x] | y),
    "setr": exec_op(lambda reg, x, y: reg[x]),
    "seti": exec_op(lambda reg, x, y: x),
    "gtir": exec_op(lambda reg, x, y: int(x > reg[y])),
    "gtri": exec_op(lambda reg, x, y: int(reg[x] > y)),
    "gtrr": exec_op(lambda reg, x, y: int(reg[x] > reg[y])),
    "eqir": exec_op(lambda reg, x, y: int(x == reg[y])),
    "eqri": exec_op(lambda reg, x, y: int(reg[x] == y)),
    "eqrr": exec_op(lambda reg, x, y: int(reg[x] == reg[y])),
}


def run_simulation(reg):
    ip_reg, data = read_data()

    ip = 0
    while ip < len(data):
        op, a, b, c = data[ip]
        reg[ip_reg] = ip
        reg = OPERATIONS[op](reg, a, b, c)
        ip = reg[ip_reg]

        ip += 1

    return reg[0]


part1 = run_simulation(reg=[0, 0, 0, 0, 0, 0])
# part2 = run_simulation(reg=[1, 0, 0, 0, 0, 0])
print(
    "1)", part1, "\n2)", "proper simulation would take forever, check part2_solution.py"
)
