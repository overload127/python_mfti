#!/usr/bin/python3

import sys
import battlelib

dirin = '/home/vova/stud_tanks/'
dirout = '/home/vova/tanks-results/res/'
prefix = 'https://senya.github.io/tanks-results/res/'
prefix = 'res/'
players = ['krohalev', 'patritskya', 'kozlova', 'venskaya', 'scherbakov', 'mishina', 'lomonosov', 'abdrakhimov']
#players = ['bot1', 'bot2', 'krohalev']

tab = [[0] * len(players) for i in players]
battles = []
index = open('/home/vova/tanks-results/index.html', 'w')

def battle(p1, p2, k):
    print(p1, ' ', p2)
    p1_p, p2_p, json = battlelib.battle(dirin + p1 + '/bot.py', dirin + p2 + '/bot.py', 5000)
    f = p1 + '_' + p2 + '-' + str(k) + '.json'
    ht = prefix + f
    f = dirout + f
    with open(f, 'w') as ff:
        print(json, file=ff)
    battles.append((p1, p1_p, p2, p2_p, ht))
    return (p1_p, p2_p)


for i, p in enumerate(players):
    for j in range(i):
        p2 = players[j]

        p1_points = 0
        p2_points = 0
        
        for k in range(5):
            p1_p, p2_p = battle(p, p2, k)
            p1_points += p1_p
            p2_points += p2_p

        for k in range(5):
            p2_p, p1_p = battle(p2, p, k)
            p1_points += p1_p
            p2_points += p2_p

        tab[i][j] = p1_points
        tab[j][i] = p2_points

index.write('<table>')
index.write('<tr><td></td>')
for p in players:
    index.write('<td>' + p + '</td>')

index.write('<td>Total</td>')

sor = []
for i, p in enumerate(players):
    index.write('<tr><td>' + p + '</td>')
    total = 0
    for j in range(len(players)):
        if i == j:
            index.write('<td></td>')
            continue

        res = tab[i][j]
        total += res
        index.write('<td>' + str(res) + '</td>')
    index.write('<td>' + str(total) + '</td></tr>')
    sor.append((p, total))

index.write('</table>')

sor.sort(key=lambda pl:-pl[1])
index.write('<table>')
for pl in sor:
    index.write('<tr><td>' + pl[0] + '</td><td>' + str(pl[1]) + '</td></tr>')
index.write('</table>')


index.write('<table>')
for b in battles:
    index.write('<tr>' + ''.join(['<td>' + str(t) + '</td>' for t in b[:-1]]) + '<td><a href="' + b[4] + '">json</td>')
index.write('</table>')

index.close()
