#!/usr/bin/env python3
# -*- coding: utf-8 -*-


"""
>>> is_empty()
True
>>> push(1)
>>> push(2)
>>> push(3)
>>> is_empty()
False
>>> pop()
3
>>> pop()
2
>>> pop()
1
>>> is_empty()
True
>>> push(4)
>>> push(5)
>>> push(6)
>>> is_empty()
False
>>> clear()
>>> is_empty()
True
"""

_stack = []


def pop():
    return _stack.pop()


def push(x):
    _stack.append(x)


def is_empty():
    return len(_stack) == 0


def clear():
    _stack.clear()


def top():
    if is_empty():
        return None
    return _stack[-1]


if __name__ == "__main__":
    import doctest
    doctest.testmod()