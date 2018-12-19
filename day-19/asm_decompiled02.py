ip_reg = 2
reg = [1, 0, 0, 0, 0, 0]
ip = 0

while True:
    reg[2] += 17  # 0
    reg[4] = 1  # 1
    reg[1] = 1  # 2
    reg[5] = reg[4] * reg[1]  # 3
    reg[5] = int(reg[5] == reg[3])  # 4
    reg[2] = 6 + reg[5]  # 5
    reg[2] = 8  # 6
    reg[0] += reg[4]  # 7
    reg[1] += 1  # 8
    reg[5] = int(reg[1] > reg[3])  # 9
    reg[2] = 11 + reg[5]  # 10
    reg[2] = 3  # 11
    reg[4] += 1  # 12
    reg[5] = int(reg[4] > reg[3])  # 13
    reg[2] = 15 + reg[5]  # 14
    reg[2] = 2  # 15
    [print(reg), exit()]  # 16
    reg[3] += 2  # 17
    reg[3] = reg[3] * reg[3]  # 18
    reg[3] = 19 * reg[3]  # 19
    reg[3] *= 11  # 20
    reg[5] += 2  # 21
    reg[5] *= 22  # 22
    reg[5] += 8  # 23
    reg[3] += reg[5]  # 24
    reg[2] = 26 + reg[0]  # 25
    reg[2] = 1  # 26
    reg[5] = 27  # 27
    reg[5] *= 28  # 28
    reg[5] += 29  # 29
    reg[5] *= 30  # 30
    reg[5] *= 14  # 31
    reg[5] *= 32  # 32
    reg[3] += reg[5]  # 33
    reg[0] = 0  # 34
    reg[2] = 1  # 35
