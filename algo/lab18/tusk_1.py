#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import pygame

pygame.init()

width = 500
height = 500

radius_cir = 20
x_cir = 20
y_cir = 20
x_change = 5
y_change = 3

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('YAHOOOO')
clock = pygame.time.Clock()

while True:
    dt = clock.tick(50) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT or event.type == pygame.KEYDOWN:
            sys.exit()

    x_cir += x_change
    y_cir += y_change

    if x_cir >= width - radius_cir:
        x_change = -abs(x_change)
        x_cir = (width - radius_cir) - (x_cir - (width - radius_cir))
    elif x_cir <= radius_cir:
        x_change = abs(x_change)
        x_cir = radius_cir + radius_cir - x_cir
    if y_cir >= height - radius_cir:
        y_change = -abs(y_change)
        y_cir -= y_cir - (height - radius_cir)
    elif y_cir <= radius_cir:
        y_change = abs(y_change)
        y_cir = radius_cir + radius_cir - y_cir


    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (150, 10, 50), (int(x_cir), int(y_cir)), radius_cir)

    pygame.display.flip()