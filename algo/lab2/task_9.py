#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_2():
    if not wall_is_above():
        fill_cell()
    while not wall_is_on_the_right():
        move_right()
        if not wall_is_above():
            fill_cell()


if __name__ == '__main__':
    run_tasks()
