#!/usr/bin/env python3

ss = input()

m = [0]*4
for i, s in enumerate(ss.split()):
    m[i] = int(s)

while m[0] < m[2]:
    m[0] += int(m[0] * m[1])/100
    m[3] += 1


print(m[3])
