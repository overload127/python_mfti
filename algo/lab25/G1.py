#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# 
from collections import deque


def get_input():
    # start = [map(int, *input())]
    # end = [map(int, *input())]
    start = []
    end = []
    for ch in input():
        start.append(int(ch))
    for ch in input():
        end.append(int(ch))
    # start = list(map(int, [*input()]))
    # end = list(map(int, [*input()]))

    return start, end


def gen_graph():
    graph = dict()

    return graph


def owg(start, end):
    queue = deque([start])
    # length = dict()
    # length[start] = 0
    path = dict()
    path[get_num(start)] = None
    # length = {v: None for v in graph}
    # length = [None] * l
    while queue:
        vertex = queue.popleft()
        if vertex == end:
            # Здесь нужна функция возврата пути
            return path
        number = get_num(vertex)
        if (vertex[3] - 1) != 0:
            next_vertex = vertex.copy()
            next_vertex[3] -= 1
            next_number = get_num(next_vertex)
            if path.get(next_number, None) is None:
                path[next_number] = number
                queue.append(next_vertex)

        if (vertex[0] + 1) != 10:
            next_vertex = vertex.copy()
            next_vertex[0] += 1
            next_number = get_num(next_vertex)
            if path.get(next_number, None) is None:
                path[next_number] = number
                queue.append(next_vertex)

        next_vertex = [vertex[3], vertex[0], vertex[1], vertex[2]]
        next_number = get_num(next_vertex)
        if path.get(next_number, None) is None:
            path[next_number] = number
            queue.append(next_vertex)

        next_vertex = [vertex[1], vertex[2], vertex[3], vertex[0]]
        next_number = get_num(next_vertex)
        if path.get(next_number, None) is None:
            path[next_number] = number
            queue.append(next_vertex)

    return None


def main():
    start, end = get_input()

    path = owg(start, end)

    if path is None:
        i = 0
        while True:
            i += 1
    else:
        start_num = get_num(start)
        end_num = get_num(end)
        all_path = []
        all_path.append(end_num)
        while end_num != start_num:
            end_num = path[end_num]
            all_path.append(end_num)

        for _ in range(len(all_path)):
            print(all_path.pop())

def get_num(vertex):
    return vertex[0]*1000+vertex[1]*100+vertex[2]*10+vertex[3]


main()