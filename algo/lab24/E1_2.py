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


#def check_circle(or_graph):
    used = set()
    for vertex in or_graph:
        if vertex not in used:
            stack = []
            res = dfs(vertex, or_graph, used, stack)
            if not res:
                return ' '.join(stack)

    return 'YES'


#def dfs(vertex, or_graph, used, stack):
    used.add(vertex)
    stack.append(vertex)
    for next_vertex in or_graph[vertex]:
        if next_vertex not in used:
            res = dfs(next_vertex, or_graph, used, stack)
            if not res:
                return False
        elif next_vertex in stack:
            return False
    stack.pop()
    return True


def check_circle(or_graph):
    back_or_graph = get_back_or_graph(or_graph)
    stack = get_stack_from_graph(back_or_graph)

    return get_circle_from_graph(or_graph, stack)


def get_back_or_graph(or_graph):
    back_or_graph = {}
    for vertex in or_graph:
        for next_vertex in or_graph[vertex]:
            if next_vertex not in back_or_graph:
                back_or_graph[next_vertex] = set()
            if vertex not in back_or_graph:
                back_or_graph[vertex] = set()
            back_or_graph[next_vertex].add(vertex)

    return back_or_graph


def get_stack_from_graph(or_graph):
    stack = []
    used = set()
    for vertex in or_graph:
        if vertex not in used:
            dfs1(vertex, or_graph, used, stack)

    return stack


def dfs1(vertex, or_graph, used, stack):
    used.add(vertex)
    for next_vertex in or_graph[vertex]:
        if next_vertex not in used:
            dfs1(next_vertex, or_graph, used, stack)

    stack.append(vertex)


def get_circle_from_graph(or_graph, stack):
    used = set()
    while len(stack):
        vertex = stack.pop()
        if vertex not in used:
            circle = []
            dfs2(vertex, or_graph, used, circle)

    return circle or "YES"


def dfs2(vertex, or_graph, used, circle):
    used.add(vertex)
    circle.append(vertex)
    for next_vertex in or_graph[vertex]:
        if next_vertex not in used:
            if dfs2(next_vertex, or_graph, used, circle):
                return True
        elif next_vertex in circle:
            return True

    circle.pop()
    return False


def main():
    or_graph = get_input()
    #print(or_graph)
    #n = 8
    #or_graph = {'7': {'3'}, '3': {'1'}, '1': {'6', '2'}, '5': {'2'}, '2': set(), '6': {'7', '4'}, '4': {'7'}}
    #or_graph = {'0': {'10', '8', '7'}, '7': {'10', '4', '2'}, '10': {'9', '2'}, '2': set(), '4': {'11', '8'}, '11': {'0'}, '3': {'4', '5'}, '5': set(), '8': {'11'}, '6': {'11', '1', '5', '8'}, '9': {'8', '2'}, '1': set()}

    ans = check_circle(or_graph)
    print(ans)



main()
