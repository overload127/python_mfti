#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from graph import *


width = 642
heigth = 990


def main():

    windowSize(width, heigth)
    canvasSize(width-10, heigth-10)
    background()


    hata_small(20, 370)
    hata_small(310, 390)
    hata(50, 450)
    hata_small(35, 520)
    hata_small(90, 570)

    # кошак
    cat(95, 550)
    cat(-100, 630)
    cat(95, 720)
    cat(200, 900)
    cat(400, 800)

    # челы
    human_small(400, 350, False)
    human_small(530, 370, False)
    human_small(450, 400, False)
    human_small(490, 470, False)
    human_small(430, 450, True)
    human_small(370, 400, True)
    human_small(310, 470, True)

    human(420, 520, False)

    run()


def cat(x, y):
    """ кошак """
    penColor(222, 222, 222)
    brushColor(222, 222, 222)
    # тело
    oval(x+10, y+55, x+210, y+95)
    # хвост
    oval(x+185, y+75, x+285, y+50)
    # лапы
    oval(x+165, y+80, x+185, y+145)
    oval(x+145, y+85, x+165, y+155)
    oval(x+75, y+80, x+95, y+145)
    oval(x+55, y+85, x+75, y+155)
    # рыбка над телом, но под головой
    fish(x-20, y+40)
    # голова
    penColor(222, 222, 222)
    brushColor(222, 222, 222)
    oval(x, y+13, x+60, y+63)
    polygon([(x+28, y), (x+20, y+15), (x+35, y+15), (x+28, y)])
    polygon([(x+43, y), (x+35, y+15), (x+50, y+25), (x+43, y)])
    penColor(255, 255, 255)
    brushColor(255, 255, 255)
    polygon([(x+15, y+60), (x+17, y+65), (x+19, y+60), (x+15, y+60)])
    polygon([(x+25, y+63), (x+27, y+68), (x+29, y+63), (x+25, y+63)])
    penColor(242, 242, 242)
    brushColor(255, 255, 255)
    oval(x+5, y+23, x+20, y+35)
    oval(x+30, y+28, x+45, y+40)
    penColor(0, 0, 0)
    brushColor(0, 0, 0)
    circle(x+17, y+29, 3)
    circle(x+41, y+34, 3)
    circle(x+20, y+50, 2)


def fish(x, y):
    """ рыба """
    penColor(0, 0, 0)
    brushColor(173, 36, 5)
    polygon([(x+35, y+20), (x+35, y), (x+5, y), (x+35, y+20)])
    polygon([(x+25, y+20), (x+25, y+40), (x+55, y+40), (x+25, y+20)])
    penColor(0, 0, 0)
    brushColor(54, 156, 107)
    oval(x, y+10, x+70, y+30)
    polygon([(x+75, y+20), (x+95, y+30), (x+95, y+10), (x+70, y+20)])
    penColor(5, 53, 130)
    brushColor(5, 53, 130)
    circle(x+10, y+20, 4)
    penColor(255, 255, 255)
    brushColor(255, 255, 255)
    circle(x+11, y+20, 1)


def human(x, y, hand):
    """ человек """
    # капюшон
    penColor(209, 192, 171)
    brushColor(209, 192, 171)
    oval(x+30, y, x+130, y+75)
    # руки
    penColor(122, 95, 62)
    brushColor(122, 95, 62)
    oval(x, y+80, x+60, y+100)
    oval(x+100, y+80, x+160, y+100)
    # ноги
    oval(x+40, y+125, x+65, y+200)
    oval(x+95, y+125, x+120, y+200)
    oval(x+25, y+190, x+60, y+200)
    oval(x+100, y+190, x+135, y+200)
    # тело
    arc(x+30, y+50, x+130, y+300, 0, 180)
    penColor(89, 69, 45)
    brushColor(89, 69, 45)
    rectangle(x+30, y+155, x+130, y+175)
    rectangle(x+70, y+70, x+90, y+150)
    # голова
    penColor(179, 155, 127)
    brushColor(179, 155, 127)
    oval(x+40, y+10, x+120, y+65)
    penColor(209, 192, 171)
    brushColor(209, 192, 171)
    oval(x+50, y+22, x+110, y+58)
    # лицо
    penColor(0, 0, 0)
    brushColor(0, 0, 0)
    line(x+60, y+30, x+72, y+42)
    line(x+88, y+42, x+100, y+35)
    arc(x+65, y+50, x+95, y+60, 0, 180, ARC)
    # палка
    if hand:
        line(x+150, y+10, x+145, y+180)
    else:
        line(x+15, y+10, x+20, y+180)


