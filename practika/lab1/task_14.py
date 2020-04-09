#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_11():
    cur_filled_up()
    cur_filled_down()
    cur_filled()
    while not wall_is_on_the_right():
        move_right()
        cur_filled_up()
        cur_filled_down()
        cur_filled()


def cur_filled_up():
    if not wall_is_above():
        move_up()
        fill_cell()
        move_down()


def cur_filled_down():
    if not wall_is_beneath():
        move_down()
        fill_cell()
        move_up()


def cur_filled():
    if wall_is_beneath() and wall_is_above():
        fill_cell()

if __name__ == '__main__':
    run_tasks()
