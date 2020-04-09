#!/usr/bin/env python3


s = input().strip()
if len(s) == 0:
    print("NO SOLUTION")
    exit(0)
num = int(input())
if num == 0:
    print("NO SOLUTION")
    exit(0)
elif num > 0:
    print(s*num)
else:
    d = len(s)//abs(num)
    if s[:d] * abs(num) == s:
        print(s[:d])
    else:
        print("NO SOLUTION")


