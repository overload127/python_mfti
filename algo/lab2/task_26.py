#!/usr/bin/python3

from pyrob.api import *


@task(delay=0.02)
def task_2_4():
    move_right()
    move_down()
 
    CrossRight(10)
    move_down(4)
    CrossLeft(10)
    move_down(4)
    CrossRight(10)
    move_down(4)
    CrossLeft(10)
    move_down(4)
    CrossRight(10)
    
    move_left(37)
    move_up()

def CrossLeft(step=1):
    Cross()
    while step > 1:
        move_left(4)
        Cross()
        step -= 1

def CrossRight(step=1):
    Cross()
    while step > 1:
        move_right(4)
        Cross()
        step -= 1

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
