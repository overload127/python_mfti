#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import turtle

def draw_line(l, n):
    if n == 0:
        turtle.forward(l)
        return

    x = l*n / (4*n)
    draw_line(x, n-1)
    turtle.left(90)
    draw_line(x, n-1)
    turtle.right(90)
    draw_line(x, n-1)
    turtle.right(90)
    draw_line(x, n-1)
    draw_line(x, n-1)
    turtle.left(90)
    draw_line(x, n-1)
    turtle.left(90)
    draw_line(x, n-1)
    turtle.right(90)
    draw_line(x, n-1)



turtle.speed('fastest')
draw_line(400, 6)
