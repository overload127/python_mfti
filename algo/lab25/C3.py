#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
9 10
5 4
7 8
XXXXXXXXXX
X        X
X XXXXXX X
X X    X X
X X XX X X
X X  X X X
X XXXX X X
X      X X
XXXXXXXXXX
============================
4 4
1 1
2 2
XXXX
X  X
X  X
XXXX
============================
4 4
0 0
3 3
    
 XX 
 XX 
    
============================
"""

from collections import deque


def get_input():
    n, m = [int(line) for line in input().split()]

    y1, x1 = [int(line) for line in input().split()]
    start = y1 * m + x1
    y2, x2 = [int(line) for line in input().split()]
    end = y2 * m + x2

    #graph = {i*m+j:set() for j in range(m) for i in range(n)}
    graph = {i: set() for i in range(n*m)}
    old_ch = 'X' * m
    for k in range(n):
        line = input()
        #line = "X" * m
        for i in range(m):
            if line[i] == ' ':
                if 0 <= i - 1 <= m - 1 and line[i-1] == ' ':
                    graph[k*m+i].add(k*m+i-1)
                    graph[k*m+i-1].add(k*m+i)
                if 0 <= k - 1 <= n - 1 and old_ch[i] == ' ':
                    graph[k*m+i].add((k-1)*m+i)
                    graph[(k-1)*m+i].add(k*m+i)

        old_ch = line

    if x1 == x2 and y1 == y2:
        print("0")
        exit(0)
        # из-за этого 7я задача решается верно

    if n == 0 or m == 0:
        print("INF")
        exit(0)

    if y1 >= n or 0 > y1 or x1 >= m or 0 > x1:
        print("INF")
        exit(0)

    if y2 >= n or 0 > y2 or x2 >= m or 0 > x2:
        print("INF")
        exit(0)

    if (start < 0 or start >= len(graph) or
       end < 0 or end >= len(graph)):
        print("INF")
        exit(0)

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

    return lenght


def main():
    graph, start, end = get_input()

    ans = owg(graph, start, end)
    if ans[end]:
        print(ans[end])
    else:
        print("INF")


main()
