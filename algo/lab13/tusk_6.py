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


def serch(string_main, string_pod):
    all_vhod = []
    length_pod = len(string_pod)
    string_all = '#'.join((string_pod, string_main))
    length_all = len(string_all)
    pi = p_func(string_all, length_all)
    for i in range(length_pod+1, length_all):
        if pi[i] == length_pod:
            all_vhod.append(i-length_pod*2)

    return all_vhod

if __name__ == "__main__":
    tmp1 = "abacaba"
    tmp2 = 'aba'
    print(serch(tmp1, tmp2))
