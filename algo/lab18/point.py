#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math


class Point:

    def __init__(self, x=0, y=0):
        """A 2D cartesian coordinate

        >>> point_1 = Point(1, 0)
        >>> point_1
        Point(1, 0)
        >>> point_2 = Point(10, 22)
        >>> point_2
        Point(10, 22)
        >>> point_3 = point_1 + point_2
        >>> point_3
        Point(11, 22)
        >>> point_2 += point_2
        >>> point_2
        Point(20, 44)
        >>> point_2 -= point_3
        >>> point_2
        Point(9, 22)
        """
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def distance_from_origin(self):
        """The distance of the point from the origin

        >>> point = Point(3, 4)
        >>> point.distance_from_origin
        5.0
        """
        return math.hypot(self.x, self.y)

    @property
    def get_tuple(self):
        """This property return coordinate in tuple

        >>> point = Point(3, 4)
        >>> point
        Point(3, 4)
        >>> point.get_tuple
        (3, 4)
        """
        return self.x, self.y

    @x.setter
    def x(self, x):
        self.__x = x

    @y.setter
    def y(self, y):
        self.__y = y

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y

    def __repr__(self):
        return ("{0.__class__.__name__}({0.x!r}, {0.y!r})".format(
                self))

    def __str__(self):
        return "({0.x!r}, {0.y!r})".format(self)

    def __add__(self, other):
        return Point(self.x+other.x, self.y+other.y)

    def __sub__(self, other):
        return Point(self.x-other.x, self.y-other.y)

    def __iadd__(self, other):
        self.x += other.x
        self.y += other.y
        return Point(self.x, self.y)

    def __isub__(self, other):
        self.x -= other.x
        self.y -= other.y
        return Point(self.x, self.y)

    def __pos__(self):
        return Point(self.x, self.y)

    def __neg__(self):
        return Point(-self.x, -self.y)

    def __mul__(self, length):
        return Point(self.x*length, self.y*length)

    def __imul__(self, length):
        self.x *= length
        self.y *= length
        return Point(self.x, self.y)

    def __truediv__(self, length):
        assert length != 0, "division by zero"
        return Point(self.x/length, self.y/length)

    def __itruediv__(self, length):
        assert length != 0, "division by zero"
        self.x /= length
        self.y /= length
        return Point(self.x, self.y)

    def length_from_point(self, other):
        return Point(self.x - other.x, self.y - other.y).distance_from_origin()

    def get_normalized(self):
        length = self.distance_from_origin
        if length == 0:
            return Point(0, 0)
        return Point(self.x / length, self.y / length)

    @staticmethod
    def distance_between_points(point_1, point_2):
        return point_1.length_from_point(point_2)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
