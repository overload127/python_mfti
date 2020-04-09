#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_28():
    left = True
    while True:
        if left:
            if not wall_is_on_the_left():
                move_left()
            else:
                left = False
        else:
            move_right()

        if not wall_is_above():
            move_up()
            break

    while not wall_is_above():
        move_up()

    while not wall_is_on_the_left():
        move_left()


if __name__ == '__main__':
    run_tasks()
