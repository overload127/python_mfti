#!/usr/bin/env python3
# -*- coding: utf-8 -*-


n = int(input())
res = 0
all_date = [0] * (n+1)


if n != 0 and not(n % 2):
    all_date[0] = 1
    all_date[2] = 3
    if n > 2:
        all_date[4] = 11
    for i in range(6, n+1, 2):
        all_date[i] = 4 *all_date[i-2] - all_date[i-4]

    
    res = all_date[n]

print(res)
