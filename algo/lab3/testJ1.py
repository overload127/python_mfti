#!/usr/bin/python3

i = -1
x = -1
k = 0
while x != 0:
    x = int(input())
    if i == None or i < x:
        i = x
        k = 1
        continue
    elif i == x:
        k += 1
        
    
print(k)
