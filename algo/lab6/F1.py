#!/usr/bin/env python3

n = int(input())
a, b, c = 1, 3, 0
if n%2 == 1:
    b = 0
else:
    for i in range(1, n//2):      
        c = 4*b - a
        a = b
        b = c
print(b)
