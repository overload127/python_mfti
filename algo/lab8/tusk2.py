#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fibo(num, A = 0,B = 1):
    if num == 1:
        return B
    else:
        print(B)
        return fibo(num-1, B, A + B)



print(fibo(7))
