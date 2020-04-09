#!/usr/bin/env python3


import turtle
import math

def main():
    turtle.shape('turtle')
    star_moe(400, 21)

def moe_4_circle():
    turtle.penup()
    turtle.forward(100)
    turtle.pendown()
    turtle.left(90)
    turtle.circle(100)

def moe_2_5():
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.left(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)
    turtle.right(90)
    turtle.forward(50)

def moe_4_quadr(x=50):
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(x)
    turtle.left(90)
    turtle.forward(x)
    turtle.left(90)

def moe_5_x_quadr(count=10,step=5):
    i = 0
    while i < count:
        i += 1
        moe_4_quadr(5+i*step*2)
        turtle.penup()
        turtle.right(135)
        turtle.forward(step)
        turtle.right(90)
        turtle.forward(step)
        turtle.right(90)
        turtle.right(90)
        turtle.pendown()

def moe_6_spaider(count=None,angel=30):
    if count:
        angel = 360 // count
    i = 0
    while i < 360:
        turtle.right(angel)
        turtle.forward(100)
        turtle.stamp()
        turtle.right(180)
        turtle.forward(100)
        turtle.left(180)
        i += angel

def moe_7_spir(N=100):
    i = 0
    while i < N:
        r = 1*i
        turtle.circle(r,57)
        i += 1

def moe_8_qub_spir(N=100):
    i = 0
    while i < N:
        turtle.forward(5+i*4)
        turtle.left(90)
        i += 1
    
def moe_9_true_mnogo(n=10, len_side=25):
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

def moe_10_flower(rad=25, lepestki=3):
    angel = 180 / lepestki
    i = 1
    turtle.circle(rad)
    turtle.circle(-rad)
    while i < lepestki:
        turtle.left(angel)
        turtle.circle(rad)
        turtle.circle(-rad)
        i += 1

def moe_11_baterfly(rad=25, lepestki=3):
    i = 1
    while i <= lepestki:
        turtle.circle(rad+i*5)
        turtle.circle(-rad-i*5)

        i += 1

def moe_12_spring(rad=25, count=3):
    i = 1
    while i <= count:
        turtle.circle(-rad,180)
        turtle.circle(-rad/5,180)
        i += 1 

def moe_13_smile(rad=25):
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

def star_moe(width=200, v=5):
    turtle.forward(width/2)
    turtle.left(180)
    #turtle.color('red', 'yellow')
    #turtle.begin_fill()
    angel = 180/v
    i = 0
    while i < v:
        turtle.forward(width)
        turtle.left(180-angel)
        i += 1
    #turtle.end_fill()
    turtle.done()

main()
