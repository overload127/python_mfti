#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_4():
    cur_filled()
    while not wall_is_on_the_right():
        move_right()
        cur_filled()


def cur_filled():
    if wall_is_above() and wall_is_beneath():
        fill_cell()


if __name__ == '__main__':
    run_tasks()
