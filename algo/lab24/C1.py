#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def get_input():
    n = int(input())

    graf_matrix = []
    for i in range(n):
        graf_matrix.append([int(line) for line in input().split()])

    _ = input()

    color = [int(line) for line in input().split()]
    return n, graf_matrix, color


def count_bad_bridge(n, graf_matrix, color):
    count = 0
    for i in range(n):
        for j in range(i+1,n):
            if graf_matrix[i][j] and color[i] != color[j]:
                count += 1

    return count

def main():
    n, graf_matrix, color = get_input()
    # print(n)
    # print(graf_matrix)
    # print(color)
    # n = 7
    # graf_matrix = [[0, 1, 0, 0, 0, 1, 1], [1, 0, 1, 0, 0, 0, 0], [0, 1, 0, 0, 1, 1, 0], [0, 0, 0, 0, 0, 0, 0], [0, 0, 1, 0, 0, 1, 0], [1, 0, 1, 0, 1, 0, 0], [1, 0, 0, 0, 0, 0, 0]]
    # color = [1, 1, 1, 1, 1, 3, 3]

    count = count_bad_bridge(n, graf_matrix, color)
    print(count)


if __name__ == "__main__":
    main()
