#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import pygame
from circlebot import CircleBot
from point import Point
from color import Color

pygame.init()

k = 0.003
width = 500
height = 500
p = Point(20, 20)
c = Color(0, 50, 255)
m = Point(5, 3)
b = Point(0.5, 0.5)
circle_1 = CircleBot(20, p, c, m, b)
p = Point(width-20, height-20)
circle_2 = CircleBot(20, p, c, m, b)


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
                circle_1.move -= Point(0, 5)
            elif event.key == pygame.K_DOWN:
                circle_1.move += Point(0, 5)
            elif event.key == pygame.K_RIGHT:
                circle_1.move += Point(5, 0)
            elif event.key == pygame.K_LEFT:
                circle_1.move -= Point(5, 0)
            elif event.key == pygame.K_KP_PLUS:
                circle_1.move += circle_1.move / 5

    circle_1.next_step()
    circle_2.next_step()

    circle_1.check_wall(width, height)
    circle_2.check_wall(width, height)

    circle_1.execute_friction_to_boost(k)
    circle_1.change_move()
    circle_1.collision_old(circle_2)
    circle_1.change_color_from_move()

    circle_2.execute_friction_to_boost(k)
    circle_2.change_move()
    circle_2.change_color_from_move()

    screen.fill((0, 0, 0))
    circle_1.draw(screen)
    circle_2.draw(screen)

    pygame.display.flip()
