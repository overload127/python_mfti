#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import deque
CHILDREN, LENGTH, PARENT = 0, 1, 2


def get_input():
    n, m = [int(line) for line in input().split()]

    or_graph = {i: set() for i in range(n)}
    for _ in range(m):
        i, j = [int(line) for line in input().split()]

        or_graph[i].add(j)
    return or_graph, n


def get_small_circle(graph, n):
    small = None
    small_path = None
    for vertex in graph:
        path = owg(vertex, graph, n)
        if path is None:
            continue
        small = small or len(path)
        if small >= len(path):
            small_path = path
            small = len(path)

    return small_path


def owg(start, graph, n):
    # lenght = {v: None for v in graph}
    # parent = {v: None for v in graph}
    length = [None] * n
    parent = [None] * n
    queue = deque([start])
    length[start] = 0
    while queue:
        vertex = queue.popleft()
        for next_vertex in graph[vertex]:
            if length[next_vertex] is None:
                length[next_vertex] = length[vertex] + 1
                parent[next_vertex] = vertex
                queue.append(next_vertex)
            elif next_vertex == start:
                return get_path_circle(start, vertex, next_vertex, parent)
    return None


def get_path_circle(start, first, second, parent):
    path = []
    pre_vertex = first
    while pre_vertex is not None:
        path.append(pre_vertex)
        pre_vertex = parent[pre_vertex]
    path = path[::-1]

    pre_vertex = second
    while parent[pre_vertex] is not None:
        path.append(pre_vertex)
        pre_vertex = parent[pre_vertex]

    return path


def main():
    or_graph, n = get_input()

    path = get_small_circle(or_graph, n)
    if path is None:
        print("NO CYCLES")
    else:
        print(' '.join(map(str, path)))


main()
