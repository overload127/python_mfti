#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# Входные данные испорчены. Текст программы примерный


dict_en_ru_start = {}
dict_ru_en_start = {}


with open('tusk_8_en-ru_start_ok.txt', 'r', encoding='utf8') as f1:
    for line in f1.readlines():
        left, right = tuple(line.split('\t-\t'))
        right = right.strip().split(', ')
        # Формируем английский-русско словарь
        if left not in dict_en_ru_start:
            dict_en_ru_start[left] = set()
        for word in right:
            dict_en_ru_start[left].add(word)
        # Формируем русско-английский словарь
        for word in right:
            if word not in dict_ru_en_start:
                dict_ru_en_start[word] = set()
            dict_ru_en_start[word].add(left)


with open('tusk_8_ru-en_start_ok.txt', 'r', encoding='utf8') as f1:
    for line in f1.readlines():
        left, right = tuple(line.split('\t-\t'))
        right = right.strip().split(', ')
        # Формируем английский-русско словарь
        for word in right:
            if word not in dict_en_ru_start:
                dict_en_ru_start[word] = set()
            dict_en_ru_start[word].add(left)
        # Формируем русско-английский словарь
        if left not in dict_ru_en_start:
            dict_ru_en_start[left] = set()
        for word in right:
            dict_ru_en_start[left].add(word)


# Подготавливаем английский-русско словарь к записи
list_data_base = list(dict_en_ru_start.items())

list_data_base.sort(key = lambda line: line[0])

with open('tusk_8_en-ru_start_end.txt', 'w', encoding='utf8') as f1:
    for line in list_data_base:
        f1.write("{0}\t-\t{1}\n".format(line[0],', '.join(line[1])))


# Подготавливаем русско-английский словарь к записи
list_data_base = list(dict_ru_en_start.items())

list_data_base.sort(key = lambda line: line[0])

with open('tusk_8_ru-en_start_end.txt', 'w', encoding='utf8') as f1:
    for line in list_data_base:
        f1.write("{0}\t-\t{1}\n".format(line[0],', '.join(line[1])))