#!/usr/bin/env python3
# -*- coding: utf-8 -*-
line_1 = input()
dd = input()
line_2 = input()
res = False
if dd == '<':
    res = line_1 < line_2
else:
    res = line_1 > line_2

if res:
    print("YES")
else:
    print('NO')