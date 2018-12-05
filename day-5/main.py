with open("data.txt") as f:
    polymer = f.read().strip()


def react_polymer(pol):
    pol = [(ord(c) - ord("A")) + 1 for c in pol]
    pol = [c if c < 33 else -(c - 32) for c in pol]

    i = 0
    while i < len(pol) - 1:
        if pol[i] == -pol[i + 1]:
            del pol[i]
            del pol[i]
            i -= 1
        else:
            i += 1

    return pol


def part1():
    return len(react_polymer(polymer))


def part2():
    return min(
        len(react_polymer(pol))
        for pol in [
            polymer.replace(chr(a), "").replace(chr(a - 32), "")
            for a in range(ord("a"), ord("z") + 1)
        ]
    )


print("1)", part1(), "\n2)", part2())
