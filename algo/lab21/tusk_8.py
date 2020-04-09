#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Входные данные испорчены. Текст программы примерный


room_no_open = dict()
room_is_open = set()
all_room = []


with open('tusk_9_input.txt', 'r', encoding='utf8') as f1:
    n, m, k = [int(i) for i in f1.readline().split()]
    for line in f1.readlines():
        #all_room.append([[int(element) for element in keys.split()] for keys in f1.readline().split(',')])
        tmp1 = [[int(element) for element in keys.split()] for keys in line.split(',')]
        all_room.append(tmp1)


find_key = None
room_no_open[m] = k
while len(room_no_open) > 0:
    rooms = list(room_no_open.keys())
    for room in rooms:
        room_is_open.add(room)
        for line in all_room[room]:
            if line[0] - room_no_open[room] == n:
                find_key = line[1]
                break
            if line[0] - room_no_open[room] not in room_is_open:
                room_no_open[line[0] - room_no_open[room]] = line[1]
        if find_key:
            break
        del(room_no_open[room])
    if find_key:
        break

print(find_key)