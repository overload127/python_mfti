#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import pygame
import math

def get_length_from_coord(pos_1, pos_2):
    putch_xy = pos_1[0] - pos_2[0], pos_1[1] - pos_2[1]
    return math.sqrt(putch_xy[0]**2 + putch_xy[1]**2) 

pygame.init()

# select_tusk_from_key = {}

width = 500
height = 500

radius_cir = 20
x_cir = 20
y_cir = 20
x_change = 5
y_change = 3
x_a = 0
y_a = 0
k = 0.01

screen = pygame.display.set_mode((width, height))
pygame.display.set_caption('YAHOOOO')
clock = pygame.time.Clock()

while True:
    dt = clock.tick(50) / 1000.0

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit()
            elif event.key == pygame.K_UP:
                y_change -= 5
            elif event.key == pygame.K_DOWN:
                y_change += 5
            elif event.key == pygame.K_RIGHT:
                x_change += 5
            elif event.key == pygame.K_LEFT:
                x_change -= 5

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
    
    x_change += x_a
    y_change += y_a

    len_change = get_length_from_coord([0, 0], [x_change, y_change])
    if len_change < 0.5:
        x_change = 0
        y_change = 0
    

    x_a = -x_change * k
    y_a = -y_change * k


    screen.fill((0, 0, 0))
    pygame.draw.circle(screen, (150, 10, 50), (int(x_cir), int(y_cir)), radius_cir)

    pygame.display.flip()