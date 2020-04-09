#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def algo1(n):
    mas = [0]*100
    try:
        while n > 0:
            i = int(input())
            mas[i] += 1
            n -= 1
    except ValueError:
        exit(2)
    mx = max(mas)
    while n < 100:
        if mas[n] == mx:
            print(n)
            break
        n += 1

try:
    n = int(input())
except ValueError:
    exit(2)
if n < 1:
    print(0)
algo1(n)
