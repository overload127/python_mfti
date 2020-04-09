#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def get_input():
    n, m = [int(line) for line in input().split()]

    or_graph = {}
    for _ in range(m):
        i, j = [line for line in input().split()]

        if or_graph.get(i, None) is None:
            or_graph[i] = set()
        if or_graph.get(j, None) is None:
            or_graph[j] = set()
        or_graph[i].add(j)
        or_graph[j].add(i)
    return n, or_graph


def check_pol_graph(n, or_graph):
    for vertex in or_graph:
        if len(or_graph[vertex]) > n:
            return "NO"
        elif len(or_graph[vertex]) < n - 1:
            return "NO"
        elif len(or_graph[vertex]) == n - 1:
            for ch in or_graph[vertex]:
                if ch == vertex:
                    return "NO"

    return "YES"

def main():
    n, or_graph = get_input()
    # print(n)
    # print(m)
    # print(or_graph)
    # n = 5
    # or_graph = {'0': {'1', '2', '3', '4'}, '1': {'0', '2', '4'}, '2': {'0', '1', '3'}, '4': {'0', '1', '2', '3'}, '3': {'0', '4', '2'}}

    ans = check_pol_graph(n, or_graph)
    print(ans)


if __name__ == "__main__":
    main()
