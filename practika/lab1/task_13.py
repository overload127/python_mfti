#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_10():
    cur_filled_up()
    cur_filled_down()
    while not wall_is_on_the_right():
        move_right()
        cur_filled_up()
        cur_filled_down()


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


if __name__ == '__main__':
    run_tasks()
