with open("data.txt") as f:
    polymer = f.read().strip()


def single_reaction_pass(x):
    changes = 0

    poly = []
    i = 0
    while i < len(x) - 1:
        ch, nextch = x[i], x[i + 1]

        if abs(ord(ch) - ord(nextch)) == 32:
            changes += 1
            i += 2
            continue

        poly.append(ch)
        i += 1

    poly += [x[-1]]

    return poly, changes


def react_polymer(polymer):
    changes = 1
    while changes != 0:
        polymer, changes = single_reaction_pass(polymer)

    return len(polymer)


def part1():
    return react_polymer(polymer)


def part2():
    return min(
        react_polymer(polymer.replace(chr(a), "").replace(chr(a - 32), ""))
        for a in range(ord("a"), ord("z") + 1)
    )


print("1)", part1(), "\n2)", part2())
