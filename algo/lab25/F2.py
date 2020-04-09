#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Версия решения через формулу
# Не проходит по времени
from collections import deque


def get_input():
    n, m = [int(line) for line in input().split()]

    all_start = []
    for k in range(n):
        line = input().split()
        for i in range(m):
            if line[i] == '1':
                all_start.append((k, i))

    return all_start, n, m


def main():
    all_start, n, m = get_input()

    for i in range(n):
        line = [None] * m
        for j in range(m):
            minimum = None
            for point in all_start:
                if j == point[1] and i == point[0]:
                    minimum = 0
                    break
                l = abs(j-point[1]) + abs(i-point[0])
                minimum = minimum or l
                if minimum > l:
                    minimum = l
            line[j] = str(minimum)
        print(' '.join(line))


main()
