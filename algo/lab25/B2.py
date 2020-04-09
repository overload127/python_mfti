#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import deque


def get_input():
    n, m = [int(line) for line in input().split()]
    if n == 0:
        exit(0)

    graph = {i: set() for i in range(n)}
    for _ in range(m):
        i, j = [int(line) for line in input().split()]

        graph[i].add(j)
        graph[j].add(i)
    return graph


def owg(graph, start):
    queue = deque([start])
    lenght = [None] * len(graph)
    lenght[start] = 0
    while queue:
        vertex = queue.popleft()
        for next_vertex in graph[vertex]:
            if lenght[next_vertex] is None:
                lenght[next_vertex] = lenght[vertex] + 1
                queue.append(next_vertex)

    return lenght


def main():
    graph = get_input()

    length = owg(graph, 0)
    for vertex in range(len(graph)):
        print(length[vertex])


main()
