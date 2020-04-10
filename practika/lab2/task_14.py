#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import turtle


def star(width=200, v=5):
    turtle.forward(width/2)
    turtle.left(180)
    angel = 180/v
    i = 0
    while i < v:
        turtle.forward(width)
        turtle.left(180-angel)
        i += 1
    turtle.done()


def main():
    turtle.shape('turtle')
    star(200, 11)


main()
