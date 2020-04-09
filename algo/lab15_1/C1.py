#!/usr/bin/env python3
# -*- coding: utf-8 -*-

N = int(input())
max_day = 0
cur_day = 0
for line in input().split():
    line = int(line)
    if line > 0:
        cur_day += 1
    else:
        if cur_day > max_day:
            max_day = cur_day
        cur_day = 0
else:
    if cur_day > max_day:
        max_day = cur_day

print(max_day)