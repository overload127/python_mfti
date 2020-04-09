#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_10():
    chek_wall_up_and_down()
    while not wall_is_on_the_right():
        move_right()
        chek_wall_up_and_down()

def chek_wall_up_and_down():
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
