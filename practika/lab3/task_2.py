#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from graph import *


width = 642
heigth = 990


def main():

    windowSize(width, heigth)
    canvasSize(width-10, heigth-10)
    background()

    hata()

    # кошак
    cat()
    
    run()


def cat():
    """ кошак """
    penColor(222, 222, 222)
    brushColor(222, 222, 222)
    # тело
    oval(105, 675, 305, 715)
    # хвост
    oval(280, 695, 380, 670)
    # лапы
    oval(260, 700, 280, 765)
    oval(240, 705, 260, 775)
    oval(160, 700, 180, 765)
    oval(140, 705, 160, 775)
    # голова
    oval(95, 633, 155, 683)
    polygon([(123, 620), (115, 635), (130, 635), (123, 620)])
    polygon([(123+15, 620), (115+15, 635), (130+15, 645), (123+15, 620)])
    penColor(242, 242, 242)
    brushColor(255, 255, 255)
    oval(100, 643, 115, 655)
    oval(125, 648, 140, 660)
    penColor(0, 0, 0)
    brushColor(0, 0, 0)
    circle(112, 649, 3)
    circle(136, 654, 3)
    circle(115, 670, 2)


def hata():
    """ хата """
    penColor(0, 0, 0)
    brushColor(222, 222, 222)
    arc(50, 375, 380, 650, 0, 180)
    line(58, 475, 374, 475)
    line(80, 433, 348, 433)
    line(145, 390, 290, 390)


def background():
    """ Задний план картинки """
    penColor(222, 222, 222)
    brushColor(222, 222, 222)
    rectangle(-5, -5, width+5, heigth*0.4)

    penColor(242, 242, 242)
    brushColor(242, 242, 242)
    rectangle(-5, heigth*0.4, width+5, heigth+5)

    penColor(237, 237, 237)
    penColor(237, 237, 237)
    rectangle(-5, heigth*0.45, width+5, heigth*0.70)

main()