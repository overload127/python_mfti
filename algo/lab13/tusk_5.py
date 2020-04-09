#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pprint


def p_func2(s, n):
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
    tmp = "abacaba"
    print(p_func(tmp, len(tmp)))
