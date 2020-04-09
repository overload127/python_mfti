#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import deque


def get_input():
    n, m, *ms = [int(line) for line in input().split()]

    country = {i: dict() for i in range(n)}

    for _ in range(m):
        a, b, p = [int(line) for line in input().split()]
        country[a][b] = p
        country[b][a] = p
    return country, n, ms


def get_tmp(country, n, ms):
    stack_vertex = set()
    INF = 1000*1000*10000
    l = [(INF, -1)] * n
    for s in ms:
        l[s] = (0, s)
        stack_vertex.add((s, 0, s))

    while stack_vertex:
        cur_s, cur_p, owner = min(stack_vertex, key=lambda ele: ele[1])
        stack_vertex -= {(cur_s, cur_p, owner)}
        for next_s, p in country[cur_s].items():
            if l[next_s][0] > l[cur_s][0] + cur_p:
                stack_vertex -= {(next_s, l[next_s][0], l[next_s][1])}
                l[next_s] = (l[cur_s][0] + cur_p, owner)
                stack_vertex.add((next_s, l[next_s][0], l[next_s][1]))

    return l


def main():

    country, n, ms = get_input()

    tmp = get_tmp(country, n, ms)

    for ele in tmp:
        print(ele[1])


main()
