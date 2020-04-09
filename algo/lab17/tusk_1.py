#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import game
g_move_up = True


def move(me, enemies, bullets, bonuses, m):
    global g_move_up   
    if me['pos'][1] < game.TANK_RADIUS+game.TANK_SPEED+1 and g_move_up:
        g_move_up = False
    elif me['pos'][1] > game.HEIGHT-game.TANK_RADIUS-game.TANK_SPEED-1 and not g_move_up:
        g_move_up = True

    if g_move_up:
        m.up()
    else:
        m.down()