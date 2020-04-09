#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import pygame
from circlebot import CircleBot
from point import Point
from color import Color


def add_new_circle_under_mouse(p):
    c = Color(0, 50, 255)
    m = Point(5, 3)
    b = Point(0.5, 0.5)
    all_circle.append(CircleBot(20, p, c, m, b))


pygame.init()

k = 0.002
width = 500
height = 500
all_circle = []
add_new_circle_under_mouse(Point(20, 20))

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
                all_circle[-1].move -= Point(0, 5)
            elif event.key == pygame.K_DOWN:
                all_circle[-1].move += Point(0, 5)
            elif event.key == pygame.K_RIGHT:
                all_circle[-1].move += Point(5, 0)
            elif event.key == pygame.K_LEFT:
                all_circle[-1].move -= Point(5, 0)
            elif event.key == pygame.K_KP_PLUS:
                all_circle[-1].move += all_circle[-1].move / 5
        elif event.type == pygame.MOUSEBUTTONDOWN:
            if event.button == 1:
                # left
                add_new_circle_under_mouse(Point(event.pos[0], event.pos[1]))
            elif event.button == 2:
                # centr
                for i in range(len(all_circle)):
                    all_circle[i].move += all_circle[i].move / 5
            elif event.button == 3:
                # rigth
                if len(all_circle) > 1:
                    del(all_circle[-1])

    screen.fill((0, 0, 0))
    count = len(all_circle)
    for i in range(count):
        all_circle[i].next_step()

        all_circle[i].check_wall(width, height)

        all_circle[i].execute_friction_to_boost(k)
        all_circle[i].change_move()
        for j in range(i+1, count):
            all_circle[i].collision(all_circle[j])
        all_circle[i].change_color_from_move()
        all_circle[i].draw(screen)

    pygame.display.flip()
