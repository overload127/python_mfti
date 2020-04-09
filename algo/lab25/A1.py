#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import deque


def get_input():
    line = input().split()
    n = int(line[0])
    m = int(line[1])
    start = line[2]
    end = line[3]

    graph = {str(i): set() for i in range(n)}
    for _ in range(m):
        i, j = [line for line in input().split()]
        graph[i].add(j)
        graph[j].add(i)
    return start, end, graph


def owg(graph, start, end):
    queue = deque([start])
    lenght = {v: None for v in graph}
    lenght[start] = 0
    while queue:
        vertex = queue.popleft()
        for next_vertex in graph[vertex]:
            if lenght[next_vertex] is None:
                lenght[next_vertex] = lenght[vertex] + 1
                queue.append(next_vertex)
            if end == next_vertex:
                return lenght[next_vertex]

    return None


def main():
    start, end, graph = get_input()

    ans = owg(graph, start, end)
    print(ans)


main()
