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



K = int(input())
mas = input().split()

if K == 0:
    print(0)
else:
    for i in range(K):
        mas[i] = int(mas[i])

    merge_sort(mas)
    p = K//2 + 1

    res = 0 

    for i in range(p):
        if mas[i] > 0:
            res += mas[i]//2+1

    print(res)