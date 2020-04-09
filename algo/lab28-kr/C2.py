#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def get_input():
    n = int(input())

    istock = [1] * (n+1)
    stock = [1] * (n+1)
    if n != 0:
        for i in range(1, n+1):
            for j, ch in enumerate(input().split(), start=1):
                if ch != '0':
                    stock[i] -= 1
                    istock[j] -= 1

    return istock, stock, n


def main():
    istock, stock, n = get_input()

    for i in range(1, n+1):
        if istock[i] == 1:
            print(i, end=' ')
    print()

    for i in range(1, n+1):
        if stock[i] == 1:
            print(i, end=' ')


main()
