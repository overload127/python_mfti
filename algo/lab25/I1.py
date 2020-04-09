#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import deque


def get_input():
    start, end = input().split()
    return start, end


def gen_graph_doska(top, bot):
    graph = {top[i]+bot[j]: set() for j in range(8) for i in range(8)}

    for i in range(8):
        for j in range(8):
            point = top[i]+bot[j]

            if 0 <= i-2 <= 7 and 0 <= j-1 <= 7:
                v = top[i-2]+bot[j-1]
                graph[point].add(v)
                graph[v].add(point)
            if 0 <= i-1 <= 7 and 0 <= j-2 <= 7:
                v = top[i-1]+bot[j-2]
                graph[point].add(v)
                graph[v].add(point)
            if 0 <= i+1 <= 7 and 0 <= j-2 <= 7:
                v = top[i+1]+bot[j-2]
                graph[point].add(v)
                graph[v].add(point)
            if 0 <= i+2 <= 7 and 0 <= j-1 <= 7:
                v = top[i+2]+bot[j-1]
                graph[point].add(v)
                graph[v].add(point)

    return get_even_graph(graph)


def get_even_graph(graph):
    start = 'a1'
    queue = deque([start])
    even_graph = dict()
    while queue:
        vertex = queue.popleft()
        even_graph[(vertex, 0)] = set()
        even_graph[(vertex, 1)] = set()
        for next_vertex in graph[vertex]:
            if (next_vertex, 0) not in even_graph:
                queue.append(next_vertex)
            even_graph[(vertex, 0)].add((next_vertex, 1))
            even_graph[(vertex, 1)].add((next_vertex, 0))

    return even_graph


def owg(graph, start, end):
    lenght = {v: None for v in graph}
    queue = deque([(start, 0)])
    lenght[(start, 0)] = 0
    while queue:
        vertex = queue.popleft()
        for next_vertex in graph[vertex]:
            if lenght[next_vertex] is None:
                lenght[next_vertex] = lenght[vertex] + 1
                queue.append(next_vertex)
            if next_vertex == (end, 0):
                return lenght[next_vertex] // 2
    return -1


def main():
    top = 'abcdefgh'
    bot = '12345678'
    start, end = get_input()
    graph = gen_graph_doska(top, bot)
    ans = owg(graph, start, end)
    print(ans)


main()
