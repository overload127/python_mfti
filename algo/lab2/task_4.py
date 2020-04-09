#!/usr/bin/python3

from pyrob.api import *


@task
def task_3_3():
    for fun in chek_wall:
        if fun[0]():
            # wall
        else:
            # not wall
            fun[1]()
            break

chek_wall = ((wall_is_above, move_up),
             (wall_is_beneath, move_down),
             (wall_is_on_the_left, move_left),
             (wall_is_on_the_right, move_right))

if __name__ == '__main__':
    run_tasks()
