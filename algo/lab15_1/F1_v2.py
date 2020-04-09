#!/usr/bin/env python3
# -*- coding: utf-8 -*-


total = int(input())

all_proc = [int(proc) for proc in input().split()]
length = len(all_proc)
all_profit = [0] * (length + 1)
patch = [0] * (length + 1)
maximum = (0, total)
best_patch = []

if length > 1:
    all_profit[0] = total
    patch[0] = -1
    all_profit[1] = -100000000000
    patch[1] = -1
    all_profit[2] = all_profit[0] + all_proc[2]
    patch[2] = 0
    if maximum[1] < all_profit[2]:
        maximum = (2, all_profit[2])
    if length > 2:
        for i in range(3, length):
            if all_profit[i-2] > all_profit[i-3]:
                all_profit[i] = all_profit[i-2] + all_proc[i]
                patch[i] = i - 2
            else:
                all_profit[i] = all_profit[i-3] + all_proc[i]
                patch[i] = i - 3
            if maximum[1] < all_profit[i]:
                maximum = (i, all_profit[i])

best_patch.append(maximum[0])

while best_patch[-1] > 0:
    best_patch.append(patch[best_patch[-1]])

print(best_patch[-1]+1, end='')

for i in range(len(best_patch)-2, -1, -1):
    print(' ', end=str(best_patch[i]+1))
