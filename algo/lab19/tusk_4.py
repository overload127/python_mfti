#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pygame
import sys
import math


class Vector:

    def __init__(self, x=0, y=0):
        self.x = x
        self.y = y

    def __add__(self, other):
        return Vector(self.x + other.x, self.y + other.y)

    def __sub__(self, other):
        return Vector(self.x - other.x, self.y - other.y)

    def __mul__(self, i):
        return Vector(self.x * i, self.y * i)

    def __rmul__(self, i):
        return Vector(self.x * i, self.y * i)

    def __neg__(self):
        return Vector(-self.x, -self.y)

    def __str__(self):
        return '{} {}'.format(self.x, self.y)

    def intpair(self):
        return (int(self.x), int(self.y))

    def get_length(self):
        return math.hypot(self.x, self.y)


class Ball():

    def __init__(self, radius, x, y, xs, ys):
        self.radius = radius
        self.point = Vector(x, y)
        self.speed = Vector(xs, ys)
        self.rgb = (111, 222, 111)

    def update(self, width, height):
        self.point = self.point + self.speed

        if self.point.x >= width - self.radius:
            self.speed = Vector(-abs(self.speed.x), self.speed.y)
            self.point = Vector((width - self.radius) -
                                (self.point.x - (width - self.radius)),
                                self.point.y)
        elif self.point.x <= self.radius:
            self.speed = Vector(abs(self.speed.x), self.speed.y)
            self.point = Vector(self.radius + self.radius -
                                self.point.x, self.point.y)
        if self.point.y >= height - self.radius:
            self.speed = Vector(self.speed.x, -abs(self.speed.y))
            self.point = Vector(self.point.x, (height - self.radius) -
                                (self.point.y - (height - self.radius)))
        elif self.point.y <= self.radius:
            self.speed = Vector(self.speed.x, abs(self.speed.y))
            self.point = Vector(self.point.x, self.radius + self.radius -
                                self.point.y)

    def render(self, canvas):
        pygame.draw.circle(canvas, self.rgb,
                           (self.point.intpair()),
                           self.radius)

    def next_color(self):
        r = self.rgb[0] + 25
        g = self.rgb[1] - 12
        b = self.rgb[2] + 15
        if r > 255:
            r -= 255
        if g < 0:
            g += 255
        if b > 255:
            b -= 255
        self.rgb = (r, g, b)


def main():
    width = 500
    height = 500
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('YAHOOOO')
    clock = pygame.time.Clock()
    balls = []

    while True:
        dt = clock.tick(50) / 1000.0
        count = len(balls)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    # left
                    b = Ball(20, event.pos[0], event.pos[1], 1, 1)
                    balls.append(b)
                    count += 1
                elif event.button == 3:
                    # rigth
                    for i in range(count):
                        mouse_pos = Vector(event.pos[0], event.pos[1])
                        length = (balls[i].point - mouse_pos).get_length()
                        if length < balls[i].radius:
                            balls[i].next_color()

        screen.fill((0, 0, 0))

        for i in range(count):
            balls[i].update(width, height)
            balls[i].render(screen)
        pygame.display.flip()


if __name__ == "__main__":
    main()
