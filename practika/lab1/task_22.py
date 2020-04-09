#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.01)
def task_5_10():
    flag = True
    finish = True
    while not wall_is_beneath():

        if flag:
            while not wall_is_on_the_right():
                fill_cell()
                move_right()

        else:
            while not wall_is_on_the_left():
                fill_cell()
                move_left()

        fill_cell()
        move_down()
        flag = not flag

    if flag:
        while not wall_is_on_the_right():
            fill_cell()
            move_right()

    else:
        while not wall_is_on_the_left():
            fill_cell()
            move_left()

    fill_cell()

    while not wall_is_on_the_left():
        move_left()


if __name__ == '__main__':
    run_tasks()
