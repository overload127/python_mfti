#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import sys
import game
i = 0



def move(me, enemies, bullets, bonuses, m):
    global i
    first_enemy = enemies[0]
    if i < 21:
        m.shot(0, 0)
    i += 1