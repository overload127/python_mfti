#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Версия решения через граф. В очередь будут помещены все начальные
# координаты друг за другом. Таким образом не придётся10 раз создавать карты глубины.
from collections import deque


def get_input():
    n, m = [int(line) for line in input().split()]

    graph = {str(i): set() for i in range(n*m)}
    all_start = []
    for k in range(n):
        line = input().split()
        for i in range(m):
            if line[i] == '1':
                all_start.append(str(k*m+i))
            if 0 <= i - 1 <= m - 1:
                graph[str(k*m+i)].add(str(k*m+i-1))
                graph[str(k*m+i-1)].add(str(k*m+i))
            if 0 <= k - 1 <= n - 1:
                graph[str(k*m+i)].add(str((k-1)*m+i))
                graph[str((k-1)*m+i)].add(str(k*m+i))

    return graph, all_start, n, m


def owg(graph, all_start, l):
    ost_graph_reb = []
    queue = deque()
    lenght = {v: None for v in graph}
    # lenght = [None] * l
    for ch in all_start:
        lenght[ch] = 0
        queue.append(ch)
    while queue:
        vertex = queue.popleft()
        for next_vertex in graph[vertex]:
            if lenght[next_vertex] is None:
                lenght[next_vertex] = lenght[vertex] + 1
                queue.append(next_vertex)
                ost_graph_reb.append(' '.join((str(vertex), str(next_vertex))))

    return lenght


def print1(table, n, m):
    for i in range(n):
        line = [None] * m
        for j in range(m):
            line[j] = str(table[str(i*m+j)])
        print(' '.join(line))


def print2(table, n, m):
    for i in range(n):
        for j in range(m):
            print(table[str(i*m+j)], end=' ')
        print()


def main():
    graph, all_start, n, m = get_input()

    table = owg(graph, all_start, n*m)

    print2(table, n, m)


main()
