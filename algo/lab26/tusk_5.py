#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
4 4
0 1 -1
1 2 -1
2 3 -1
3 1 -1
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
    for i in range(n):
        if i < n-1:
            for u, v, w in edges:
                if d1[u] is not None:
                    d1[v] = min(INF if d1[v] is None else d1[v], d1[u] + w)
        else:
            d2 = d1.copy()
            for u, v, w in edges:
                if d2[u] is not None:
                    d2[v] = min(INF if d2[v] is None else d2[v], d2[u] + w)

    path = 'Циклов нет'
    for i in range(n):
        if d1[i] != d2[i]:
            path = []
            cur_vertex = i
            cur_price = d1[i]
            path.append(i)
            nxt = True
            while nxt:
                nxt = False
                for u, v, w in edges:
                    if cur_vertex == u and cur_price - w == d1[v]:
                        cur_vertex = v
                        cur_price = d1[v]
                        path.append(v)
                        nxt = True
                        break
                    elif cur_vertex == v and cur_price - w == d1[u]:
                        cur_vertex = u
                        cur_price = d1[u]
                        path.append(u)
                        nxt = True
                        break
            break

    return d1, path


def main():
    edges, start, n = get_input()

    shortest_price, path = get_price_to_all_vertex(edges, start, n)

    print('{:10} = {:10}'.format('vertex', 'price'))
    for i, price in enumerate(shortest_price):
        print('{:10} = {:10}'.format(i, price))

    print()
    print(path)


main()
