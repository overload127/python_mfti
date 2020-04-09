#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
9 10
0 0 0 0 0 0 0 0 0 0
1 1 1 0 1 1 1 1 1 0
0 0 0 0 0 0 0 0 1 0
0 1 1 1 1 1 1 0 1 0
0 1 0 0 0 2 1 0 1 0
0 1 0 1 1 1 1 0 1 0
0 1 0 0 0 0 0 0 1 0
0 1 1 1 1 1 1 1 1 0
0 0 0 0 0 0 0 0 0 0

9 10
0 0 0 0 2 0 0 0 0 1
0 1 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 1 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 1 0 0 0 0 0 0
0 0 0 0 0 0 1 0 0 0
1 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 1 0

9 10
0 0 0 0 2 0 0 0 0 1
1 0 0 0 0 0 0 0 0 0
0 0 0 1 0 1 0 0 0 0
1 1 0 0 0 0 0 0 0 0
0 0 0 0 0 0 1 0 0 0
0 0 0 1 0 0 0 0 0 0
0 0 0 0 0 0 0 1 0 0
0 0 1 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0

3 3
0 2 0
2 0 0
0 0 1
"""
from collections import deque


def get_input():
    n, m = [int(line) for line in input().split()]

    graph = {i: {'left': None, 'right': None, 'up': None, 'down': None} for i in range(n*m)}
    end = set()
    old_line = []
    for i in range(n):
        line = [line for line in input().split()]
        for j in range(m):
            if line[j] != '1':
                cur_point = i*m+j
                if 0 <= j - 1 < m and line[j-1] != '1':
                    back_point1 = i*m+j-1
                    graph[cur_point]['left'] = back_point1
                    graph[back_point1]['right'] = cur_point
                if 0 <= i - 1 < n and old_line[j] != '1':
                    back_point2 = (i-1)*m+j
                    graph[cur_point]['up'] = back_point2
                    graph[back_point2]['down'] = cur_point
                if line[j] == '2':
                    end.add(cur_point)
        old_line = line

    return graph, end


def owg(graph, start, end):
    queue = deque([start])
    INF = 1000 * 1000 * 1000
    lenght = [INF] * len(graph)
    lenght[start] = 0
    while queue:
        vertex = queue.popleft()
        if vertex in end:
            return lenght[vertex]
        for direct, next_vertex in graph[vertex].items():
            next_vertex_old = vertex
            while next_vertex is not None:
                next_vertex_old = next_vertex
                next_vertex = graph[next_vertex_old][direct]
            if lenght[next_vertex_old] > lenght[vertex] + 1:
                lenght[next_vertex_old] = lenght[vertex] + 1
                queue.append(next_vertex_old)

    return -1


def main():
    graph, end = get_input()

    ans = owg(graph, 0, end)

    print(ans)


main()
