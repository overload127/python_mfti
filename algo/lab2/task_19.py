#!/usr/bin/python3

from pyrob.api import *


@task
def task_8_29():
    left = True
    right = True
    while True:
        if left:
            if not wall_is_on_the_left():
                move_left()
            else:
                left = False
        else:
            if not wall_is_on_the_right():
                move_right()
            else:
                right = False
                break
        if not wall_is_above():
            move_up()
            break

    if left or right:
        while not wall_is_above():
            move_up()

        while not wall_is_on_the_left():
            move_left()
        


if __name__ == '__main__':
    run_tasks()
