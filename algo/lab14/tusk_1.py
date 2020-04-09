#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import my_stack


if __name__ == "__main__":
    my_stack.clear()
    for i in range(1, 11):
        my_stack.push(i)

    while not(my_stack.is_empty()):
        x = my_stack.pop()
        print(x)
