#!/usr/bin/env python3

tr = [0] * 3
pos = 0
mx = None
mn = None
sred = 0
end = True
j = 0
i = 0
stroka = False

tr[0] = input()
lst = tr[0].split()
if len(lst) > 1:   
    for i in range(1,len(lst)):
        print(lst[i], end=' ')
    print(lst[0], end=' ')
        
else:
    mn = mx = tr[0] = int(tr[0])
    j = i = 1
    sred += tr[0]
    while end:
        while i < 3:
            tr[i] = input()
            if str(tr[i]) == '#':
                end = False
                break
            tr[i] = int(tr[i])
            if mx < tr[i]:
                mx = tr[i]
            if mn > tr[i]:
                mn = tr[i]
            sred += tr[i]
            i += 1
            j += 1
        if end:
            pos += (tr[0] + tr[1] + tr[2]) % tr[2]
        i = 0
    sred = round(sred / j, 3)
    print(sred, mx, mn, pos)
