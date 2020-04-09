#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_9_3():
    width = GedtWidth()
    
    i = 0
    k = 0
   
    while True:
        MoveLeftToWall(k, width)
            
        if wall_is_beneath():
            break

        move_down()
        k += 1
        i = 0

        MoveRightToWall(k, width)

        if wall_is_beneath():
            break

        move_down()
        k += 1
        i = 0


def MoveRightToWall(k, width):
    i = 0
    while True:
        if i != k and i != width-k:
            fill_cell()
        i += 1

        if wall_is_on_the_right():
            break
        move_right()


def MoveLeftToWall(k, width):
    i = 0
    while True:
        if i != k and i != width-k:
            fill_cell()
        i += 1

        if wall_is_on_the_left():
            break

        move_left()


def GedtWidth():
    width = 0
    while not wall_is_on_the_right():
        width += 1
        move_right()
    return width


if __name__ == '__main__':
    run_tasks()
