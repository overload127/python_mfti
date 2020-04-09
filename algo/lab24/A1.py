#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def get_input():
    n = int(input())

    graf_matrix = []
    for i in range(n):
        graf_matrix.append([int(line) for line in input().split()])
    return n, graf_matrix


def count_rebr(n, graf_matrix):
    count = 0
    for i in range(n):
        for j in range(i,n):
            count += graf_matrix[i][j]

    return count

def main():
    n, graf_matrix = get_input()
    # print(graf_matrix)
    # n = 5
    # graf_matrix = [[0, 1, 0, 0, 0], [1, 0, 1, 0, 0], [0, 1, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]

    count = count_rebr(n, graf_matrix)
    print(count)


if __name__ == "__main__":
    main()
