#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pprint


#N = int(input())
#W = int(input())
#predmet = []
#for i in range(N):
#    predmet.append((int(input()),int(input())))
N = 5
W = 13
predmet = [(3, 1), (4, 6), (5, 4), (8, 7), (9, 6)]

predmet.sort(key = lambda line: line[0])

mas = [[0]*(W+1) for i in range(N+1)]
for j in range(1, N+1):
    for i in range(0, W+1):
        if predmet[j-1][0] > i:
            mas[j][i] = mas[j-1][i]
        else:
            mas[j][i] = max(mas[j-1][i], mas[j-1][i-predmet[j-1][0]] + predmet[j-1][1])
pprint.pprint(predmet)
pprint.pprint(mas)
print(max(mas[-1]))