#!/usr/bin/env python3
# -*- coding: utf-8 -*-


def merge(A:list, B:list):
    C=[0]*(len(A)+len(B))
    i=k=n=0
    while i < len(A) and k < len(B):
        if A[i] <= B[k]:
            C[n] = A[i]
            i += 1
            n += 1
        else:
            C[n] = B[k]
            k += 1
            n += 1

    while i < len(A):
        C[n] = A[i]
        i += 1
        n += 1

    while k < len(B):
        C[n] = B[k]
        k += 1
        n += 1

    return C


def merge_sort(A):
    if len(A) <= 1:
        return
    middle= len(A)//2
    L = [A[i] for i in range(0,middle)]
    R = [A[i] for i in range(middle,len(A))]

    merge_sort(L)
    merge_sort(R)
    C = merge(L,R)
    for i in  range(len(A)):
        A[i] = C[i]



mas_main = input().split()
k = len(mas_main)
mas_chet = []
mas_ne_chet = []


for i in range(k):
    mas_main[i] = int(mas_main[i])
    if mas_main[i] % 2:
        mas_ne_chet.append(mas_main[i])
    else:
        mas_chet.append(mas_main[i])

merge_sort(mas_chet)
merge_sort(mas_ne_chet)

i=n=0
if len(mas_chet) > 0:
    print(mas_chet[i], end='')
    i = 1
while i < len(mas_chet):
    print(' ', end=str(mas_chet[i]))
    i += 1

if i == 0 and len(mas_ne_chet) > 0:
    print(mas_ne_chet[n], end='')
    n = 1
while n < len(mas_ne_chet):
    print(' ', end=str(mas_ne_chet[n]))
    n += 1
