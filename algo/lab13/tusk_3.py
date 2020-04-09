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


def serch_all_pod(string_a):
    pod_str_count = 0

    length_a = len(string_a)
    for i in range(1, length_a+1):
        pod_str_count += i - max(z_func_triv(string_a[:i][::-1], i))
    return pod_str_count


if __name__ == "__main__":
    tmp1 = 'abacaba'

    print(serch_all_pod(tmp1))
        