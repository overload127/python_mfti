#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import turtle

def draw_line(l, n):
    if n == 0:
        turtle.forward(l)
        return

    x = l*n / (3*n)
    draw_line(x, n-1)
    turtle.left(60)
    draw_line(x, n-1)
    turtle.right(120)
    draw_line(x, n-1)
    turtle.left(60)
    draw_line(x, n-1)


def draw_star(l, n):
    draw_line(l, n)
    turtle.right(120)
    draw_line(l, n)
    turtle.right(120)
    draw_line(l, n)


turtle.speed('fastest')
draw_star(400, 6)
