from collections import defaultdict
import re


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


def part1():
    with open("data_registers.txt") as f:
        data = list([x.strip() for x in f.readlines()])

        over_2_possible = 0
        all_poss = defaultdict(set)
        for i in range(len(data) // 4 + 1):
            l1, l2, l3, *_ = data[i * 4 :]
            reg = list(map(int, re.findall(r"\d", l1)))
            result = list(map(int, re.findall(r"\d", l3)))
            op, a, b, c = map(int, l2.split())

            poss = [k for k, fn in OPERATIONS.items() if result == fn(reg, a, b, c)]
            over_2_possible += int(len(poss) > 2)

            for p in poss:
                all_poss[p].add(op)

        op_map = {}
        while all_poss:
            k, v = [(k, v) for k, v in all_poss.items() if len(v) == 1][0]
            op_map[list(v)[0]] = k
            del all_poss[k]
            all_poss = {k: (rest - set(v)) for k, rest in all_poss.items()}

    return over_2_possible, op_map


def part2(op_map):
    with open("data_program.txt") as f:

        reg = [0, 0, 0, 0]
        for l2 in f.readlines():
            op, a, b, c = map(int, l2.split())
            opnam = op_map[op]
            reg = OPERATIONS[opnam](reg, a, b, c)

    return reg[0]


over_2, op_mapping = part1()
reg_0 = part2(op_mapping)

print("1)", over_2, "\n2)", reg_0)
