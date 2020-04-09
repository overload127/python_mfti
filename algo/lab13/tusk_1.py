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


if __name__ == "__main__":
    tmp = "abacaba"
    print(z_func_triv(tmp, len(tmp)))
        