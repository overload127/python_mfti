#!/usr/bin/env python3
# -*- coding: utf-8 -*-7


def get_input():
    n, m = [int(line) for line in input().split()]

    or_graph = {i: set() for i in range(1, n+1)}

    bad = False
    for _ in range(m):
        a, b = [int(line) for line in input().split()]
        or_graph[a].add(b)

    return or_graph, n


def get_circle(or_graph, n):
    for vertex in or_graph:
        used = set()
        if dfs(vertex, or_graph, used, vertex):
            return "No"

    return "Yes"


def dfs(vertex, or_graph, used, start):
    used.add(vertex)
    for next_vertex in or_graph[vertex]:
        if next_vertex == start:
            return True
        elif next_vertex not in used:
            if dfs(next_vertex, or_graph, used, start):
                return True

    return False


def main():

    or_graph, n = get_input()

    ans = get_circle(or_graph, n)

    print(ans)


main()
