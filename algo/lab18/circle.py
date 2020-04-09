#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from point import Point
from color import Color
import pygame


class Circle:
    def __init__(self, radius, point=Point(),
                 color=Color()):
        """A Circle

        >>> circle = Circle(2)
        >>> circle
        Circle(2, Point(0, 0), Color(111, 111, 111))
        """
        self.point = Point(*point.get_tuple)
        self.color = Color(*color.get_tuple)
        self.radius = radius

    @property
    def point(self):
        return Point(self.__point.x, self.__point.y)

    @property
    def color(self):
        return Color(self.__color.r, self.__color.g, self.__color.b)

    @property
    def radius(self):
        """The circle's radius

        >>> circle = Circle(-2)
        Traceback (most recent call last):
        ...
        AssertionError: radius must be nonzero and non-negative
        >>> circle = Circle(4)
        >>> circle.radius = -1
        Traceback (most recent call last):
        ...
        AssertionError: radius must be nonzero and non-negative
        >>> circle.radius = 6
        """
        return self.__radius

    @property
    def edge_distance_from_origin(self):
        """The distance of the circle's edge from the origin

        >>> point = Point(3, 4)
        >>> circle = Circle(2, point)
        >>> circle.edge_distance_from_origin
        3.0
        """
        return abs(self.point.distance_from_origin - self.radius)

    @point.setter
    def point(self, point):
        self.__point = Point(point.x, point.y)

    @color.setter
    def color(self, color):
        self.__color = Color(color.r, color.g, color.b)

    @radius.setter
    def radius(self, radius):
        assert radius > 0, "radius must be nonzero and non-negative"
        self.__radius = radius

    def __eq__(self, other):
        return (self.point == other.point and self.color == other.color and
                self.radius == other.radius)

    def __repr__(self):
        return ("{0.__class__.__name__}({0.radius!r}, {1}, {2})".format(
                self, self.point.__repr__(), self.color.__repr__()))

    def __str__(self):
        line = self.point + ' ' + self.color + ' ' + str(self.radius)
        return line

    def draw(self, screen):
        pygame.draw.circle(screen, self.color.get_tuple,
                           (int(self.point.x), int(self.point.y)),
                           self.radius)


if __name__ == "__main__":
    import doctest
    doctest.testmod()
