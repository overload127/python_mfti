#!/usr/bin/env python3
# -*- coding: utf-8 -*-
vhod = [int(i,16) for i in input().split()]

res = hex(int(bin(vhod[0]^vhod[1]),2))
print(res[2:])
