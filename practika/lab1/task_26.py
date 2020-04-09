#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.02)
def task_2_4():

    move_right()
    move_down()
    fill_krest()
    move_right()

    while True:

        while not wall_is_on_the_right():
            move_right(3)
            fill_krest()
            move_right()

        if not go_down():
            break

        move_left()
        fill_krest()
        move_left()

        while not wall_is_on_the_left():
            move_left(3)
            fill_krest()
            move_left()

        if not go_down():
            break

        move_right()
        fill_krest()
        move_right()

    move_up(2)
    while not wall_is_on_the_left():
        move_left()


def fill_krest():
    fill_cell()
    move_down()
    fill_cell()
    move_up(2)
    fill_cell()
    move_down()
    move_left()
    fill_cell()
    move_right(2)
    fill_cell()
    move_left()


def go_down():
    for _ in range(4):
        if not wall_is_beneath():
            move_down()
        else:
            return False

    return True


if __name__ == '__main__':
    run_tasks()
