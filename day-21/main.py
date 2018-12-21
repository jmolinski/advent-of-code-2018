# decompiled-by-hand & optimized
# definitely not gonna refactor this one
# 0.18s on pypy3

ip_reg = 4
reg = [0, 0, 0, 0, 0, 0]
i = 0
seen = set()
lst = []
while True:
    i += 1
    break_true = False
    while True:
        if break_true:
            if i == 1:
                print("1)", reg[1])
            if reg[1] in seen:
                if len(lst) == 25000:
                    p2 = max(seen, key=lambda x: lst.index(x))
                    print("2)", p2)
                    exit()
            seen.add(reg[1])
            lst.append(reg[1])

            break

        reg[2] = reg[1] | 65536  # 6
        reg[1] = 8725355  # 7
        while True:
            reg[5] = reg[2] & 255  # 8
            reg[1] += reg[5]  # 9
            reg[1] &= 16777215  # 10
            reg[1] *= 65899  # 11
            reg[1] &= 16777215  # 12

            reg[2] = reg[2] // 256

            if reg[2] == 0:
                break_true = True
                break

    break_true = False
