#!/usr/bin/python3

from pyrob.api import *


@task
def task_7_5():
    i = 0
    k = 0
    move_right()
    while not wall_is_on_the_right():
        if k >= i:
            fill_cell()
            k = 0
            i += 1
        
        move_right()
        k += 1


if __name__ == '__main__':
    run_tasks()
