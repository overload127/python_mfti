#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
9 14
a b 2
a h 15
b c 1
b d 5
c g 1
c f 2
c d 3
d f 4
d e 6
g f 1
f h 3
f e 7
h i 12
e i 2
a
"""
from collections import deque


def get_input():
    n, m = [int(line) for line in input().split()]

    graph = {}
    for _ in range(m):
        a, b, price = [line for line in input().split()]
        price = float(price)
        add_vertex(graph, a, b, price)
        add_vertex(graph, b, a, price)

    start = input()

    return graph, start


def add_vertex(graph, a, b, price):
    if a not in graph:
        graph[a] = {b: price}
    else:
        graph[a][b] = price


def get_price_to_all_vertex(graph, start):
    queue = deque([start])
    price_all = {v: None for v in graph}
    price_all[start] = 0
    while queue:
        vertex = queue.popleft()
        for next_vertex in graph[vertex]:
            if price_all[next_vertex] is None or price_all[vertex] + graph[vertex][next_vertex] < price_all[next_vertex]:
                price_all[next_vertex] = price_all[vertex] + graph[vertex][next_vertex]
                queue.append(next_vertex)

    return price_all


def main():
    graph, start = get_input()

    shortest_price = get_price_to_all_vertex(graph, start)

    print('{:10} = {:10}'.format('vertex', 'price'))
    for vertex in shortest_price:
        print('{:10} = {:10}'.format(vertex, shortest_price[vertex]))


main()
