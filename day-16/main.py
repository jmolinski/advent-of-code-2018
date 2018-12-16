from collections import defaultdict
import re


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

            operations = {
                "addr": lambda: reg[a] + reg[b],
                "addi": lambda: reg[a] + b,
                "mulr": lambda: reg[a] * reg[b],
                "muli": lambda: reg[a] * b,
                "banr": lambda: reg[a] & reg[b],
                "bani": lambda: reg[a] & b,
                "borr": lambda: reg[a] | reg[b],
                "bori": lambda: reg[a] | b,
                "setr": lambda: reg[a],
                "seti": lambda: a,
                "gtir": lambda: int(a > reg[b]),
                "gtri": lambda: int(reg[a] > b),
                "gtrr": lambda: int(reg[a] > reg[b]),
                "eqir": lambda: int(a == reg[b]),
                "eqri": lambda: int(reg[a] == b),
                "eqrr": lambda: int(reg[a] == reg[b]),
            }

            poss = [k for k, v in operations.items() if result[c] == v()]
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
        operators = {
            "ad": lambda x, y: x + y,
            "mu": lambda x, y: x * y,
            "ba": lambda x, y: x & y,
            "bo": lambda x, y: x | y,
            "se": lambda x, y: x,
            "gt": lambda x, y: int(x > y),
            "eq": lambda x, y: int(x == y),
        }

        reg = [0, 0, 0, 0]
        for l2 in f.readlines():
            op, a, b, c = map(int, l2.split())
            opnam = op_map[op]

            if opnam[:2] in ("eq", "gt"):
                operand1 = a if opnam[-2] == "i" else reg[a]
                operand2 = b if opnam[-1] == "i" else reg[b]
            elif opnam == "seti":
                operand1 = a
                operand2 = None
            else:
                operand1 = reg[a]
                operand2 = b if opnam[-1] == "i" else reg[b]

            reg[c] = operators[opnam[:2]](operand1, operand2)

    return reg[0]


over_2, op_mapping = part1()
reg_0 = part2(op_mapping)

print("1)", over_2, "\n2)", reg_0)
