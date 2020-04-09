#!/usr/bin/env python3

ss = input()

m = [0]*4
for i, s in enumerate(ss.split()):
    m[i] = int(s)

m[3] = (m[0]**2 +m[1]**2)**(1/2)
print("YES" if m[3] <= m[2] else "NO")
