#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import deque


def get_input():
    n, m = [int(line) for line in input().split()]
    if n == 0 or m == 0:
        exit(0)

    x1, y1 = [int(line) for line in input().split()]
    start = x1 * m + y1
    x2, y2 = [int(line) for line in input().split()]
    end = x2 * m + y2

    graph = {i*m+j:set() for j in range(m) for i in range(n)}
    old_ch = 'X' * m
    for k in range(n):
        line = input()
        for i in range(m):
            if line[i] != 'X':
                if 0 <= i - 1 <= m - 1 and line[i-1] != 'X':
                    graph[k*m+i].add(k*m+i-1)
                    graph[k*m+i-1].add(k*m+i)
                if 0 <= k - 1 <= n - 1 and old_ch[i] != 'X':
                    graph[k*m+i].add((k-1)*m+i)
                    graph[(k-1)*m+i].add(k*m+i)

        old_ch = line

    return graph, start, end


def owg(graph, start, end):
    queue = deque([start])
    # lenght = {v: None for v in graph}
    lenght = [None] * len(graph)
    lenght[start] = 0
    while queue:
        vertex = queue.popleft()
        for next_vertex in graph[vertex]:
            if lenght[next_vertex] is None:
                lenght[next_vertex] = lenght[vertex] + 1
                queue.append(next_vertex)
            if next_vertex == end:
                return lenght[next_vertex]

    return "INF"


def main():
    graph, start, end = get_input()

    ans = owg(graph, start, end)
    print(ans)


main()
