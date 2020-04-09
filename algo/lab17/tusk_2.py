#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import game
import math
import sys
_X, _Y = 0, 1
old_pos_enemy = []
first_call = True

def get_length_from_coord(pos_1, pos_2):
    putch_xy = pos_1[_X] - pos_2[_X], pos_1[_Y] - pos_2[_Y]
    return math.sqrt(putch_xy[_X]**2 + putch_xy[_Y]**2) 


def get_steps_from_coord(enemy_xy, bullet_xy):
    return get_length_from_coord(enemy_xy, bullet_xy) // game.BULLET_SPEED


def get_xy_object_from_steps(pos, direct, steps):
    return [pos[_X]+direct[_X]*steps, pos[_Y]+direct[_Y]*steps]


def move(me, enemies, bullets, bonuses, m):
    global old_pos_enemy
    global first_call
    if first_call:
        old_pos_enemy = enemies[0]['pos'][:]
        first_call = False
        sys.stderr.write('First')

    dir_enemy = [enemies[0]['pos'][_X]-old_pos_enemy[_X], enemies[0]['pos'][_Y]-old_pos_enemy[_Y]]
    len_dir = get_length_from_coord([0, 0], dir_enemy)
    if len_dir == 0:
        len_dir = 1
    dir_enemy = [dir_enemy[_X]/len_dir*5, dir_enemy[_Y]/len_dir*5]

    sys.stderr.write(str(enemies))
    target_xy = enemies[0]['pos'][:]
    length_target_to_enemi = game.TANK_RADIUS + 1
    next_pos = enemies[0]['pos'][:]
    
    while length_target_to_enemi > game.TANK_RADIUS:
        target_xy = next_pos[:]
        count_steps = get_steps_from_coord(target_xy, me['pos'])
        next_pos = get_xy_object_from_steps(enemies[0]['pos'], dir_enemy, count_steps)
        sys.stderr.write('next_pos = ' + str(next_pos)+'\n')

        if next_pos[_Y] < game.TANK_RADIUS:
            next_pos[_Y] = game.TANK_RADIUS - next_pos[_Y]
        elif next_pos[_Y] > game.HEIGHT-game.TANK_RADIUS:
            next_pos[_Y] = game.HEIGHT-game.TANK_RADIUS - (next_pos[_Y]-(game.HEIGHT-game.TANK_RADIUS))
  
        if next_pos[_X] < game.TANK_RADIUS:
            next_pos[_X] = game.TANK_RADIUS - next_pos[_X]
        elif next_pos[_X] > game.WIDTH-game.TANK_RADIUS:
            next_pos[_X] = game.WIDTH-game.TANK_RADIUS - (next_pos[_X]-(game.WIDTH-game.TANK_RADIUS))

        length_target_to_enemi = get_length_from_coord(next_pos, target_xy)
        
        sys.stderr.write('target_xy = ' + str(target_xy)+'\n')
        sys.stderr.write('count_steps = ' + str(count_steps)+'\n')
        sys.stderr.write('next_pos = ' + str(next_pos)+'\n')
        sys.stderr.write('length_target_to_enemi = ' + str(length_target_to_enemi)+'\n')
        sys.stderr.write(':::::::::::::::::::::::::::::::::::::::::' + '\n')
    
    old_pos_enemy = enemies[0]['pos'][:]
    
    m.shot(target_xy[_X], target_xy[_Y])