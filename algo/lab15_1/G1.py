#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pprint

n = int(input())
mas = [[1]*(n+1) for i in range(n+1)]


for k in range(1, n+1):
    for i in range(1, n+1):
        mas[k][i] = mas[k-1][i] + mas[k][i-1]

for i in range(n+1):
    y = i
    x = 0
    while y >= 0 and x <= i:
        print(mas[y][x], end=' ')
        x += 1
        y -= 1
    print()