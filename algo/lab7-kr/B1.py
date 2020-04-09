#!/usr/bin/env python3
# -*- coding: utf-8 -*-

import math

A, B, C = 0,1,2

side = []

i = 0
try:
    while i < 3:
        side.append(int(input()))
        i += 1
except ValueError:
    exit()

if side[A] + side[B] <= side[C]:
    print("impossible")
    exit()
elif side[B] + side[C] <= side[A]:
    print("impossible")
    exit()
elif side[C] + side[A] <= side[B]:
    print("impossible")
    exit()

AB,BC,CA = 0,1,2

angel=[0,0,0]

angel[AB] = math.degrees(math.acos((side[A]**2 + side[B]**2 - side[C]**2)/(2*side[A]*side[B])))
angel[BC] = math.degrees(math.acos((side[B]**2 + side[C]**2 - side[A]**2)/(2*side[B]*side[C])))
angel[CA] = math.degrees(math.acos((side[C]**2 + side[A]**2 - side[B]**2)/(2*side[C]*side[A])))

max_angel = max(angel)

if max_angel > 90:
    print("obtuse")
elif max_angel < 90:
    print("acute")
else:
    print("right")
