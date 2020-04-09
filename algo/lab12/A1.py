#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pprint

N = M = 8

# x - M
# y - N
# kletka[x][y]
kletka_1 = [[3]*(N) for i in range(M)]

def konb1(hod, x, y):
    if hod >= kletka_1[x][y]:
        return

    kletka_1[x][y] = hod

    if x > 0 and y > 1:
        konb1(hod+1, x-1, y-2)
    if x > 1 and y > 0:
        konb1(hod+1, x-2, y-1)
    if x > 0 and y < N-1-1:
        konb1(hod+1, x-1, y+2)
    if x > 1 and y < N-1-0:
        konb1(hod+1, x-2, y+1)
    if x < M-1-0 and y > 1:
        konb1(hod+1, x+1, y-2)
    if x < M-1-1 and y > 0:
        konb1(hod+1, x+2, y-1)
    if x < M-1-0 and y < N-1-1:
        konb1(hod+1, x+1, y+2)
    if x < M-1-1 and y < N-1-0:
        konb1(hod+1, x+2, y+1)


x1 = int(input())
y1 = int(input())
x2 = int(input())
y2 = int(input())

konb1(0, x1-1, y1-1)

if kletka_1[x2-1][y2-1] not in [0,1,2]:
    print(-1)
else:
    print(kletka_1[x2-1][y2-1])