#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math


def dot_product(N, vector1, vector2):
    if N == 2:
        res = vector1[0]*vector2[0] + vector1[1]*vector2[1]
    elif N == 3:
        res = vector1[0]*vector2[0] + vector1[1]*vector2[1] + vector1[2]*vector2[2]
    else:
        res = 0
    return res

if __name__ == "__main__":
    print(dot_product(3, [1, 2, 3], [1, 2, 3]))
    print(dot_product(3, [1, 2, 3], [4, 5, 6]))
