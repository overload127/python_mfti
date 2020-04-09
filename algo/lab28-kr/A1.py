#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from collections import deque


def get_input():
    start = input()[::-2]
    return start


def gen_graph_doska(top, bot):
    or_graph = {top[i]+bot[j]: set() for j in range(8) for i in range(8)}

    for i in range(7, -1, -1):
        for j in range(8):
            point = top[i]+bot[j]

            if 0 <= i+1 <= 7 and 0 <= j-1 <= 7:
                v = top[i+1]+bot[j-1]
                or_graph[point].add(v)
            if 0 <= i+1 <= 7 and 0 <= j+1 <= 7:
                v = top[i+1]+bot[j+1]
                or_graph[point].add(v)

    return or_graph


def owg_get_cont_path(or_graph, start):
    count_path = {v: 0 for v in or_graph}
    queue = deque([start])
    count_path[start] = 1
    while queue:
        vertex = queue.popleft()
        for next_vertex in or_graph[vertex]:
            if count_path[next_vertex] == 0:
                queue.append(next_vertex)
            count_path[next_vertex] += count_path[vertex]

    return count_path


def main():
    top = '12345678'
    bot = '12345678'

    start = get_input()

    or_graph = gen_graph_doska(top, bot)
    count_path = owg_get_cont_path(or_graph, start)

    ans = 0
    for j in range(8):
        ans += count_path[top[-1]+bot[j]]
    print(ans)


main()
