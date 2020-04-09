#!/usr/bin/env python3
# -*- coding: utf-8 -*-
res=0
vhod = int(input())

b = bin(vhod)
for ch in b[2:]:
    if ch == '1':
        res+=1
print(res)
