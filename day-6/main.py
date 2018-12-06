from collections import Counter


with open("data.txt") as f:
    points = list(enumerate([list(map(int, r.split(", "))) for r in f.readlines()]))

    minc, maxc = 0, 360
    m = list(list(list() for x in range(minc, maxc)) for y in range(minc, maxc))

    for x in range(minc, maxc):
        for y in range(minc, maxc):
            for i, (a, b) in points:
                d = abs(a - x) + abs(b - y)
                m[x][y].append((i, d))


def wtf(minc, maxc, m, v):
    return set(
        Counter(
            m[(x, y)][0]
            for x in range(minc + v, maxc - v)
            for y in range(minc + v, maxc - v)
        ).items()
    )


def part1():
    lst = []
    dst = {}

    for x in range(minc, maxc):
        for y in range(minc, maxc):
            mxy = m[x][y]
            mind = min(mxy, key=lambda x: x[1])[1]
            mxy = [(i, d) for i, d in mxy if d == mind]
            mxy = "." if len(mxy) > 1 else mxy[0]
            dst[(x, y)] = mxy
            lst.append(mxy[0])

    area_by_id = Counter(lst)

    p1 = wtf(minc, maxc, dst, 1)
    p2 = wtf(minc, maxc, dst, 2)

    finite_ids = [a for a, b in (p1 & p2)]
    return max(area_by_id[i] for i in finite_ids)


def part2():
    licz = 0
    for x in range(minc, maxc):
        for y in range(minc, maxc):
            licz += sum(d for i, d in m[x][y]) < 10000

    return licz


print("1)", part1(), "\n2)", part2())

