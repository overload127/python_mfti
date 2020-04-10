#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import turtle


def quadrs(count=10,step=5):
    i = 0
    while i < count:
        i += 1
        cur_step = 5+i*step*2
        delta = abs(cur_step - (5+(i+1)*step*2)) // 2
        delta = (delta**2 + delta**2) ** 0.5
        quadr(cur_step)
        turtle.penup()
        turtle.right(135)
        turtle.forward(delta)
        turtle.left(135)
        turtle.pendown()


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
    quadrs()


main()
