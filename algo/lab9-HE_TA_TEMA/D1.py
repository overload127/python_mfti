#!/usr/bin/env python3
# -*- coding: utf-8 -*-

PRICE, DELTA, M = 0, 1, 2

day = 1
week = 0

mas = [int(i) for i in input().split()]

total = 0

while True:
    if day == 8:
        day = 1
        week += 1
    if week >= mas[M]:
        break

    total += mas[PRICE]
    mas[PRICE] += mas[DELTA]
    day += 1

print(total)
