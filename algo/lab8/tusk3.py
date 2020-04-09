#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import turtle

def draw(l, n):
    if n == 0:
        turtle.forward(l)
        return

    x = l*n / (3*n)
    draw(x, n-1)
    turtle.left(60)
    draw(x, n-1)
    turtle.right(120)
    draw(x, n-1)
    turtle.left(60)
    draw(x, n-1)

turtle.speed('fastest')
draw(400, 1)
