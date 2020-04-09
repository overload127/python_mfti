down = True

def move(me, enemies, bullets, bonuses, m):
    global down
    if me['pos'][1] < 25:
        down = True
    elif me['pos'][1] > 575:
        down = False

    if down:
        m.down()
    else:
        m.up()

    m.shot(100, 100)
