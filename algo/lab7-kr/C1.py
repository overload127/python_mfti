#!/usr/bin/env python3
# -*- coding: utf-8 -*-

data = 0
i = 1

try:
    tmp = float(input())
    data += tmp
    if tmp == 0:
        print(0)
        exit()
    while tmp != 0:
        i += 1
        tmp = float(input())
        data += tmp
except ValueError:
    exit()
i -= 1

print(round(data/i,2))
