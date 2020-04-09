# Tanks

Prerequisities:
```
pip install --user pygame
git clone https://github.com/senya/tanks.git
cd tanks
cp strategy.py new.py

Then, open folder `tanks` as a project in PyCharm and edit new.py - it is your strategy. You can add any number of strategy files.
```

Run battle: `./battle.py strategy1.py strategy2.py 5000 > out.json`

Show battle: `./vis.py out.json`


For cmd:

Run battle: `python battle.py strategy.py strategy.py 1000 > out.json`

Show battle: `python vis.py out.json`