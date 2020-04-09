#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def get_input():
    n, m = [int(line) for line in input().split()]

    graph = {str(i): [set(), 'white', None] for i in range(n)}
    for _ in range(m):
        i, j = [line for line in input().split()]

        graph[i][0].add(j)
        graph[j][0].add(i)
    return graph


def get_group(graph):
    stack_out = []
    for vertex in graph:
        if graph[vertex][1] == 'white':
            dfs2(vertex, graph, stack_out, True)

    return stack_out[::-1]


def dfs2(vertex, graph, stack_out, group):
    graph[vertex][1] = 'gray'
    graph[vertex][2] = group
    for next_vertex in graph[vertex][0]:
        if graph[next_vertex][1] == 'white':
            dfs2(next_vertex, graph, stack_out, not group)
        elif graph[next_vertex][2] == group:
            print("NO")
            exit(0)

    graph[vertex][1] = 'black'
    if group:
        stack_out.append(vertex)


def main():
    graph = get_input()
    #print(graph)
    #n = 8
    #graph = {'7': {'3'}, '3': {'1'}, '1': {'6', '2'}, '5': {'2'}, '2': set(), '6': {'7', '4'}, '4': {'7'}}
    #graph = {'0': {'10', '8', '7'}, '7': {'10', '4', '2'}, '10': {'9', '2'}, '2': set(), '4': {'11', '8'}, '11': {'0'}, '3': {'4', '5'}, '5': set(), '8': {'11'}, '6': {'11', '1', '5', '8'}, '9': {'8', '2'}, '1': set()}

    ans = get_group(graph)
    print(' '.join(ans))


main()
