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


def serch_all_pod(string_a):
    pod_str_count = 0

    length_a = len(string_a)
    for i in range(1, length_a+1):
        pod_str_count += i - max(p_func(string_a[:i][::-1], i))
    return pod_str_count


if __name__ == "__main__":
    tmp1 = 'abacaba'

    print(serch_all_pod(tmp1))