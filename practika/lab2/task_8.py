#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import turtle


def quadr_spir(N=100):
    i = 0
    while i < N:
        turtle.forward(5+i*4)
        turtle.left(90)
        i += 1


def main():
    turtle.shape('turtle')
    quadr_spir()


main()
