#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pprint
N = 10
M = 8

kletka = [[0]*M for i in range(N)]
kletka[1][1]=1

for i in range(1,N):
    for j in range(1,M):
        if not i==j==1:
            kletka[i][j]=kletka[i-1][j]+kletka[i][j-1]



pprint.pprint(kletka)