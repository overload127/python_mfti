#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def pi_func(line):
    length = len(line)
    pi = [0] * length
    for i in range(1, length):
        old = pi[i-1]
        while old > 0 and line[old] != line[i]:
            old = pi[old-1]
        if line[old] == line[i]:
            old += 1
        pi[i] = old
    return pi

line_4 = 'abacabacabacaba'
line_1 = 'aaaaa'
length = len(line_1)
print('0 0', end = ' ')
for k in range(3,length+1):
    line_2 = line_1[:k]
    pi = pi_func(line_2)

    b = [0] * (k+1)
    for i in range(k):
        b[pi[i]] += 1
    for i in range(k-1, 0, -1):
        b[pi[i-1]] += b[i]
    maximum = 0
    for i in range(k-1, -1, -1):
        if b[i] >= 3:
            maximum = i
            break
    print(maximum, end = ' ')