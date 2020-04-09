#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pprint


def p_func(s, n):
    p = [0] * n

    for i in range(1, n):
        j = p[i-1]
        while (j > 0 and s[j] != s[i]):
            j = p[j-1]
        if s[j] == s[i]:
            p[i] = j + 1

    return p


if __name__ == "__main__":
    n = int(input())
    patern = input()

    pi = p_func(patern+'#', n+1) 

    ch = ''
    i = 0
    j = 0
    vhod = []

    tmp1 = []
    tmp2 = []

    while ch != '0':
        i+=1
        ch = input()
        if ch == '0':
            continue
        # Чито для проверки значений
        tmp1.append(ch)
        tmp2.append(str(i-1))

        while j > 0 and patern[j] != ch:
            j = pi[j-1]

        if patern[j] == ch:
            j += 1

        if j == n:
            vhod.append(i-n)
            j -= 1
    
    print(vhod)
