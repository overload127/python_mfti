#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import turtle


def circle():
    turtle.penup()
    turtle.forward(100)
    turtle.pendown()
    turtle.left(90)
    turtle.circle(100)


def main():
    turtle.shape('turtle')
    circle()


main()
