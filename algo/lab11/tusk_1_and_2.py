#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pprint

n=55

F = [-1]*(n+1)
F[0]=0
F[1]=1
F[2]=1
F[3]=1

for i in range(4,n):
    F[i]=F[i-1]+F[i-2]+F[i-3]

pprint.pprint([(i, F[i]) for i in range(n+1)])

F = [-1]*(n+1)
F[0]=0
F[1]=1
F[2]=1
F[3]=2

for i in range(4,n):
    F[i]=F[i-1]+F[i-2]
    if i % 3:
        F[i]=F[i-1]+F[i-2]
    else:
        F[i]=F[i-1]+F[i-2]+F[i//3]

pprint.pprint([(i, F[i]) for i in range(n+1)])