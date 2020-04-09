#!/usr/bin/python

import sys
import json
from time import sleep

import pygame
from pygame import *

import game

with open(sys.argv[1]) as f:
    data = json.load(f)

pygame.init()

TANK_COLORS = [(50,150,0), (150,50,20)]

font = pygame.font.SysFont("Arial", 20)

def handle_events():
    sleep(1 / 60.)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit(0)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_ESCAPE:
                sys.exit(0)


def draw_frame(surf, frame):
    surf.fill((0, 0, 0))
    ty = 10
    win = len(frame['tanks']) == 1
    for t in frame['tanks']:
        s = t['name'] + ' ' + str(t['health'])
        if win:
            s += ' WIN!!!'
        name = font.render(s, True, TANK_COLORS[t['ind']])
        screen.blit(name, (10, ty))
        ty += 23
        pygame.draw.circle(surf, TANK_COLORS[t['ind']], list(map(int,t['pos'])), game.TANK_RADIUS)

    for b in frame['bullets']:
        pygame.draw.circle(surf, (200, 200, 200), list(map(int,b['pos'])), game.BULLET_RADIUS)

    for b in frame['bonuses']:
        pygame.draw.circle(surf, (200, 100, 100), list(map(int,b['pos'])), game.BONUS_RADIUS)


screen = pygame.display.set_mode((game.WIDTH, game.HEIGHT))

for f in data:
    handle_events()
    draw_frame(screen, f)
    pygame.display.update()

while 1:
    handle_events()
