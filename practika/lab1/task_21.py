#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    flag = True

    for i in range(1, 14):
        if flag:
            move_down()
            move_right()
            for j in range(i):
                fill_cell()
                move_right()

            flag = False

        else:
            move_down()
            for j in range(i):
                fill_cell()
                move_left()
            flag = True

    move_down()
    move_left(13)


if __name__ == '__main__':
    run_tasks()
