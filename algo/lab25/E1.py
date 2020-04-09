#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import deque


def get_input():
    n, m = [int(line) for line in input().split()]

    graph = {str(i): set() for i in range(n)}
    for _ in range(m):
        i, j = [line for line in input().split()]

        graph[i].add(j)
        graph[j].add(i)
    return graph


def owg(graph, start):
    ost_graph_reb = []
    queue = deque([start])
    lenght = {v: None for v in graph}
    lenght[start] = 0
    while queue:
        vertex = queue.popleft()
        for next_vertex in graph[vertex]:
            if lenght[next_vertex] is None:
                lenght[next_vertex] = lenght[vertex] + 1
                queue.append(next_vertex)
                ost_graph_reb.append(' '.join((str(vertex), str(next_vertex))))

    return ost_graph_reb


def main():
    graph = get_input()
    # print(graph)
    #graph = {'0': {'12', '10', '1', '11'}, '1': {'0', '7'}, '2': {'6'}, '3': {'11'}, '4': {'10', '6'}, '5': {'13', '8'}, '6': {'4', '10', '2'}, '7': {'13', '1'}, '8': {'12', '5'}, '9': {'11'}, '10': {'0', '4', '6'}, '11': {'12', '14', '3', '0', '9'}, '12': {'0', '8', '11'}, '13': {'5', '7'}, '14': {'11'}}

    ost_graph_reb = owg(graph, '0')
    for line in ost_graph_reb:
        print(line)


main()
