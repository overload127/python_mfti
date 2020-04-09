#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import deque


def get_input():
    n, m = [int(line) for line in input().split()]

    country = {i: dict() for i in range(n)}

    for _ in range(m):
        a, b, p = [int(line) for line in input().split()]
        country[a][b] = p
        country[b][a] = p
    return country, n


def get_capytal(country, n):
    minimumu_all_len = 1000*1000*10000
    capital = None
    for city in country:
        cur_all_len = owg(country, city, n)
        cur_sum_len = sum(cur_all_len)
        if minimumu_all_len > cur_sum_len:
            minimumu_all_len = cur_sum_len
            capital = city

    return capital


def owg(country, start, n):
    queue = deque([start])
    INF = 1000*1000*10000
    l = [INF] * n
    l[start] = 0
    while queue:
        cur_c = queue.popleft()
        for next_c, p in country[cur_c].items():
            if l[next_c] > l[cur_c] + p:
                l[next_c] = l[cur_c] + p
                queue.append(next_c)

    return l


def main():

    country, n = get_input()

    ans = get_capytal(country, n)

    print(ans)


main()
