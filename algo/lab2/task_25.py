#!/usr/bin/python3

from pyrob.api import *


@task
def task_2_2():
    move_right()
    move_down(2)
    Cross()

    i = 4
    while i > 0:
        move_right(4)
        Cross()
        i -= 1
    
    move_left()
    move_up()

def Cross():
    fill_cell()
    
    field_up()    
    field_down()
    field_right()
    field_left()

def field_up():
    move_up()
    fill_cell()
    move_down()

def field_down():
    move_down()
    fill_cell()
    move_up()

def field_right():
    move_right()
    fill_cell()
    move_left()

def field_left():
    move_left()
    fill_cell()
    move_right()


if __name__ == '__main__':
    run_tasks()
