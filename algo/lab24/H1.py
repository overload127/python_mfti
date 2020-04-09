#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def get_input():
    n, m = [int(line) for line in input().split()]

    or_graph = {str(i): set() for i in range(n)}
    for _ in range(m):
        i, j = [line for line in input().split()]

        or_graph[i].add(j)
        or_graph[j].add(i)
    return or_graph


def get_gam_cicle(or_graph):
    for vertex in or_graph:
        stack = []
        dfs1(vertex, or_graph, stack, vertex)

    print("NO")


def dfs1(vertex, or_graph, stack, first):
    stack.append(vertex)
    for next_vertex in or_graph[vertex]:
        if next_vertex not in stack:
            dfs1(next_vertex, or_graph, stack, first)
        elif next_vertex == first:
            if len(stack) == len(or_graph):
                print(' '.join(stack))
                exit(0)

    stack.pop()


def main():
    or_graph = get_input()
    #print(or_graph)
    #n = 5
    #or_graph = {'0': {'1', '4'}, '1': {'0', '3', '2'}, '2': {'3', '1', '4'}, '3': {'2', '1'}, '4': {'2', '0'}}
    #or_graph = {'0': {'10', '8', '7'}, '7': {'10', '4', '2'}, '10': {'9', '2'}, '2': set(), '4': {'11', '8'}, '11': {'0'}, '3': {'4', '5'}, '5': set(), '8': {'11'}, '6': {'11', '1', '5', '8'}, '9': {'8', '2'}, '1': set()}

    get_gam_cicle(or_graph)
    # print(' '.join(ans))


main()
