#!/usr/bin/env python3
# -*- coding: utf-8 -*-

def fac(n):
    if n == 0:
        return 1
    else:
        return n * fac(n - 1)

i = 0
while True:
    print(f"test rec [{i}]")
    fac(i)
    i += 1

# функция сделала 1024 вызова
# А системная фукция sys.getrecursionlimit()
# сообщает о максимальной глубине в 1000 
