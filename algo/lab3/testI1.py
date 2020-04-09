#!/usr/bin/python3

i = None
x = -1
while x != 0:
    x = int(input())
    if i == None or i < x:
        i = x
print(i)
