#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
5
0 1 1 1 1
1 0 1 1 1
1 1 0 1 1
1 1 1 0 1
1 1 1 1 0
1 3
0 2 4
"""


def get_input():
    n = int(input())

    graph = [None for i in range(n)]
    for j in range(n):
        graph[j] = [9999 if int(i) == 0 else int(i) for i in input().split()]

    start = [int(line) for line in input().split()]
    end = [int(line) for line in input().split()]

    return graph, start, end, n


def tmp_fun(d, n):
    for k in range(n):
        for i in range(n):
            for j in range(n):
                d[i][j] = min(d[i][j], d[i][k]+d[k][j])


def display(graph):
    n = len(graph)

    print(('{:5}'*(n+1)).format(' ', *list(range(n))))
    for i in range(n):
        print(('{:5}'*(n+1)).format(i, *graph[i]))


def display_2_0(graph, start, end):
    l_e = len(end)
    line = [None] * (l_e + 1)
    print(('{:5}'*(l_e+1)).format(' ', *end))
    for s in start:
        i = 0
        line[i] = s
        i += 1
        for i, e in enumerate(end):
            line[i+1] = graph[s][e]
            i += 1
        print(('{:5}'*(l_e+1)).format(*line))


def main():
    graph, start, end, n = get_input()
    display(graph)
    tmp_fun(graph, n)
    display_2_0(graph, start, end)


main()
