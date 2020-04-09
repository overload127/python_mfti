#!/usr/bin/env python3
# -*- coding: utf-8 -*-


A = set('bqlpzlkwehrlulsdhfliuywemrlkjhsdlfjhlzxcovt')
B = set('zmxcvnboaiyerjhbziuxdytvasenbriutsdvinjhgik')
for x in A:
    if x not in B:
        print(x)