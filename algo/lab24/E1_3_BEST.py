#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def get_input():
    n, m = [int(line) for line in input().split()]

    or_graph = {}
    for _ in range(m):
        i, j = [line for line in input().split()]

        if or_graph.get(i, None) is None:
            or_graph[i] = [set(), 'white']
        if or_graph.get(j, None) is None:
            or_graph[j] = [set(), 'white']
        or_graph[i][0].add(j)
    return n, or_graph


def check_circle(n, or_graph):
    for vertex in or_graph:
        if or_graph[vertex][1] == 'white':
            dfs(vertex, or_graph)

    return 'YES'


def dfs(vertex, or_graph):
    or_graph[vertex][1] = 'gray'
    for next_vertex in or_graph[vertex][0]:
        if or_graph[next_vertex][1] == 'white':
            dfs(next_vertex, or_graph)
        elif or_graph[next_vertex][1] == 'gray':
            vv = next_vertex
            while vv != vertex:
                print(vv, end=' ')
                for next_vv in or_graph[vv][0]:
                    if or_graph[next_vv][1] == 'gray':
                        vv = next_vv
                        break
            print(vv, end=' ')
            exit(0)

    or_graph[vertex][1] = 'black'
    return True


def main():
    n, or_graph = get_input()
    #print(or_graph)
    #n = 8
    #or_graph = {'7': {'3'}, '3': {'1'}, '1': {'6', '2'}, '5': {'2'}, '2': set(), '6': {'7', '4'}, '4': {'7'}}
    #or_graph = {'0': {'10', '8', '7'}, '7': {'10', '4', '2'}, '10': {'9', '2'}, '2': set(), '4': {'11', '8'}, '11': {'0'}, '3': {'4', '5'}, '5': set(), '8': {'11'}, '6': {'11', '1', '5', '8'}, '9': {'8', '2'}, '1': set()}

    ans = check_circle(n, or_graph)
    print(ans)



main()
