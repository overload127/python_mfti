#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pprint


def z_func_triv(s, n):
    z = [0] * n
    r = 0
    l = 0

    for j in range(1, n):
        if j <= r:
            z[j] = min(r-j+1,z[j-l])
        while j + z[j] < n and s[z[j]] == s[j + z[j]]:
            z[j] += 1
        if j+z[j]-1 > r:
            l = j
            r = j + z[j] - 1

    return z


def serch_pod(string_a, string_b):
    string_full = '#'.join((string_b, string_a))
    length_a = len(string_a)
    length_b = len(string_b)
    length_full = len(string_full)
    
    z = z_func_triv(string_full, length_full)
    vhod = []
    i = length_b + 1
    while i < length_full:
        if z[i] == length_b:
            vhod.append(i-length_b-1)
        i += z[i] + 1
    return vhod


if __name__ == "__main__":
    tmp1 = 'abacaba'
    print(z_func_triv(tmp1, len(tmp1)))
    tmp2 = 'aba'

    print(serch_pod(tmp1, tmp2))
        