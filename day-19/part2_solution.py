# decompiled-by-hand
# from asm from data.txt
# it's been a real hell this one
# i couldnt spot it was looking for the divisors...

# i'm not even gonna refector or clean this one up

ip_reg = 2
reg = [1, 0, 0, 0, 0, 0]
ip = 0

ip = 17  # 0

while True:
    cond_goto_17 = ip == 17
    while not cond_goto_17:
        # basicly it looks for the sum
        # of all the divisors of reg[3]
        sqrt = int((reg[3]) ** (1 / 2))

        divisors = set()
        for x in range(1, sqrt + 1):
            reg[1] = 1  # 2
            cond_goto_3 = True
            if reg[3] % x == 0:
                divisors.add(x)
                divisors.add(reg[3] // x)

            if x % 25000 == 0:
                print("goto_2", reg)
                pass

        reg[0] = sum(divisors)

        print("2)", reg[0])
        exit()

    # here it constructs reg[3] - all the code below
    # is being run only once

    reg[3] = ((reg[3] + 2) ** 2) * 19 * 11  # 17
    reg[5] = (reg[5] + 2) * 22 + 8  # 21
    reg[3] += reg[5]  # 24

    if reg[0] == 0:
        # print("bef27", reg)
        continue
    if reg[0] == 1:
        reg[5] = 27  # 27
    if reg[0] <= 2:
        reg[5] *= 28  # 28
    if reg[0] <= 3:
        reg[5] += 29  # 29
    if reg[0] <= 4:
        reg[5] *= 30  # 30
    if reg[0] <= 5:
        reg[5] *= 14  # 31
    if reg[0] <= 6:
        reg[5] *= 32  # 32
    if reg[0] <= 7:
        reg[3] += reg[5]  # 33
    if reg[0] <= 8:
        reg[0] = 0  # 34

    ip = 1
