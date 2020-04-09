#!/usr/bin/env python3
# -*- coding: utf-8 -*-


line = [int(i) for i in input().split()]
rad2 = (line[0]**2 + line[1]**2)**(1/2)
if rad2 > line[2]:
    print("NO")
else:
    print("YES")