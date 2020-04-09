#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import string


all_translate = {}
with open('tusk_5_en-ru.txt', 'r', encoding='utf8') as f1:
    for line in f1.readlines():
        left, right = tuple(line.split('\t-\t'))
        right = right.strip()
        all_translate[left] = right

all_text = ''
with open('tusk_5_input.txt', 'r', encoding='utf8') as f1:
    all_text = f1.read()

all_text_in_list = []
word = []
for ch in all_text:
    if ch == ' ':
        if len(word) > 0:
            word_str = (''.join(word)).lower()
            all_text_in_list.append(all_translate.get(word_str, word_str))
            word = []
        all_text_in_list.append(ch)
    elif ch in string.punctuation:
        if len(word) > 0:
            word_str = (''.join(word)).lower()
            all_text_in_list.append(all_translate.get(word_str, word_str))
            word = []
        all_text_in_list.append(ch)
    else:
        word.append(ch)
if len(word) > 0:
    word_str = (''.join(word)).lower()
    all_text_in_list.append(all_translate.get(word_str, word_str))
    word = []

print(''.join(all_text_in_list))