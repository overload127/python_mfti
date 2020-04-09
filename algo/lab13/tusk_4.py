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


def sjatb1(string_a, len_str):
    z = z_func_triv(string_a, len_str)
    pod_str_id = len_str - max(z)
    if pod_str_id > len_str//2:
        pod_str_id = len_str
    return pod_str_id


def sjatb2(string_a, len_str):
    z = z_func_triv(string_a, len_str)
    for i in range(len(z)):
        if i+z[i] == len_str and not (len_str%i):
            return i
    return 0



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

