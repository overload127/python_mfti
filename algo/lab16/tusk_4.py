#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import string


all_text = ''
count_dict = {}

with open('LICENSE', 'r') as f1:
    all_text = f1.read()

for i in string.punctuation:
    all_text = all_text.replace(i, ' ')

all_text = all_text.lower()
for str_1 in all_text.split():
    c = count_dict.get(str_1, 0)
    count_dict[str_1] = c + 1

get_x = len(count_dict) if len(count_dict) < 10 else 10

all_items = list(count_dict.items())

all_items.sort(key=lambda x: x[1], reverse=True)

for i in range(get_x):
    print(all_items[i][0])