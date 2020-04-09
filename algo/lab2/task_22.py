#!/usr/bin/python3

from pyrob.api import *


@task
def task_5_10():
    right = True
    while True:
        fill_cell()
        if right:
            MoveRightFill()
        else:
            MoveLeftFill()
        if not wall_is_beneath():
            move_down()
        else:
            break
        right = not right

    GoToLeftWall() 
            

def MoveRightFill():
    while not wall_is_on_the_right():
        move_right()
        fill_cell()

def MoveLeftFill():
    while not wall_is_on_the_left():
        move_left()
        fill_cell()

def GoToLeftWall():
    while not wall_is_on_the_left():
        move_left()
        


if __name__ == '__main__':
    run_tasks()
