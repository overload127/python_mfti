#!/usr/bin/env python3
# -*- coding: utf-8 -*-


class Color:

    def __init__(self, r=111, g=111, b=111):
        """A color in formar RGB

        >>> color = Color()
        >>> color
        Color(111, 111, 111)

        >>> color = Color(11, 44, 22)
        >>> color
        Color(11, 44, 22)

        >>> color = Color(256, 44, 22)
        Traceback (most recent call last):
        ...
        AssertionError: red color must be from 0 to 255

        >>> color = Color(11, 256, 22)
        Traceback (most recent call last):
        ...
        AssertionError: green color must be from 0 to 255

        >>> color = Color(11, 44, 256)
        Traceback (most recent call last):
        ...
        AssertionError: blue color must be from 0 to 255
        """
        self.r = r
        self.g = g
        self.b = b

    @property
    def r(self):
        return self.__r

    @property
    def g(self):
        return self.__g

    @property
    def b(self):
        return self.__b

    @property
    def get_tuple(self):
        """This property return color in RGB in tuple

        >>> color = Color(11, 44, 22)
        >>> color
        Color(11, 44, 22)
        >>> color.get_tuple
        (11, 44, 22)
        """
        return self.r, self.g, self.b

    @r.setter
    def r(self, r):
        assert 255 >= r >= 0, "red color must be from 0 to 255"
        self.__r = r

    @g.setter
    def g(self, g):
        assert 255 >= g >= 0, "green color must be from 0 to 255"
        self.__g = g

    @b.setter
    def b(self, b):
        assert 255 >= b >= 0, "blue color must be from 0 to 255"
        self.__b = b

    def __eq__(self, other):
        return self.r == other.r and self.g == other.g and self.b == other.b

    def __repr__(self):
        return ("{0.__class__.__name__}({0.r!r}, {0.g!r}, {0.b!r})".format(
                self))

    def __str__(self):
        return "({0.r!r}, {0.g!r}, {0.b!r})".format(self)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
