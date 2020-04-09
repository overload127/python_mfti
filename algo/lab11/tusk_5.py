#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pprint


def ferz(n, m):
    kletka = [['+'] * (m+1) for i in range(n+1)]

    N = [True] * (n+1)
    M = [True] * (m+1)
    D = [True] * (n+m-1)

    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            if (N[i] and M[j] and D[i-j+m]):
                kletka[i][j] = '-'
                N[i] = False
                M[j] = False
                D[i-j+m] = False
                break

    return kletka


tmp = ferz(1, 11)
for line in tmp:
    str_line = ''
    for j in line:
        str_line = ''.join((str_line, j, ' '))
    print(str_line)
