"""seti 123 0 1  # reg[1] = 123
bani 1 456 1     # reg[1] &= 456
eqri 1 72 1      # reg[1] = int(reg[1] == 72)  [ip=2]
addr 1 4 4       # reg[4] == reg[1] + reg[4]  JUMP TO [5 if reg[1] else 4] 
seti 0 0 4       # loop if test fails
seti 0 7 1       # reg[1] = 0
bori 1 65536 2   # reg[2] = reg[1] | 65536
seti 8725355 6 1 # reg[1] = 8725355
bani 2 255 5     # reg[5] = reg[2] & 255
addr 1 5 1       # reg[1] += reg[5]
bani 1 16777215 1# reg[1] &= 16777215
muli 1 65899 1   # reg[1] *= 65899
bani 1 16777215 1# reg[1] &= 16777215
gtir 256 2 5     # reg[5] = int(256 > reg[2])
addr 5 4 4       # reg[4] += reg[5]  JUMP TO 16 if reg[5] else 15
addi 4 1 4       # reg[4] += 1 JUMP TO 17 
seti 27 8 4      # reg[4] = 27 JUMP TO 28
seti 0 0 5       # reg[5] = 0
addi 5 1 3       # reg[3] = reg[5] + 1
muli 3 256 3     # reg[3] *= 256
gtrr 3 2 3       # reg[3] = int(reg[3] > reg[2])
addr 3 4 4       # reg[4] += reg[3]  JUMP TO 23 if reg[3] > reg[2] else 22
addi 4 1 4       # reg[4] += 1  JUMP TO 24
seti 25 1 4      # reg[4] = 25
addi 5 1 5       # reg[5] += 1
seti 17 9 4      # reg[4] = 17 JUMP TO 18
setr 5 1 2       # reg[2] = reg[5]
seti 7 6 4       # reg[4] = 7 JUMP TO 8
eqrr 1 0 5       # reg[5] = int(reg[1] == reg[0])
addr 5 4 4       # reg[4] += reg[5] JUMP TO 31 [EXIT] if reg[1] == reg[0] else 30 
seti 5 7 4       # reg[4] = 5 JUMP TO 6
"""

