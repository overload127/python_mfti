#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import turtle


def spaider(count=None,angel=30):
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


def main():
    turtle.shape('turtle')
    spaider()


main()
