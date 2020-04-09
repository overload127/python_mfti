#!/usr/bin/env python3
# -*- coding: utf-8 -*-

all_element = []
i = 0

total_3 = 0

line = input()
while line != '#':
    i += 1
    all_element.append(int(line))

    if i == 3:
        total_3 += (all_element[-1]+all_element[-2]+all_element[-3])%all_element[-1]
        i = 0

    line = input()

maximum = max(all_element)
minimum = min(all_element)
total = sum(all_element)
count = len(all_element)
sred = total / count

print(round(sred, 3), maximum, minimum, total_3)
