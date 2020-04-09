#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def check(n: int, max_n) -> bool:
    return n // 2 * 2 == n and max_n < n

data = 0

try:
    tmp = int(input())
    if tmp == 0:
        print(0)
        exit()
    while tmp != 0:
        if check(tmp, data):
            data = tmp
        tmp = int(input())
except ValueError:
    exit()

print(data)
