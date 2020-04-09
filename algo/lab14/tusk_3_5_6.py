#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pprint
import math
import my_stack

stack_1 = []
stack_2 = []


def get_prioryty(ch):
    if ch in '+-':
        return 1
    elif ch in '*/':
        return 2
    elif ch in '^':
        return 3
    else:
        print('ERROR!!!')
        exit(3)


def take_token(str_to_token):
    mas = []
    str_tmp = ''
    for ch in str_to_token:
        if ch.isdigit():
            str_tmp = ''.join((str_tmp, ch))
        else:
            if len(str_tmp) != 0:
                mas.append(str_tmp)
                str_tmp = ''
            mas.append(ch)
    if len(str_tmp) != 0:
        mas.append(str_tmp)

    return mas


def polska9_1(mas_token):
    mas_end = []
    for ch_next in mas_token:
        if ch_next == '(':
            my_stack.push((ch_next, 0))
        elif ch_next == ')': # переделать обработку
            ch_old = my_stack.pop()
            while ch_old[0] != '(':
                mas_end.append(ch_old[0])
                ch_old = my_stack.pop()
        elif ch_next.isdigit():
            mas_end.append(ch_next)
        else: # Иначе это функция - действие
            prior = get_prioryty(ch_next)
            if my_stack.is_empty():
                my_stack.push((ch_next, prior))
            else:
                ch_old = my_stack.pop()
                if ch_old[1] >= prior:
                    mas_end.append(ch_old[0])
                else: 
                    my_stack.push(ch_old)
                my_stack.push((ch_next, prior))
    while not my_stack.is_empty():
        ch_old = my_stack.pop()
        mas_end.append(ch_old[0])
        
    return mas_end


def polska9_2(mas_token):
    mas_end = []
    for ch_next in mas_token[::-1]:
        if ch_next == ')':
            my_stack.push((ch_next, 0))
        elif ch_next == '(': # переделать обработку
            ch_old = my_stack.pop()
            while ch_old[0] != ')':
                mas_end.append(ch_old[0])
                ch_old = my_stack.pop()
        elif ch_next.isdigit():
            mas_end.append(ch_next)
        else: # Иначе это функция - действие
            prior = get_prioryty(ch_next)
            if my_stack.is_empty():
                my_stack.push((ch_next, prior))
            else:
                ch_old = my_stack.pop()
                if ch_old[1] >= prior:
                    mas_end.append(ch_old[0])
                else: 
                    my_stack.push(ch_old)
                my_stack.push((ch_next, prior))
    while not my_stack.is_empty():
        ch_old = my_stack.pop()
        mas_end.append(ch_old[0])
        
    return mas_end[::-1]


if __name__ == "__main__":
    # начало программы
    str_main = ["(2-3)*(12-10)+4/2", "(3+4*(2-1))/5", "3+4*2/(1-5)^2"]
    for line in str_main:
        mas_token = take_token(line)

        tmp = polska9_1(mas_token)
        for ch in tmp:
            print(ch, end='')
        print()
        
        tmp = polska9_2(mas_token)
        for ch in tmp:
            print(ch, end='')
        print()
