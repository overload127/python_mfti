#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import turtle


def baterfly(rad=25, lepestki=3):
    i = 1
    while i <= lepestki:
        turtle.circle(rad+i*5)
        turtle.circle(-rad-i*5)

        i += 1


def main():
    turtle.shape('turtle')
    baterfly()


main()
