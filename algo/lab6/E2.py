#!/usr/bin/env python3

n = int(input())
if n < 1000:
    all_date = [[] for i in range(n)]
    line = input()
    while line != '#':
        student_id, value = [int(i) for i in line.split()]
        all_date[student_id].append(value)
        line = input()

    all_date.sort(key=lambda x: sum(x), reverse=True)

    for i in range(n):
        all_date[i].sort(reverse=True)
        for ch in all_date[i]:
            print(ch, end=' ')
else:
    a = list(range(n+1))
    a[1] = 0
    lst = []

    i = 2
    while i <= n:
        if a[i] != 0:
            lst.append(str(a[i]))

            for j in range(i, n+1, i):
                a[j] = 0
        i += 1
    print(' '.join(lst))