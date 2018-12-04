from collections import Counter, namedtuple

Order = namedtuple("Order", "id shiftleft shifttop width height")
with open("data.txt") as f:
    orders = [
        Order(*list(map(int, x.split())))
        for x in (
            f.read()
            .replace("#", "")
            .replace("@ ", "")
            .replace(",", " ")
            .replace(":", "")
            .replace("x", " ")
            .split("\n")
        )
    ]

    fabric = list(list(set() for _ in range(1002)) for x in range(1002))

    for o in orders:
        for i in range(o.shifttop, o.shifttop + o.height):
            for j in range(o.shiftleft, o.shiftleft + o.width):
                fabric[i][j].add(o.id)


def part1():
    return sum(len(x) >= 2 for row in fabric for x in row)


def part2():
    ids_taken = set()

    for row in fabric:
        for x in row:
            if len(x) >= 2:
                ids_taken.update(x)

    return list({o.id for o in orders} - ids_taken)[0]


print("1)", part1(), "\n2)", part2())
