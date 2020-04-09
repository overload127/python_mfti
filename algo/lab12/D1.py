#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pprint
import math

def total_count(n):
    mas = [999999999] * n
    start = -1
    mid = -1
    end = -1
    if n == 0:
        return 0

    start = int(input())
    if n < 2:
        return 0

    mid = int(input())
    if n == 2:
        return abs(mid-start)

    mas[0] = 0
    mas[1] = abs(start-mid)
    for i in range(2, n-2+1+1):
        end = int(input())
        # print(start, mid, end)
        # step = abs(end-mid)
        # super_step = 3*abs(end-start)
        mas[i] = min(abs(end-mid)+mas[i-1], 3*abs(end-start)+mas[i-2], mas[i])

        start = mid
        mid = end
    # pprint.pprint(mas)
    return mas[-1]

n = int(input())
print(total_count(n))