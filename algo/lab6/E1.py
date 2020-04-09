#!/usr/bin/env python3

lst = []
ch_lst = []

end = False
i = None

N = input()
if N == '#':
    exit(0)
elif int(N) <= 0:
    exit(0)

while not end:
    try:
        stroka = input()
    except EOFError:
        end = True
        break 
    if stroka == '#' or stroka == '/n' or stroka == ' ':
        end = True
        break
    ch_lst = stroka.split()

    find = False
    if i == None:
        i = 0
        lst.append(list())
        lst[i].append(list())
        lst[i][0].append(int(ch_lst[1]))
        lst[i].append(int(ch_lst[1]))
        lst[i].append(int(ch_lst[0]))
        continue
    else:
        for j in range(len(lst)):
            if lst[j][2] == int(ch_lst[0]):
                find = True
                break
    if find:
        lst[j][0].append(int(ch_lst[1]))
        lst[j][1] += int(ch_lst[1])
    else:
        i += 1
        lst.append(list())
        lst[i].append(list())
        lst[i][0].append(int(ch_lst[1]))
        lst[i].append(int(ch_lst[1]))
        lst[i].append(int(ch_lst[0]))

if len(lst) <= 0:
    exit(0)

lst.sort(key=lambda x: x[2])

lst.sort(key=lambda x: x[1] ,reverse=True)
for i in range(len(lst)):
    lst[i][0].sort(reverse=True)

for line_in in lst:
    for line in line_in[0]:
        print(line, end=' ')
