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
    return or_graph


def check_circle(or_graph):
    used = set()
    for vertex in or_graph:
        if vertex not in used:
            stack = []
            dfs(vertex, or_graph, used, stack)


def dfs(vertex, or_graph, used, stack):
    used.add(vertex)
    stack.append(vertex)
    for next_vertex in or_graph[vertex]:
        if next_vertex not in used:
            dfs(next_vertex, or_graph, used, stack)
        elif next_vertex in stack:
            print(' '.join(stack))
            exit(0)
    stack.pop()
    return True


def main():
    or_graph = get_input()
    #print(or_graph)
    #n = 8
    #or_graph = {'7': {'3'}, '3': {'1'}, '1': {'6', '2'}, '5': {'2'}, '2': set(), '6': {'7', '4'}, '4': {'7'}}
    #or_graph = {'0': {'10', '8', '7'}, '7': {'10', '4', '2'}, '10': {'9', '2'}, '2': set(), '4': {'11', '8'}, '11': {'0'}, '3': {'4', '5'}, '5': set(), '8': {'11'}, '6': {'11', '1', '5', '8'}, '9': {'8', '2'}, '1': set()}

    check_circle(or_graph)



main()
