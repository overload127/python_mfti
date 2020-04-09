#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def get_input():
    n, m = [int(line) for line in input().split()]

    graph = [[0]*n for _ in range(n)]
    if n != 0:
        for _ in range(m):
            i, j = [int(line) for line in input().split()]

            graph[i][j] += 1
            graph[j][i] += 1

    return graph, n


def main():
    graph, n = get_input()

    if n == 0:
        print("YES")
    else:
        count = sum(graph[-1])
        for i in range(n):
            if count != sum(graph[i]):
                print("NO")
                exit(0)
        print("YES")


main()
