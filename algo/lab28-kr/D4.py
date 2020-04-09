#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
9 10
0 0 0 0 0 0 0 0 0 0
1 1 1 0 1 1 1 1 1 0
0 0 0 0 0 0 0 0 1 0
0 1 1 1 1 1 1 0 1 0
0 1 0 0 0 2 1 0 1 0
0 1 0 1 1 1 1 0 1 0
0 1 0 0 0 0 0 0 1 0
0 1 1 1 1 1 1 1 1 0
0 0 0 0 0 0 0 0 0 0

9 10
0 0 0 0 0 0 0 0 0 0
1 1 1 1 1 1 1 1 1 0
0 0 0 0 0 0 2 0 1 0
1 1 1 1 1 1 1 1 1 0
0 2 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
0 0 0 0 0 0 0 0 0 0
1 0 0 0 0 0 0 0 0 0


3 3
0 2 0
2 0 0
0 0 1
"""


from collections import deque
# 0 - stop 1 - left 2 - up 3 - right 4 -down

def get_input():
    pass


def owg():
    pass


def main():
    n, m = [int(line) for line in input().split()]

    a = [[1] * (1 + m + 1) for _ in range(1 + n + 1)]
    for i in range(1, n+1):
        j = 1
        for ch in input():
            if ch == ' ':
                continue
            else:
                a[i][j] = int(ch)
                j += 1

    INF = n * m * 2
    l = [[INF] * (1 + m + 1) for _ in range(1 + n + 1)]
    l[1][1] = 0
    q = deque([(1, 1)])

    while q:
        cur = q.popleft()
        if a[cur[0]][cur[1]] == 2:
            print(l[cur[0]][cur[1]])
            exit(0)
        for di in range(-1, 2):
            for dj in range(-1, 2):
                if di * di + dj * dj == 1:
                    ni = cur[0]
                    nj = cur[1]
                    while True:
                        if a[ni][nj] == 2:
                            break
                        if a[ni+di][nj+dj] == 1:
                            break
                        ni += di
                        nj += dj
                    if l[ni][nj] > l[cur[0]][cur[1]] + 1:
                        l[ni][nj] = l[cur[0]][cur[1]] + 1
                        q.append((ni, nj))

    return -1


main()
