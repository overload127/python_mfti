#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
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

    graph = {}
    for _ in range(m):
        a, b, price = [int(line) for line in input().split()]
        price = float(price)
        add_vertex(graph, a, b, price)
        add_vertex(graph, b, a, price)

    start = int(input())

    return graph, start, n


def add_vertex(graph, a, b, price):
    if a not in graph:
        graph[a] = set()
    graph[a].add((b, price))


def get_price_to_all_vertex(graph, start, n):
    INF = 999999
    # считываем граф, преобразуем его в список смежности, который храним в graph
    # INF - заведомо большое число
    d = [INF] * n  # Считаем, что n - кол-во вершин, вершины пронумерованы от 0
    d[start] = 0  # s - стартовая вершина
    used = [False] * n
    while True:
        u = -1
        for i in range(n):
            if not used[i] and (u == -1 or d[u] > d[i]):
                u = i
        if u == -1:
            break
        used[u] = True
        for v, w in graph[u]:
            d[v] = min(d[v], d[u] + w)

    return d


def main():
    graph, start, n = get_input()

    shortest_price = get_price_to_all_vertex(graph, start, n)

    print('{:10} = {:10}'.format('vertex', 'price'))
    for i, price in enumerate(shortest_price):
        print('{:10} = {:10}'.format(i, price))


main()
