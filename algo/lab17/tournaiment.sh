#!/bin/bash

dirin=$1
dirout=$2
players='bot1 bot2 bot3 krohalev patritskya kozlova venskaya scherbakov mishina lomonosov abdrakhimov'

for first in $players; do
  mkdir -p $dirout/$first
  for second in $players; do
    echo $first ' ' $second
    ./battle.py $dirin/$first/bot.py $dirin/$second/bot.py 5000 2>$dirout/$first/to_$second.res >$dirout/$first/to_$second.json
  done
done

./genhtml.py $dirout 'https://senya.github.io/tanks-results/res' $players > $dirout/../index.html
