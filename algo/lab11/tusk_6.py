#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pprint


def ferz(n, m):
    kletka = [['+'] * (m+1) for i in range(n+1)]

    for i in range(n-1, -1, -1):
        for j in range(m-1, -1, -1):
            if (kletka[i+1][j+1] == '+' and
               kletka[i][j+1] == '+' and
               kletka[i+1][j] == '+' ):
                kletka[i][j] = '-'

    return kletka


tmp = ferz(5, 2)
for line in tmp:
    str_line = ''
    for j in line:
        str_line = ''.join((str_line, j, ' '))
    print(str_line)
