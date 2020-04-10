#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import turtle


def spiral_v_1(N=100):
    i = 0
    while i < N:
        r = 1*i
        turtle.circle(r,57)
        i += 1


def spiral_v_2(N=100):
    i = 1
    while i < N:
        for j in range(i):
            turtle.forward(1)
        turtle.left(360 / i)
        i += 1


def spiral_v_3(N=1000):
    for i in range(N):
        turtle.forward(i * 0.001)
        turtle.left(1)


def main():
    turtle.shape('turtle')
    turtle.speed(speed=0)
    spiral_v_3(1000 * 5)


main()
