from collections import Counter

with open("data.txt") as f:
    ids = list(x.strip() for x in f.readlines())


def part1():
    num_2, num_3 = 0, 0

    for box_id in ids:
        counts = Counter(box_id).values()
        num_2 += 2 in counts
        num_3 += 3 in counts

    return num_2 * num_3


def part2():
    for b1id in ids:
        for b2id in ids:
            comm_id = "".join([x for x, y in zip(b1id, b2id) if x == y])
            if len(comm_id) + 1 == len(b1id):
                return comm_id


print("1)", part1())
print("2)", part2())
