#!/usr/bin/env python3
# -*- coding: utf-8 -*-

tmp = int(input())

mas = [tmp]*10
mx = tmp
cur = 1
while True:
    while cur < 10:
        tmp = int(input())
        if tmp == 0:
            print(mx)
            exit(0)
        mas[cur] = tmp
        i = cur - 5
        if i < 0:
            i += 10
        if mx < mas[i]:
            mx = mas[i]
        cur += 1
    cur = 0
    
