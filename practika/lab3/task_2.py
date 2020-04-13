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

    # чел
    human()
    
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
    # рыбка над телом, но под головой
    fish()
    # голова
    penColor(222, 222, 222)
    brushColor(222, 222, 222)
    oval(95, 633, 155, 683)
    polygon([(123, 620), (115, 635), (130, 635), (123, 620)])
    polygon([(123+15, 620), (115+15, 635), (130+15, 645), (123+15, 620)])
    penColor(255, 255, 255)
    brushColor(255, 255, 255)
    polygon([(110, 680), (112, 685), (114, 680), (110, 680)])
    polygon([(120, 683), (122, 688), (124, 683), (120, 683)])
    penColor(242, 242, 242)
    brushColor(255, 255, 255)
    oval(100, 643, 115, 655)
    oval(125, 648, 140, 660)
    penColor(0, 0, 0)
    brushColor(0, 0, 0)
    circle(112, 649, 3)
    circle(136, 654, 3)
    circle(115, 670, 2)


def fish():
    """ рыба """
    penColor(0, 0, 0)
    brushColor(173, 36, 5)
    polygon([(110, 680), (110, 660), (80, 660), (110, 680)])
    polygon([(100, 680), (100, 700), (130, 700), (100, 680)])
    penColor(0, 0, 0)
    brushColor(54, 156, 107)
    oval(75, 670, 145, 690)
    polygon([(145, 680), (170, 690), (170, 670), (145, 680)])
    penColor(5, 53, 130)
    brushColor(5, 53, 130)
    circle(85, 680, 4)
    penColor(255, 255, 255)
    brushColor(255, 255, 255)
    circle(86, 680, 1)


def human():
    """ человек """
    penColor(209, 192, 171)
    brushColor(209, 192, 171)
    oval(400, 385, 555, 475)
    penColor(122, 95, 62)
    brushColor(122, 95, 62)
    oval(375, 500, 450, 530)
    oval(500, 500, 575, 530)
    oval(425, 575, 465, 725)
    oval(485, 575, 525, 725)

    oval(390, 700, 450, 735)
    oval(500, 700, 560, 735)
    arc(400, 450, 550, 850, 0, 180)
    penColor(89, 69, 45)
    brushColor(89, 69, 45)
    rectangle(400, 650, 550, 670)
    rectangle(460, 425, 490, 648)
    penColor(179, 155, 127)
    brushColor(179, 155, 127)
    oval(415, 400, 540, 460)
    penColor(179, 155, 127)
    brushColor(179, 155, 127)
    oval(415, 400, 540, 460)
    penColor(209, 192, 171)
    brushColor(209, 192, 171)
    oval(425, 410, 530, 450)
    penColor(0, 0, 0)
    brushColor(0, 0, 0)
    line(380, 475, 390, 700)
    line(445, 420, 465, 430)
    line(485, 430, 515, 425)
    arc(465, 455, 500, 440, 0, 180, ARC)



def hata():
    """ хата """
    penColor(0, 0, 0)
    brushColor(222, 222, 222)
    arc(50, 375, 380, 650, 0, 180)
    line(58, 475, 374, 475)
    line(80, 433, 348, 433)
    line(145, 390, 290, 390)

    line(112, 475, 100, 513)
    line(160, 475, 150, 513)
    line(205, 475, 200, 513)
    line(245, 475, 250, 513)
    line(290, 475, 300, 513)
    line(338, 475, 350, 513)

    line(115, 475, 125, 433)
    line(165, 475, 170, 433)
    line(215, 475, 215, 433)
    line(265, 475, 260, 433)
    line(315, 475, 305, 433)

    line(160, 390, 150, 433)
    line(205, 390, 200, 433)
    line(245, 390, 250, 433)
    line(290, 390, 300, 433)

    line(225, 390, 225, 375)


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