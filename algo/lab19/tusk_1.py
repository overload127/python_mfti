#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Vector:

    def __init__(self, x = 0, y = 0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, other):
        return Vector(self.x * i, self.y * i)

    def __rmul__(self, i):
        return Vector(self.x * i, self.y * i)

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __str__(self):
        return '{} {}'.format(self.x, self.y)
