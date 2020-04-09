#!/usr/bin/env python3
# -*- coding: utf-8 -*-


line = [int(i) for i in input().split()]
year = 0

tmp = line[0] + line[0]*line[1] / 100
if tmp - line[0] < 1:
    print((line[2]-line[0]) * 100 // line[1])
    exit(0)

while line[0] <= line[2]:
    line[0] += (line[0]*line[1]) / 100
    year += 1

print(year)