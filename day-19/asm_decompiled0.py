"""#ip 2
addi 2 16 2
seti 1 2 4
seti 1 8 1
mulr 4 1 5
eqrr 5 3 5
addr 5 2 2
addi 2 1 2
addr 4 0 0
addi 1 1 1
gtrr 1 3 5
addr 2 5 2
seti 2 6 2
addi 4 1 4
gtrr 4 3 5
addr 5 2 2
seti 1 2 2
mulr 2 2 2
addi 3 2 3
mulr 3 3 3
mulr 2 3 3
muli 3 11 3
addi 5 2 5
mulr 5 2 5
addi 5 8 5
addr 3 5 3
addr 2 0 2
seti 0 4 2
setr 2 5 5
mulr 5 2 5
addr 2 5 5
mulr 2 5 5
muli 5 14 5
mulr 5 2 5
addr 3 5 3
seti 0 8 0
seti 0 5 2
"""

ip_reg = 2
reg = [1, 0, 0, 0, 0, 0]

# addi 2 16 2 | ip=0
reg[2] += 17

# seti 1 2 4
reg[4] = 1
reg[2] += 1

# seti 1 8 1
reg[1] = 1
reg[2] += 1

# mulr 4 1 5
reg[5] = reg[4] * reg[1]
reg[2] += 1

# eqrr 5 3 5
reg[5] = int(reg[5] == reg[3])
reg[2] += 1

# addr 5 2 2
reg[2] += reg[5] + 1

# addi 2 1 2
reg[2] += 2

# addr 4 0 0
reg[0] += reg[4]

# addi 1 1 1
reg[1] += 1
reg[2] += 1

# gtrr 1 3 5
reg[5] = int(reg[1] > reg[2])
reg[2] += 1

# addr 2 5 2
reg[2] += reg[5] + 1

# seti 2 6 2
reg[2] = 3

# addi 4 1 4
reg[4] += 1
reg[2] += 1

# gtrr 4 3 5
reg[5] = int(reg[4] > reg[3])
reg[2] += 1
# addr 5 2 2
reg[2] += reg[5] + 1
# seti 1 2 2
reg[2] = 2
# mulr 2 2 2
reg[2] = reg[2] * reg[2] + 1

# addi 3 2 3
reg[3] += 2
reg[2] += 1

# mulr 3 3 3
reg[3] = reg[3] * reg[3]
reg[2] += 1

# mulr 2 3 3
reg[3] = reg[2] * reg[3]
reg[2] += 1

# muli 3 11 3
reg[3] *= 11
reg[2] += 1

# addi 5 2 5
reg[5] += 2
reg[2] += 1

# mulr 5 2 5
reg[5] *= 2
reg[2] += 1

# addi 5 8 5
reg[5] += 8
reg[2] += 1

# addr 3 5 3
reg[3] += reg[5]
reg[2] += 1

# addr 2 0 2
reg[2] += reg[0] + 1

# seti 0 4 2
reg[2] = 1

# setr 2 5 5
reg[5] = reg[2]
reg[2] += 1

# mulr 5 2 5
reg[5] *= reg[2]
reg[2] += 1

# addr 2 5 5
reg[5] += reg[2]
reg[2] += 1

# mulr 2 5 5
reg[5] *= reg[2]
reg[2] += 1

# muli 5 14 5
reg[5] *= 14
reg[2] += 1

# mulr 5 2 5
reg[5] *= reg[2]
reg[2] += 1

# addr 3 5 3
reg[3] += reg[5]
reg[2] += 1

# seti 0 8 0
reg[0] = 0
reg[2] += 1

# seti 0 5 2
reg[2] = 1
