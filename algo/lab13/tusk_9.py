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


def sjatb1(string_a, len_str):
    z = p_func(string_a, len_str)
    pod_str_id = len_str - max(z)
    if pod_str_id > len_str//2:
        pod_str_id = len_str
    return pod_str_id


def sjatb2(string_a, len_str):
    z = p_func(string_a, len_str)
    k = len_str - z[-1]
    if not(len_str % k):
        return k
    return len_str


if __name__ == "__main__":
    tmp1 = "bbb-bbb-"
    len_str = len(tmp1)

    pod_str_id = sjatb1(tmp1, len_str)
    print(f'tmp1 = {tmp1}')
    tmp1_feom_pod = tmp1[:pod_str_id]*(len_str//pod_str_id)
    print(f'tmp1 = {tmp1_feom_pod}')
    print(f'pod_ = {tmp1[:pod_str_id]}')

    pod_str_id = sjatb2(tmp1, len_str)
    print(f'tmp1 = {tmp1}')
    tmp1_feom_pod = tmp1[:pod_str_id]*(len_str//pod_str_id)
    print(f'tmp1 = {tmp1_feom_pod}')
    print(f'pod_ = {tmp1[:pod_str_id]}')
