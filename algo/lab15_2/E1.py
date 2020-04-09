#!/usr/bin/env python3
# -*- coding: utf-8 -*-


n = int(input())
all_date = [[] for i in range(n)]
line = input()
while line != '#':
    student_id, value = [int(i) for i in line.split()]
    all_date[student_id].append(value)
    line = input()

all_date.sort(key=lambda x: sum(x), reverse=True)

for i in range(n):
    all_date[i].sort(reverse=True)
    for ch in all_date[i]:
        print(ch, end=' ')