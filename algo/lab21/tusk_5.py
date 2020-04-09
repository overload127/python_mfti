#!/usr/bin/env python3
# -*- coding: utf-8 -*-


data_base = {}
with open('tusk_6_input.txt', 'r', encoding='utf8') as f1:
    for line in f1.readlines():
        country, right = tuple(line.split(' : '))
        right = right.strip()
        languages = right.split()
        for lang in languages:
            if lang not in data_base:
                data_base[lang] = []
            data_base[lang].append(country)


n = int(input())
for i in range(n):
    lang = input()
    countries = data_base.get(lang, ['Нет данных'])
    if len(countries) == 1:
        print(countries[0])
    else:
        print(' '.join(countries))