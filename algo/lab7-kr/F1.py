#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def algo_evk(A, B):
    D = 0
    while True:
        ost = A % B
        if ost == 0:
            D = B
            break
        A, B = B, ost
    print(D)


A = 0
B = 0
try:
    A = int(input())
    B = int(input())
except ValueError:
    exit(2)

if A == 0 or B == 0:
    print(0)
else:
	A, B = max(A, B), min(A, B)
    algo_evk(A, B)
