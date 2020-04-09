#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def pi(line):
    length = len(line)
    p = [0] * length
    for i in range(1, length):
        j = p[i-1]
        while j > 0 and line[j] != line[i]:
            j = p[j]
        if line[j] == line[i]:
            p[i] = j + 1
    return p


def find_all_vhod(line_1, line_2):
    length_2 = len(line_2)
    length_1 = len(line_1)
    line_3 = '#'.join((line_1, line_2))
    p = pi(line_3)
    return p[length_1+1:]


s = input()
k = int(input())
#k = -2
#s = 'abcdabcd'
res = ''
if k > 0:
    for i in (range(k)):
        res = ''.join((res, s))
elif k < 0:
    k = abs(k)
    length_1 = len(s)
    if length_1 % k:
        res = 'NO SOLUTION'
    else:
        length_2 = length_1 // k
        vhod = find_all_vhod(s[:length_2], s)
        flag = True
        for i in range(length_2-1, length_1, length_2):
            if vhod[i] != length_2:
                flag = False
                break
        if flag:
            res = s[:length_2]
        else:
            res = 'NO SOLUTION'
else:
    res = 'NO SOLUTION'

print(res)