def human_small(x, y, hand=False):
    """ человек """
    # капюшон
    penColor(209, 192, 171)
    brushColor(209, 192, 171)
    oval(x+15, y, x+65, y+37)
    # руки
    penColor(122, 95, 62)
    brushColor(122, 95, 62)
    oval(x, y+40, x+30, y+50)
    oval(x+50, y+40, x+80, y+50)
    # ноги
    oval(x+20, y+67, x+27, y+100)
    oval(x+47, y+67, x+54, y+100)
    oval(x+12, y+92, x+30, y+100)
    oval(x+44, y+92, x+62, y+100)
    # тело
    arc(x+15, y+25, x+65, y+150, 0, 180)
    penColor(89, 69, 45)
    brushColor(89, 69, 45)
    rectangle(x+15, y+77, x+65, y+87)
    rectangle(x+35, y+35, x+45, y+75)
    # голова
    penColor(179, 155, 127)
    brushColor(179, 155, 127)
    oval(x+20, y+5, x+60, y+32)
    penColor(209, 192, 171)
    brushColor(209, 192, 171)
    oval(x+25, y+11, x+55, y+29)
    # лицо
    penColor(0, 0, 0)
    brushColor(0, 0, 0)
    line(x+30, y+15, x+36, y+21)
    line(x+44, y+21, x+50, y+17)
    arc(x+32, y+25, x+47, y+30, 0, 180, ARC)
    # палка
    if hand:
        line(x+75, y+5, x+72, y+90)
    else:
        line(x+7, y+5, x+10, y+90)


def hata(x, y):
    """ хата """
    penColor(0, 0, 0)
    brushColor(222, 222, 222)
    arc(x, y-75, x+330, y+200, 0, 180)
    line(x+8, y+25, x+324, y+25)
    line(x+30, y-17, x+298, y-17)
    line(x+95, y-60, x+240, y-60)

    line(x+62, y+25, x+50, y+63)
    line(x+110, y+25, x+100, y+63)
    line(x+155, y+25, x+150, y+63)
    line(x+195, y+25, x+200, y+63)
    line(x+240, y+25, x+250, y+63)
    line(x+288, y+25, x+300, y+63)

    line(x+65, y+25, x+75, y-17)
    line(x+115, y+25, x+120, y-17)
    line(x+165, y+25, x+165, y-17)
    line(x+215, y+25, x+210, y-17)
    line(x+265, y+25, x+255, y-17)

    line(x+110, y-60, x+100, y-17)
    line(x+155, y-60, x+150, y-17)
    line(x+195, y-60, x+200, y-17)
    line(x+240, y-60, x+250, y-17)

    line(x+175, y-60, x+175, y-75)


def hata_small(x, y):
    """ хата """
    s = 2
    penColor(0, 0, 0)
    brushColor(222, 222, 222)
    arc(x, y-75/s, x+330/s, y+200/s, 0, 180)
    line(x+8/s, y+25/s, x+324/s, y+25/s)
    line(x+30/s, y-17/s, x+298/s, y-17/s)
    line(x+95/s, y-60/s, x+240/s, y-60/s)

    line(x+62/s, y+25/s, x+50/s, y+63/s)
    line(x+110/s, y+25/s, x+100/s, y+63/s)
    line(x+155/s, y+25/s, x+150/s, y+63/s)
    line(x+195/s, y+25/s, x+200/s, y+63/s)
    line(x+240/s, y+25/s, x+250/s, y+63/s)
    line(x+288/s, y+25/s, x+300/s, y+63/s)

    line(x+65/s, y+25/s, x+75/s, y-17/s)
    line(x+115/s, y+25/s, x+120/s, y-17/s)
    line(x+165/s, y+25/s, x+165/s, y-17/s)
    line(x+215/s, y+25/s, x+210/s, y-17/s)
    line(x+265/s, y+25/s, x+255/s, y-17/s)

    line(x+110/s, y-60/s, x+100/s, y-17/s)
    line(x+155/s, y-60/s, x+150/s, y-17/s)
    line(x+195/s, y-60/s, x+200/s, y-17/s)
    line(x+240/s, y-60/s, x+250/s, y-17/s)

    line(x+175/s, y-60/s, x+175/s, y-75/s)


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