import itertools

with open("data.txt") as f:
    data = [int(x) for x in f.readlines()]

print("1)", sum(data))


freq = {0}
f = 0
for ch in itertools.cycle(data):
    f += ch
    if f in freq:
        print("2)", f)
        break
    freq.add(f)
