#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import turtle


def spring(rad=25, count=3):
    i = 1
    while i <= count:
        turtle.circle(-rad,180)
        turtle.circle(-rad/5,180)
        i += 1 


def main():
    turtle.shape('turtle')
    spring()


main()
