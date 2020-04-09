#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pprint

def count_hod(x, y):
    N = 9
    M = 9

    kletka = [[0]*M for i in range(N)]
    kletka[N-2][1]=1

    for i in range(N-2, -1, -1):
        for j in range(1, M):
            if ((not (i == N - 2 and j == 1)) and
               (not ((i == y-2 or i == y+2) and (j == x-1 or j == x+1))) and
               (not ((i == y-1 or i == y+1) and (j == x-2 or j == x+2))) and
               (not (i == y and j == x))):
                kletka[i][j]=kletka[i+1][j]+kletka[i][j-1]+kletka[i+1][j-1]
    # pprint.pprint(kletka)
    return kletka[0][8]

stroka = input()

print(count_hod(ord(stroka[0])-96, 8-int(stroka[1])))