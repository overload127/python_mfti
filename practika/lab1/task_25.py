#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_2():
    move_right()
    move_down(2)
    fill_krest()
    for i in range(4):
        move_right(3)
        fill_krest()
    
    move_left(2)
    move_up()


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


if __name__ == '__main__':
    run_tasks()
