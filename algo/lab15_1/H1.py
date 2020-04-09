#!/usr/bin/env python3
# -*- coding: utf-8 -*-

up = down = 0

for ch in input():
    n = ord(ch)
    if n >= 97 and n <= 122:
        down += 1
    elif n >= 65 and n <= 90:
        up += 1

print(up, down)