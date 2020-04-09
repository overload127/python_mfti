#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import turtle

def draw_line(l, n):
    turtle.forward(l)
    if n == 0:
        return
    
    x,y = turtle.pos()
    turtle.penup()
    turtle.setposition(x-l,y-10)
    turtle.pendown()
    
    lenght = l / 3
    draw_line(lenght, n-1)
    turtle.penup()
    turtle.forward(lenght)
    turtle.pendown()
    draw_line(lenght, n-1)

    x,y = turtle.pos()
    turtle.penup()
    turtle.setposition(x,y+10)
    turtle.pendown()
    


turtle.penup()
turtle.setposition(-350,300)
turtle.pendown()

turtle.speed('fastest')
draw_line(800, 5)
