#!/usr/bin/env python3
# -*- coding: utf-8 -*-
from tusk_1 import Vector

l = 100
mas = Vector(0, 0)
for i in range(l-150, l-50, 1):
    mas = mas + Vector(i**2, (2*i-50)**2)

vec_all_mas = Vector(mas.x // l, mas.y // l)
print(vec_all_mas)