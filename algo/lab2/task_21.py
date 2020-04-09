#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.05)
def task_4_11():
    move_down()
    move_right()
    lest(13)

def lest(step = 1):
    i = 0
    k = 0
    while i < step:
        if k > 0:
            fill_cell()
            while k > 0:
                move_left()
                fill_cell()
                k -= 1
        else:
            while k <= i:
                fill_cell()
                move_right()
                k += 1
        move_down()
        i += 1
    move_left(k)
        
if __name__ == '__main__':
    run_tasks()
