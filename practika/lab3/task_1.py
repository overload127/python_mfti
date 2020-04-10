#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from graph import *


x1 = 250
y1 = 250
r1 = 100
penColor(0, 0, 0)
brushColor("yellow")
circle(x1, y1, r1)

x2 = x1 - r1 * 0.4
y2 = y1 - r1 * 0.3
r2 = r1 * 0.2
brushColor("red")
circle(x2, y2, r2)

x3 = x1 + r1 * 0.4
y3 = y2
r3 = r1 * 0.18
circle(x3, y3, r3)

brushColor("black")
circle(x2, y2, r2*0.4)
circle(x3, y3, r2*0.4)

rectangle(x1-r1*0.55, y1+r1*0.49, x1+r1*0.55, y1+r1*0.49+r1*0.15)

x4 = x1 - r1 * 1.02
y4 = y1 - r1 * 0.9
wx4 = r1 * 0.05
wy4 = r1 * 0.09

polygon([(x4, y4), (x4-wx4, y4+wy4),
         (x4+r1*0.9-wx4, y4+r1*0.39+wy4), (x4+r1*0.9, y4+r1*0.39),
         (x4, y4)])


x5 = x1 + r1 * 0.98
y5 = y1 - r1 * 0.7
wx5 = r1 * 0.01
wy5 = r1 * 0.09

polygon([(x5, y5), (x5+wx5, y5+wy5),
         (x5-r1*0.9+wx5, y5+r1*0.2+wy5), (x5-r1*0.9, y5+r1*0.2),
         (x5, y5)])

run()
