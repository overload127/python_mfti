#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
4 4
0 1 -1
1 2 -1
2 3 -1
3 1 -1
0

9 14
0 1 2
0 7 15
1 2 1
1 3 5
2 6 1
2 5 2
2 3 3
3 5 4
3 4 6
6 5 1
5 7 3
5 4 7
7 8 12
4 8 2
0
"""
from collections import deque


def get_input():
    n, m = [int(line) for line in input().split()]

    edges = [None] * m
    for i in range(m):
        a, b, price = [line for line in input().split()]
        edges[i] = (int(a), int(b), float(price))

    start = int(input())

    return edges, start, n


def get_price_to_all_vertex(edges, start, n):
    # считываем граф, преобразуем его в список ребер, который храним в edges
    d1 = [None] * n  # Считаем, что n - кол-во вершин, вершины пронумерованы от 0
    d1[start] = 0  # s - стартовая вершина
    # INF - заведомо большое число
    INF = 999999999
    for i in range(n-1):
        for u, v, w in edges:
            if d1[u] is not None:
                d1[v] = min(INF if d1[v] is None else d1[v], d1[u] + w)

    return d1


def main():
    edges, start, n = get_input()

    shortest_price = get_price_to_all_vertex(edges, start, n)

    print('{:10} = {:10}'.format('vertex', 'price'))
    for i, price in enumerate(shortest_price):
        print('{:10} = {:10}'.format(i, price))

main()
