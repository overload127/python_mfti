#!/usr/bin/env python3
# -*- coding: utf-8 -*-7


def pi(s, n):
    pi = [0] * n

    for i in range(1, n):
        j = pi[i-1]
        while j > 0 and s[j] != s[i]:
            j = pi[j-1]
        if s[i] == s[j]:
            pi[i] = j + 1

    return pi


def main():
    tmp = input()
    # tmp = "abcabcabc"
    n = len(tmp)
    p = pi(tmp, n)
    # print(p)
    print(n//(n - p[-1]))


main()