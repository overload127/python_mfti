#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import deque


def get_input():
    n, m = [int(line) for line in input().split()]

    graph = {str(i): set() for i in range(n)}
    if n != 0:
        for _ in range(m):
            i, j = [line for line in input().split()]

            graph[i].add(j)
            graph[j].add(i)

    return graph, n


def main():
    graph, n = get_input()

    if n == 0:
        print("YES")
    else:
        count = len(graph['0'])
        for vertex in graph:
            if count != len(graph[vertex]):
                print("NO")
                exit(0)
        print("YES")


main()
