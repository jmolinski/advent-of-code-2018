ip_reg = 2
reg = [1, 0, 0, 0, 0, 0]

# addi 2 16 2 | ip=0
reg[2] += 17

# seti 1 2 4 | ip=1
reg[4] = 1
reg[2] = 2

# seti 1 8 1 | ip=2
reg[1] = 1
reg[2] = 3

# mulr 4 1 5 | ip=3
reg[5] = reg[4] * reg[1]
reg[2] = 3

# eqrr 5 3 5 | ip=4
reg[5] = int(reg[5] == reg[3])
reg[2] = 5

# addr 5 2 2 | ip=5
reg[2] = 6 + reg[5]

# addi 2 1 2 | ip=6
reg[2] = 8

# addr 4 0 0 | ip=7
reg[0] += reg[4]
reg[2] = 8

# addi 1 1 1 | ip=8
reg[1] += 1
reg[2] = 9

# gtrr 1 3 5 | ip=9
reg[5] = int(reg[1] > reg[3])
reg[2] = 10

# addr 2 5 2 | ip=10
reg[2] = 11 + reg[5]

# seti 2 6 2 | ip=11
reg[2] = 3

# addi 4 1 4 | ip=12
reg[4] += 1
reg[2] = 13

# gtrr 4 3 5 | ip=13
reg[5] = int(reg[4] > reg[3])
reg[2] = 14

# addr 5 2 2 | ip=14
reg[2] = 15 + reg[5]

# seti 1 2 2 | ip=15
reg[2] = 2

# mulr 2 2 2 | ip=16
reg[2] = 16 * 16 + 1  # 257 = exit?

# addi 3 2 3 | ip=17
reg[3] += 2
reg[2] = 18

# mulr 3 3 3 | ip=18
reg[3] = reg[3] * reg[3]
reg[2] = 19

# mulr 2 3 3 | ip=19
reg[3] = 19 * reg[3]
reg[2] = 20

# muli 3 11 3 | ip=20
reg[3] *= 11
reg[2] = 21

# addi 5 2 5 | ip=21
reg[5] += 2
reg[2] = 22

# mulr 5 2 5 | ip=22
reg[5] *= 22
reg[2] = 23

# addi 5 8 5 | ip=23
reg[5] += 8
reg[2] = 24

# addr 3 5 3 | ip=24
reg[3] += reg[5]
reg[2] = 25

# addr 2 0 2 | ip=25
reg[2] = 26 + reg[0]

# seti 0 4 2 | ip=26
reg[2] = 1

# setr 2 5 5 | ip=27
reg[5] = 27
reg[2] = 28

# mulr 5 2 5 | ip=28
reg[5] *= 28
reg[2] = 29

# addr 2 5 5 | ip=29
reg[5] += 29
reg[2] = 30

# mulr 2 5 5 | ip=30
reg[5] *= 30
reg[2] = 31

# muli 5 14 5 | ip=31
reg[5] *= 14
reg[2] = 32

# mulr 5 2 5 | ip=32
reg[5] *= 32
reg[2] = 33

# addr 3 5 3 | ip=33
reg[3] += reg[5]
reg[2] = 34

# seti 0 8 0 | ip=34
reg[0] = 0
reg[2] = 35

# seti 0 5 2 | ip=35
reg[2] = 1
