#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_3():
    move_right()
    y = 6
    while y > 0:
        FillAndRight(26)
        FillAndDown(1)
        FillAndLeft(26)
        FillAndDown(1)
        y -= 1
    

def FillAndUp(step=0):
    while step > 0:
        fill_cell()
        move_up()
        step -= 1

def FillAndDown(step=0):
    while step > 0:
        fill_cell()
        move_down()
        step -= 1

def FillAndLeft(step=0):
    while step > 0:
        fill_cell()
        move_left()
        step -= 1

def FillAndRight(step=0):
    while step > 0:
        fill_cell()
        move_right()
        step -= 1


if __name__ == '__main__':
    run_tasks()
