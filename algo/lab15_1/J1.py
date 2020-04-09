#!/usr/bin/env python3
# -*- coding: utf-8 -*-
my_stack = []


znaki = {'I':1,'V':5,'X':10,'L':50,'C':100,'D':500,'M':1000}

stroka = input()
#stroka = 'XCIV'
end = []

for ch in stroka:
    ch_i = znaki[ch]
    if len(my_stack) == 0:
        my_stack.append((ch_i, 1))
    elif my_stack[-1][0] < ch_i:
        end.append(ch_i - my_stack.pop()[0])
    elif my_stack[-1][0] == ch_i:
        if my_stack[-1][1] == 1:
            my_stack.append((ch_i, 2))
        else:
            end.append(ch_i + my_stack.pop()[0] + my_stack.pop()[0])
    elif my_stack[-1][0] > ch_i:
        tmp = my_stack[-1]
        x = 0
        for i in range(tmp[1]):
            tmp_2 = my_stack.pop()
            x += tmp_2[0]
        end.append(x)
        my_stack.append((ch_i, 1))
    else:
        priint('ERROR!!!')
        exit(3)
if len(my_stack) > 0:
    tmp = my_stack[-1]
    x = 0
    for i in range(tmp[1]):
        tmp_2 = my_stack.pop()
        x += tmp_2[0]
    end.append(x)
print(sum(end))