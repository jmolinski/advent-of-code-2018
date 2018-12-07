from collections import defaultdict
from copy import deepcopy

with open("data.txt") as f:
    pairs = [(lambda x: (x[1], x[7]))(s.split()) for s in f.readlines()]

    req = defaultdict(set)
    all_letters = set()
    for a, b in pairs:
        req[b].add(a)
        all_letters.update([a, b])

    def letter_req(l):
        childs = req.get(l, set())
        return childs | set(r for n in childs for r in letter_req(n))

    full_req = {l: letter_req(l) for l in all_letters}


def part1():
    s = ""
    while len(s) < len(all_letters):
        s += min(l for l in all_letters - set(s) if not full_req[l] - set(s))

    return s


def part2():
    used_letters, completed = set(), set()
    in_progress = dict()
    second = -1

    while len(all_letters - completed):
        in_progress = {l: v - 1 for l, v in in_progress.items() if v}

        completed = used_letters - set(in_progress.keys())
        candidates = {
            l for l in all_letters - used_letters if not full_req[l] - completed
        }

        for c in sorted(candidates):
            if len(in_progress) >= 5:
                break

            in_progress[c] = (ord(c) - ord("A") + 1) + 59
            used_letters.add(c)

        second += 1

    return second


print("1)", part1(), "\n2)", part2())
