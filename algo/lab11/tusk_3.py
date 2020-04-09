#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pprint

def  calculate_min_cost(n, price):
    C = [0]*(n+1)
    C[0]=price[0]
    C[1]=price[1]
    C[2]=price[2]

    for i in range(3,n+1):
        C[i] = min(C[i-1], C[i-2]) + price[i]
    return C[n]

N=55
price =[0]+[1]*(N)


print(calculate_min_cost(N, price))