#!/usr/bin/env python3
# -*- coding: utf-8 -*-


import turtle

def draw_line(l, n, sign=1):
    if n == 0:
        turtle.forward(l)
        return

    x = l / 3 * 2
    turtle.right(45*sign)
    draw_line(x, n-1,1)
    turtle.left(90*sign)
    draw_line(x, n-1,-1)
    turtle.right(45*sign)
    


turtle.speed('fastest')
draw_line(400, 10)
