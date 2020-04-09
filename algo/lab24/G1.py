#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def get_input():
    n, m = [int(line) for line in input().split()]

    or_graph = {str(i): [set(), 'white', None] for i in range(n)}
    for _ in range(m):
        i, j = [line for line in input().split()]

        or_graph[i][0].add(j)
    return or_graph


def get_steck_sort(or_graph):
    stack = []
    for vertex in or_graph:
        if or_graph[vertex][1] == 'white':
            dfs1(vertex, or_graph, stack)

    return stack


def dfs1(vertex, or_graph, stack):
    or_graph[vertex][1] = 'gray'
    for next_vertex in or_graph[vertex][0]:
        if or_graph[next_vertex][1] == 'white':
            dfs1(next_vertex, or_graph, stack)
        elif or_graph[next_vertex][1] == 'gray':
            print("NO")
            exit(0)

    or_graph[vertex][1] = 'black'
    stack.append(vertex)


def get_group(or_graph, stack):
    stack_out = []
    while len(stack):
        vertex = stack.pop()
        if or_graph[vertex][1] == 'white':
            dfs2(vertex, or_graph, stack_out, True)

    return stack_out[::-1]


def dfs2(vertex, or_graph, stack_out, group):
    or_graph[vertex][1] = 'gray'
    or_graph[vertex][2] = group
    for next_vertex in or_graph[vertex][0]:
        if or_graph[next_vertex][1] == 'white':
            dfs2(next_vertex, or_graph, stack_out, not group)
        elif or_graph[next_vertex][2] == group:
            print("NO")
            exit(0)

    or_graph[vertex][1] = 'black'
    if group:
        stack_out.append(vertex)


def main():
    or_graph = get_input()
    #print(or_graph)
    #n = 8
    #or_graph = {'7': {'3'}, '3': {'1'}, '1': {'6', '2'}, '5': {'2'}, '2': set(), '6': {'7', '4'}, '4': {'7'}}
    #or_graph = {'0': {'10', '8', '7'}, '7': {'10', '4', '2'}, '10': {'9', '2'}, '2': set(), '4': {'11', '8'}, '11': {'0'}, '3': {'4', '5'}, '5': set(), '8': {'11'}, '6': {'11', '1', '5', '8'}, '9': {'8', '2'}, '1': set()}

    stack = get_steck_sort(or_graph)
    for vertex in or_graph:
        or_graph[vertex][1] = 'white'
    ans = get_group(or_graph, stack)
    print(' '.join(ans))


main()
