#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Версия решения через граф. В очередь будут помещены все начальные
# координаты друг за другом. Таким образом не придётся10 раз создавать карты глубины.
from collections import deque


def get_input():
    n, m = [int(line) for line in input().split()]

    graph = {i: set() for i in range(n*m)}
    all_start = []
    for k in range(n):
        line = input().split()
        for i in range(m):
            if line[i] == '1':
                all_start.append(k*m+i)
            if 0 <= i - 1 <= m - 1:
                graph[k*m+i].add(k*m+i-1)
                graph[k*m+i-1].add(k*m+i)
            if 0 <= k - 1 <= n - 1:
                graph[k*m+i].add((k-1)*m+i)
                graph[(k-1)*m+i].add(k*m+i)

    return graph, all_start, n, m


def owg(graph, start, l):
    ost_graph_reb = []
    queue = deque(start)
    # lenght = {v: None for v in graph}
    lenght = [None] * l
    for ch in start:
        lenght[ch] = 0
    while queue:
        vertex = queue.popleft()
        for next_vertex in graph[vertex]:
            if lenght[next_vertex] is None:
                lenght[next_vertex] = lenght[vertex] + 1
                queue.append(next_vertex)
                ost_graph_reb.append(' '.join((str(vertex), str(next_vertex))))

    return lenght


def main():
    graph, all_start, n, m = get_input()

    table = owg(graph, all_start, n*m)

    for i in range(n):
        print(' '.join(map(str, table[i*m:i*m+m])))


main()
