#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pprint

def  calculate_min_cost(n, price):
    prev = [0]*(n+1)
    C = [0]*(n+1)
    C[0]=price[0]
    C[1]=price[1]
    prev[1]=0
    C[2]=price[2]
    prev[2]=0

    for i in range(3,n+1):
        C[i] = min(C[i-1], C[i-2]) + price[i]
        if C[i-1] < C[i-2]:
            prev[i] = i-1
            C[i] = C[i-1] + price[i]
        else:
            prev[i] = i-2
            C[i] = C[i-2] + price[i]

    path = []
    i = n
    while i > 0:
        path.append(i)
        i = prev[i]
    path.append(prev[0])


    return C[n], path

N=55
price =[0]+[1]*(N)


print(calculate_min_cost(N, price))