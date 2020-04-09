#!/usr/bin/env python3
# -*- coding: utf-8 -*-

MASSA_CAR, HEIGHT_CAR, MASSA_PIANO, HEIGHT_PIANO, MASSA_HOLOD, HEIGHT_HOLOD, MASSA_MAX, HEIGHT_MAX = 0,1,2,3,4,5,6,7

data = []

i = 0
try:
    while i < 8:
        data.append(int(input()))
        i += 1
except ValueError:
    exit(2)

massa = data[MASSA_CAR] + data[MASSA_PIANO] + data[MASSA_HOLOD]
height = data[HEIGHT_CAR] + max(data[HEIGHT_PIANO], data[HEIGHT_HOLOD])

if height <= data[HEIGHT_MAX]:
    massa -= data[MASSA_HOLOD]
    if massa <= data[MASSA_MAX]:
        print("YES")
    else:
        print("NO")
elif massa <= data[MASSA_MAX]:
    if data[HEIGHT_PIANO] > data[HEIGHT_HOLOD]:
        height = data[HEIGHT_CAR] + data[HEIGHT_HOLOD]
    if height <= data[HEIGHT_MAX]:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
