#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def get_input():
    n = int(input())

    istock = set(list(range(1, n+1)))
    stock = set()
    if n != 0:
        for i in range(1, n+1):
            flag = True
            for j, ch in enumerate(input().split(), start=1):
                if ch != '0':
                    flag = False
                    istock -= set([j])
            if flag:
                stock.add(i)

    return istock, stock


def main():
    istock, stock = get_input()

    if istock:
        for ch in istock:
            print(ch, end=' ')
        print()
    if stock:
        for ch in stock:
            print(ch, end=' ')


main()
