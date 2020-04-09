#!/usr/bin/env python3
# -*- coding: utf-8 -*-
import pprint

all_prefix = []

def gen_number1(coins: list, M: int, prefix=None):
    prefix = prefix or []
    if M == 0:
        tmp_p = sorted(prefix)
        if tmp_p not in all_prefix:
            all_prefix.append(tmp_p)
        return
    elif M < 0:
        return
    for digit in coins:
        prefix.append(digit)
        gen_number1(coins, M-digit, prefix)
        prefix.pop()


def make_exchange2(money, coins):
    mas = [0] * (max(money, max(coins))+1)
    all_combo = [[] for i in range(max(money, max(coins))+1)]
    for i in coins:
        mas[i] = 1
        all_combo[i].append([i])

    for i in range(1, money+1):
        tmp = []
        for j in coins:
            if i - j >= 0:
                mas[i] = mas[i] + mas[i-j]
                for line in all_combo[i-j]:
                    tmp = line[:]
                    tmp.append(j)
                    tmp.sort()
                    if tmp not in all_combo[i]:
                        all_combo[i].append(tmp)
    
    pprint.pprint(all_combo)

    return len(all_combo[money])


def make_exchange3(money, coins):
    mas = [0] * (max(money, max(coins))+1)

    for i in coins:
        mas[i] = 1

    for i in range(1, money+1):
        for j in coins:
            if i - j >= 0:
                mas[i] = mas[i] + mas[i-j]

    return mas[money]


def make_exchange4(money, coins, first=None):
    if first is None:
        first = 0
        coins.sort()
    if money == 0:
        return 1
    if money < 0 or len(coins) == 0:
        return 0
    else:
        m = max(coins)
        return make_exchange4(money-m, coins, first) + make_exchange4(money, coins[:-1], first)

    

money = int(input())
coins = [int(i) for i in input().split()]
#money = 10
#coins = [2,3,5]

#gen_number1(coins, money)
print(make_exchange4(money, coins))

# print(make_exchange(money, coins))