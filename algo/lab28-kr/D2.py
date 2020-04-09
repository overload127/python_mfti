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
0 0 0 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1 1 0
0 0 0 0 0 0 2 0 1 0
1 1 1 1 1 1 1 1 1 0
0 2 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
1 0 0 0 0 0 0 0 0 0


3 3
0 2 0
2 0 0
0 0 1
"""
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
    used = set()
    stack_vertex = {(start, 0)}
    lenght = [None] * len(graph)
    lenght[start] = 0
    while stack_vertex:
        vertex, p = min(stack_vertex, key=lambda e: e[1])
        stack_vertex -= {(vertex, p)}
        used |= {vertex}
        if vertex in end:
            return p
        for direct, next_vertex in graph[vertex].items():
            if next_vertex is not None:
                while next_vertex is not None:
                    next_vertex_old = next_vertex
                    next_vertex = graph[next_vertex_old][direct]
                    if next_vertex_old not in used:
                        if next_vertex is None:
                            if lenght[next_vertex_old] is None or lenght[next_vertex_old] > lenght[vertex] + 1:
                                stack_vertex -= {(next_vertex_old, lenght[next_vertex_old])}
                                lenght[next_vertex_old] = lenght[vertex] + 1
                                stack_vertex |= {(next_vertex_old, lenght[next_vertex_old])}
                        elif lenght[next_vertex_old] is None or lenght[next_vertex_old] > lenght[vertex] + 2:
                            stack_vertex -= {(next_vertex_old, lenght[next_vertex_old])}
                            lenght[next_vertex_old] = lenght[vertex] + 2
                            stack_vertex |= {(next_vertex_old, lenght[next_vertex_old])}

    return -1


def main():
    graph, end = get_input()

    ans = owg(graph, 0, end)

    print(ans)


main()
