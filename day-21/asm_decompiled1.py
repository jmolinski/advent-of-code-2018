"""
reg[2] = reg[1] | 65536 # 6
reg[1] = 8725355#7
reg[5] = reg[2] & 255 #8
reg[1] += reg[5] # 9
reg[1] &= 16777215 # 10
reg[1] *= 65899 # 11
reg[1] &= 16777215 # 12
reg[5] = int(256 > reg[2]) # 13
reg[4] += reg[5]  JUMP TO 28 if reg[5] else 17 # 14


reg[5] = 0  # 17
reg[3] = reg[5] + 1 # 18
reg[3] *= 256 # 19
reg[3] = int(reg[3] > reg[2]) # 20
reg[4] += reg[3]  JUMP TO 26 if reg[3] > reg[2] else 24 # 21


reg[5] += 1 # 24
reg[4] = 17 JUMP TO 18 #25
reg[2] = reg[5] # 26
reg[4] = 7 JUMP TO 8 # 27
reg[5] = int(reg[1] == reg[0])   # 28
reg[4] += reg[5] JUMP EXIT if reg[1] == reg[0] else 30  # 29
reg[4] = 5 JUMP TO 6 # 30
"""

