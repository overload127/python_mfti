#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import my_stack


def check_str(str_main):
    str_unic = '/'
    str_left = '{['
    str_right = '}]'
    for ch in str_main:
        if ch not in str_left and ch not in str_right and ch not in str_unic:
            continue

        if ch in str_unic:
            ch_back = my_stack.pop()
            if ch_back in str_unic:
                if ch_back != ch:
                    return False
            else:
                my_stack.push(ch_back)
                my_stack.push(ch)

        elif ch in str_right:
            ch_back = my_stack.pop()
            if (ch == '}' and ch_back != '{' or
                ch == ']' and ch_back != '['):
                return False
        else:
            my_stack.push(ch)
    
    if my_stack.is_empty():
        return True

    return False


if __name__ == "__main__":
    my_stack.clear()

    str_main = '{{[[///]]}}'

    print(check_str(str_main))
