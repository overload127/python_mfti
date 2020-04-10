#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import turtle
import math


def mnogo(n=10, len_side=25):
    i = 1
    start_len = len_side / 2.5
    while i < n:
        mnogougolnik(len_side, i + 2)
        len_side += start_len * (1.2/i**2)
        i += 1


def mnogougolnik(a=100, n=3):
    r = a /(2* math.sin(2*math.pi/(2*n)))
    angel = 360 / n
    turtle.penup()
    turtle.forward(r - turtle.xcor())
    turtle.pendown()
    angel_sdvig = 90 - (180 * (n - 2))/(n*  2)
    turtle.left(90 + angel_sdvig)
    turtle.forward(a)
    while n > 1:
        n -= 1
        turtle.left(angel)
        turtle.forward(a)
    turtle.right(90 - angel_sdvig)


def main():
    turtle.shape('turtle')
    mnogo()


main()
