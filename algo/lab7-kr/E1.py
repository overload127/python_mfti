#!/usr/bin/env python3
# -*- coding: utf-8 -*-

data = [0,0,1]
number = 2

try:
    found = int(input())
    if found == 0:
        print(0)
        exit()
    while data[-1] <= found:
        number += 1
        tmp = sum(data)
        data[:-1] = data[1:]
        data[-1] = tmp
except ValueError:
    exit()

print(number)
