#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def get_input():
    n = int(input())

    graf_matrix = []
    for i in range(n):
        graf_matrix.append([int(line) for line in input().split()])
    return n, graf_matrix


def count_rebr(n, graf_matrix):
    for i in range(n):
        if graf_matrix[i][i] == 1:
            return "NO"
        for j in range(i+1,n):
            if graf_matrix[i][j] != graf_matrix[j][i]:
                return "NO"

    return "YES"

def main():
    n, graf_matrix = get_input()
    # print(graf_matrix)
    # n = 5
    # graf_matrix = [[0, 1, 0, 0, 0], [1, 0, 1, 0, 0], [0, 1, 0, 0, 1], [0, 0, 0, 0, 0], [0, 0, 1, 0, 0]]

    ans = count_rebr(n, graf_matrix)
    print(ans)


if __name__ == "__main__":
    main()
