#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import deque


def get_input():
    start = input()
    end = input()
    return start, end


def gen_graph_doska(top, bot):
    graph = {top[i]+bot[j]:set() for j in range(8) for i in range(8)}

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

    return graph

def get_path(start, end, graph):
    parent = owg(graph, start, end)
    if parent is None:
        return None
    path = []
    pre_vertex = end
    while pre_vertex is not None:
        path.append(pre_vertex)
        pre_vertex = parent[pre_vertex]
    return path[::-1]


def owg(graph, start, end):
    parent = {v: None for v in graph}
    lenght = {v: None for v in graph}
    queue = deque([start])
    lenght[start] = 0
    while queue:
        vertex = queue.popleft()
        for next_vertex in graph[vertex]:
            if lenght[next_vertex] is None:
                lenght[next_vertex] = lenght[vertex] + 1
                parent[next_vertex] = vertex
                queue.append(next_vertex)
            if next_vertex == end:
                return parent
    return None


def main():
    top = 'abcdefgh'
    bot = '12345678'
    start, end = get_input()
    graph = gen_graph_doska(top, bot)
    ans = get_path(start, end, graph)
    for line in ans:
        print(line)


main()
