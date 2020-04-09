#!/usr/bin/env python3
# -*- coding: utf-8 -*-

line = int(input())
maximum = line
count_max = 0
count_all = 0
while line != 0:
    count_all += 1
    if line > maximum:
        maximum = line
        count_max = 1
    elif line == maximum:
        count_max += 1
    else:
        pass
    line = int(input())

print(count_all-count_max)