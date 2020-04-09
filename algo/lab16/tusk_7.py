#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Входные данные испорчены. Текст программы примерный

data_base = {}
with open('tusk_7_en-ru_moe.txt', 'r', encoding='utf8') as f1:
    for line in f1.readlines():
        left, right = tuple(line.split('\t-\t'))
        right = right.strip().split(', ')
        left = left.split(', ')
        for word in right:
            if word not in data_base:
                data_base[word] = []
            data_base[word].extend(left)


list_data_base = list(data_base.items())
for line in list_data_base:
    line[1].sort()

list_data_base.sort(key = lambda line: line[0])

with open('tusk_7_ru-en_moe.txt', 'w', encoding='utf8') as f1:
    for line in list_data_base:
        f1.write("{0}\t-\t{1}\n".format(line[0],', '.join(line[1])))