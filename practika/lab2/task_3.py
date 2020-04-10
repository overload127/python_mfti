#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import turtle


def quadr(x=50):
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(x)
    turtle.left(90)


def main():
    turtle.shape('turtle')
    quadr()


main()
