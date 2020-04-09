#!/usr/bin/python3

y2 = int(input(""))

if y2 <= 10000:
    qvadrat = 1
    for i in range(1, y2//2):
        qvadrat = i * i
        if qvadrat > y2:
            break
        print(qvadrat, end=' ')
        
