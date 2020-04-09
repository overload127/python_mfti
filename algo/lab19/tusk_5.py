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

    def get_normalized(self):
        length = self.get_length()
        if length == 0:
            return Vector(0, 0)
        return Vector(self.x / length, self.y / length)



class Ball():

    def __init__(self, radius, x, y, xs, ys, r=111, g=222, b=111):
        self.radius = radius
        self.point = Vector(x, y)
        self.speed = Vector(xs, ys)
        self.rgb = (r, g, b)

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

    def collision(self, circle):
        dx = self.point.x - circle.point.x
        dy = self.point.y - circle.point.y
        length = math.sqrt(dx**2 + dy**2)

        if length < self.radius + circle.radius:
            v1 = Vector(circle.point.x - self.point.x, circle.point.y -
                        self.point.y).get_normalized()
            v2 = -v1

            l1 = self.speed.get_length()
            l2 = circle.speed.get_length()
            self.speed = (self.speed.get_normalized() +
                         v2).get_normalized() * l1
            circle.speed = (circle.speed.get_normalized() +
                           v1).get_normalized() * l2


def main():
    width = 500
    height = 500
    pygame.init()
    screen = pygame.display.set_mode((width, height))
    pygame.display.set_caption('YAHOOOO')
    clock = pygame.time.Clock()
    balls = []
    current = -1
    ramka = Ball(22, 0, 0, 0, 0, 255, 0, 0)

    while True:
        dt = clock.tick(50) / 1000.0
        count = len(balls)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    sys.exit()
                elif event.key == pygame.K_UP:
                    if 0 <= current <= count:
                        balls[current].speed -= Vector(0, 5)
                elif event.key == pygame.K_DOWN:
                    if 0 <= current <= count:
                        balls[current].speed += Vector(0, 5)
                elif event.key == pygame.K_RIGHT:
                    if 0 <= current <= count:
                        balls[current].speed += Vector(5, 0)
                elif event.key == pygame.K_LEFT:
                    if 0 <= current <= count:
                        balls[current].speed -= Vector(5, 0)
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    # left
                    b = Ball(20, event.pos[0], event.pos[1], 1, 1)
                    balls.append(b)
                    count += 1
                elif event.button == 2:
                    # centr
                    current = -1
                    for i in range(count):
                        mouse_pos = Vector(event.pos[0], event.pos[1])
                        length = (balls[i].point - mouse_pos).get_length()
                        if length < balls[i].radius:
                            current = i
                            break
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
            for j in range(i+1, count):
                balls[i].collision(balls[j])
            if i != current:
                balls[i].render(screen)
        if 0 <= current <= count:
            ramka.point = balls[current].point
            ramka.render(screen)
            balls[current].render(screen)

        pygame.display.flip()


if __name__ == "__main__":
    main()
