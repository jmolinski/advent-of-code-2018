from collections import defaultdict as ddict


class Marble:
    def __init__(self, v, prev, next):
        self.v = v
        self.prev = prev
        self.next = next

    def add_next(self, v):
        m = Marble(v, self, self.next)
        self.next.prev = m
        self.next = m
        return m

    def remove(self):
        self.prev.next = self.next
        self.next.prev = self.prev
        return self


def calc_max_score(players, last):
    pp = ddict(int)

    m0, m1 = Marble(0, None, None), Marble(1, None, None)
    m0.next, m0.prev = m1, m1
    m1.next, m1.prev = m0, m0

    curr = m1
    for i in range(2, last + 1):
        pid = i % players
        if i % 23 == 0:
            pp[pid] += i
            rem = curr.prev.prev.prev.prev.prev.prev.prev.remove()
            pp[pid] += rem.v
            curr = rem.next
        else:
            curr = curr.next.add_next(i)

    return max(pp.items(), key=lambda x: x[1])[1]


players, last = 423, 71944

print("1)", calc_max_score(players, last))
print("2)", calc_max_score(players, last * 100))

