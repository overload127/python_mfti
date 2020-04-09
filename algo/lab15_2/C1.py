#!/usr/bin/env python3
# -*- coding: utf-8 -*-


n = int(input())
maximum = 0
flag = False
cur_max = 0

for i in range(n):
    line = input()
    
    if line == '1':
        flag = True
        cur_max += 1
    else:
        if flag:
            flag = False
            if maximum < cur_max:
                maximum = cur_max
            cur_max = 0

if maximum < cur_max:
    maximum = cur_max

print(maximum)