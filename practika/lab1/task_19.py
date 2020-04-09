#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_29():
    flag = False
    while not wall_is_on_the_left():
        move_left()

    if wall_is_above():
        while not wall_is_on_the_right():
            move_right()

        if not wall_is_above():
            flag = True
    else:
        flag = True

    if flag:
        while not wall_is_above():
            move_up()

        while not wall_is_on_the_left():
            move_left()


if __name__ == '__main__':
    run_tasks()
