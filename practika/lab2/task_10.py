#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import turtle


def flower(rad=25, lepestki=3):
    angel = 180 / lepestki
    i = 1
    turtle.circle(rad)
    turtle.circle(-rad)
    while i < lepestki:
        turtle.left(angel)
        turtle.circle(rad)
        turtle.circle(-rad)
        i += 1


def main():
    turtle.shape('turtle')
    flower()


main()
