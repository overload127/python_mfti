#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import math
from circle import Circle
from point import Point
from color import Color


class CircleBot(Circle):

    def __init__(self, radius, point=Point(),
                 color=Color(), move=Point(0, 0), _boost=Point(0, 0)):
        """A CircleBot

        >>> circle_1 = CircleBot(2)
        >>> circle_1
        CircleBot(2, Point(0, 0), Color(111, 111, 111),
        Point(0, 0), Point(0, 0))

        >>> circle_2 = CircleBot(2)
        >>> circle_2
        CircleBot(2, Point(0, 0), Color(111, 111, 111),
        Point(0, 0), Point(0, 0))

        >>> circle_1 == circle_2
        True
        >>> circle_1.point = Point(10, 10)
        >>> circle_1 == circle_2
        False
        >>> circle_1.point = Point(0, 0)
        >>> circle_1 == circle_2
        True
        >>> circle_1.move = Point(10, 10)
        >>> circle_1 == circle_2
        False
        >>> circle_1.move = Point(0, 0)
        >>> circle_1 == circle_2
        True
        >>> circle_1.boost = Point(10, 10)
        >>> circle_1 == circle_2
        False
        >>> circle_1.boost = Point(0, 0)
        >>> circle_1 == circle_2
        True
        """
        super().__init__(radius, point, color)
        self.move = Point(*move.get_tuple)
        self.boost = Point(*_boost.get_tuple)

    @property
    def move(self):
        return Point(self.__move.x, self.__move.y)

    @property
    def boost(self):
        return Point(self.__boost.x, self.__boost.y)

    @move.setter
    def move(self, point):
        self.__move = Point(point.x, point.y)

    @boost.setter
    def boost(self, point):
        self.__boost = Point(point.x, point.y)

    def __eq__(self, other):
        return (super().__eq__(other) and self.move == other.move and
                self.boost == other.boost)

    def __repr__(self):
        return (("{0.__class__.__name__}({0.radius!r}, {1}, {2}, {3}, "
                "{4})").format(
                self, self.point.__repr__(), self.color.__repr__(),
                self.move.__repr__(), self.boost.__repr__()))

    def __str__(self):
        line = super().__str__()
        line += ' ' + self.move + ' ' + self.boost
        return line

    def next_step(self):
        self.point += self.move

    def change_move(self):
        self.move += self.boost

        if self.move.distance_from_origin < 0.5:
            self.move = Point(0, 0)

    def execute_friction_to_boost(self, k):
        self.boost = -(self.move * k)

    def change_color_from_move(self):
        _move = self.move.distance_from_origin
        if _move > 20:
            self.color = Color(255, self.color.g, 0)
        elif _move == 0:
            self.color = Color(0, self.color.g, 255)
        else:
            self.color = Color(255 * (_move/20),
                               self.color.g,
                               255 * (5/(_move+5)))

    def check_wall(self, width, height):
        if self.point.x >= width - self.radius:
            self.move = Point(-abs(self.move.x), self.move.y)
            self.point = Point((width - self.radius) -
                               (self.point.x - (width - self.radius)),
                               self.point.y)
        elif self.point.x <= self.radius:
            self.move = Point(abs(self.move.x), self.move.y)
            self.point = Point(self.radius + self.radius -
                               self.point.x, self.point.y)
        if self.point.y >= height - self.radius:
            self.move = Point(self.move.x, -abs(self.move.y))
            self.point = Point(self.point.x, (height - self.radius) -
                               (self.point.y - (height - self.radius)))
        elif self.point.y <= self.radius:
            self.move = Point(self.move.x, abs(self.move.y))
            self.point = Point(self.point.x, self.radius + self.radius -
                               self.point.y)

    def collision_old(self, circle):
        dx = self.point.x - circle.point.x
        dy = self.point.y - circle.point.y
        length = math.sqrt(dx**2 + dy**2)

        if length < self.radius + circle.radius:
            self.move, circle.move = circle.move, self.move

    def collision(self, circle):
        dx = self.point.x - circle.point.x
        dy = self.point.y - circle.point.y
        length = math.sqrt(dx**2 + dy**2)

        if length < self.radius + circle.radius:
            v1 = Point(circle.point.x - self.point.x, circle.point.y -
                       self.point.y).get_normalized()
            v2 = -v1

            l1 = self.move.distance_from_origin
            l2 = circle.move.distance_from_origin
            self.move = (self.move.get_normalized() +
                         v2).get_normalized() * l1
            circle.move = (circle.move.get_normalized() +
                           v1).get_normalized() * l2


if __name__ == "__main__":
    import doctest
    doctest.testmod(optionflags=doctest.NORMALIZE_WHITESPACE)
