#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_8_18():
    count = 0
    while not wall_is_on_the_right():
        count += chek_wall_up_tunnel()
        move_right()
        
    mov('ax', count)	

def chek_wall_up_tunnel():
    if not wall_is_above():
        move_up()
        count = fill_tunnel()
    else:
        count = FillCellAndCheck()
    return count

def fill_tunnel():
    count = FillCellAndCheck()
    while not wall_is_above():
        move_up()
        count += FillCellAndCheck()
    MoveDownToWall()
    return count

def FillCellAndCheck():
    if cell_is_filled():
        return 1
    else:
        fill_cell()
        return 0

def MoveDownToWall():
    while not wall_is_beneath():
        move_down()

if __name__ == '__main__':
    run_tasks()
