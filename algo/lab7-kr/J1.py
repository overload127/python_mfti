#!/usr/bin/env python3
# -*- coding: utf-8 -*-

mas = []
tmp = [0] * 3
N = int(input())
i = 0
while i < N:
    j = 0
    mas.append(list())
    while j < 3:
        mas[i].append(int(input()))
        j += 1
    i += 1

all_doski = []
M = int(input())
i = 0
while i < M:
    all_doski.append(int(input()))
    i += 1

for doska in all_doski:
    color = 0
    for line in mas[::-1]:
        if line[0] <= doska <= line[1]:
            color = line[2]
            break
    print(color)
