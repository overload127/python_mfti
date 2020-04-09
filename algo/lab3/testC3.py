#!/usr/bin/python3

x1 = int(input(""))

if 0 < x1 < 100000:
    if (x1 % 4 == 0 and x1 % 100 != 0) or x1 % 400 == 0:
        print("YES")
    else:
        print("NO")
else:
    print("NO")
