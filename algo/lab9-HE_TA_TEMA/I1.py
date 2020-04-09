#!/usr/bin/env python3
# -*- coding: utf-8 -*-


n = input()
A = [int(i) for i in input().split()]

r1=r2=0
# предположим что перый - рыцарь
cur=1
for i in A:
    if cur:
        r1+=1
        cur = cur and i
    else:
        cur = not(i)
cur=0
for i in A:
    if cur:
        r2+=1
        cur = cur and i
    else:
        cur = not(i)

print(min(r1,r2))
