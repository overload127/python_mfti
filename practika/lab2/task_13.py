#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import turtle


def smile(rad=25):
    XC = 0.2
    print(turtle.xcor())
    print(turtle.ycor())
    turtle.penup()
    turtle.forward(rad)
    turtle.pendown()
    turtle.left(90)
    turtle.color("black", "yellow")
    turtle.begin_fill()
    turtle.circle(rad)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(-rad*0.5+rad*XC, rad*0.5)
    turtle.pendown()

    turtle.color("black", "blue")
    turtle.begin_fill()
    turtle.circle(rad*XC)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(rad*0.5+rad*XC, rad*0.5)
    turtle.pendown()

    turtle.color("black", "blue")
    turtle.begin_fill()
    turtle.circle(rad*XC)
    turtle.end_fill()

    turtle.penup()
    turtle.goto(0, rad*XC)
    turtle.left(180)
    turtle.pendown()

    turtle.pen(fillcolor="black", pencolor="black", pensize=10+6)
    turtle.forward(rad*XC*2)

    turtle.penup()
    turtle.goto(rad*0.5, -rad*0.5+rad*XC)
    turtle.pendown()

    turtle.pen(fillcolor="red", pencolor="red", pensize=10+6)
    turtle.circle(-rad/2,180)


def main():
    turtle.shape('turtle')
    smile(100)


main()
