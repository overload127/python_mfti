#!/usr/bin/env python3

mmax = int(input())

i = 0
ix = 0
ixx = 0
while i < mmax:
    if int(input()):
        ix += 1
    else:
        if ixx < ix:
            ixx = ix
        ix = 0
    i += 1
if ixx < ix:
    ixx = ix

print(ixx)
