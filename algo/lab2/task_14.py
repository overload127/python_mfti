#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_11():
    chek_wall_up_center_down()
    while not wall_is_on_the_right():
        move_right()
        chek_wall_up_center_down()

def chek_wall_up_center_down():
    if wall_is_above() and wall_is_beneath():
        fill_cell()
    else:
        if not wall_is_above():
            field_up()
        if not wall_is_beneath():
            field_down()

def field_up():
    move_up()
    fill_cell()
    move_down()

def field_down():
    move_down()
    fill_cell()
    move_up()


if __name__ == '__main__':
    run_tasks()
