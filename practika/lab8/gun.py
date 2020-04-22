from random import randrange as rnd, choice
import tkinter as tk
import math
import time

WIDTH = 800
HEIGTH = 600


class ball():
    gy = 2
    u = 0.05

    def __init__(self, x=40, y=450):
        """ Конструктор класса ball
        Args:
        x - начальное положение мяча по горизонтали
        y - начальное положение мяча по вертикали
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = 0
        self.vy = 0
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canv.create_oval(
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r,
                fill=self.color
        )

    def set_coords(self):
        canv.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r
        )

    def move(self):
        """Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть, обновляет значения
        self.x и self.y с учетом скоростей self.vx и self.vy, силы гравитации, действующей на мяч,
        и стен по краям окна (размер окна 800х600).
        """
        # применяем силу тяжести

        if abs(self.vy) < 1.5 and abs(self.vx) < 0.2:
            self.x = -100
            self.y = -100
            self.set_coords()
            self.dell = True
            return False
        self.vy += self.gy

        self.vx *= (1 - self.u)
        self.vy *= (1 - self.u)

        self.x += self.vx
        self.y += self.vy

        if self.x + self.r >= WIDTH-10:
            self.vx = -self.vx
            self.x = self.x - (self.x + self.r - (WIDTH-10))

        if self.y + self.r >= HEIGTH-10:
            self.vy = -self.vy
            self.y = self.y - (self.y + self.r - (HEIGTH-10))

        self.set_coords()
        return True

    def hittest(self, obj):
        """Функция проверяет сталкивалкивается ли данный обьект с целью, описываемой в обьекте obj.

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            Возвращает True в случае столкновения мяча и цели. В противном случае возвращает False.
        """
        x = self.x - obj.x
        y = self.y - obj.y
        length = (x**2 + y**2)**0.5
        if length <= self.r + obj.r:
            return True
        return False


class gun():
    def __init__(self):
        self.f2_power = 10
        self.f2_on = 0
        self.an = 1
        self.id = canv.create_line(20, 450, 50, 420, width=7)

    def fire2_start(self, event):
        self.f2_on = 1
        canv.itemconfig(self.id, fill='orange')

    def fire2_end(self, event):
        """Выстрел мячом.
        Происходит при отпускании кнопки мыши.
        Начальные значения компонент скорости мяча vx и vy зависят от положения мыши.
        """
        canv.itemconfig(self.id, fill='black')
        global balls, bullet
        bullet += 1
        new_ball = ball()
        new_ball.r += 5
        self.an = math.atan((event.y-new_ball.y) / (event.x-new_ball.x))
        new_ball.vx = self.f2_power * math.cos(self.an)
        new_ball.vy = self.f2_power * math.sin(self.an)
        balls += [new_ball]
        self.f2_on = 0
        self.f2_power = 10

    def targetting(self, event=0):
        """Прицеливание. Зависит от положения мыши."""
        if event:
            self.an = math.atan((event.y-450) / (event.x-20))

        canv.coords(self.id, 20, 450,
                    20 + max(self.f2_power, 20) * math.cos(self.an),
                    450 + max(self.f2_power, 20) * math.sin(self.an)
                    )

    def power_up(self):
        if self.f2_on:
            if self.f2_power < 100:
                self.f2_power += 1


class target():
    def __init__(self):
        """ Инициализация новой цели. """
        self.id = canv.create_oval(0, 0, 0, 0)
        vx = self.vx = rnd(0, 10)
        vy = self.vy = rnd(0, 10)
        x = self.x = rnd(WIDTH-200-vx, WIDTH-20-vx)
        y = self.y = rnd(HEIGTH-300-vy, HEIGTH-50-vy)
        r = self.r = rnd(2, 50)
        color = self.color = 'red'
        canv.coords(self.id, x-r, y-r, x+r, y+r)
        canv.itemconfig(self.id, fill=color)

    def move(self):
        self.x += self.vx
        self.y += self.vy

        if self.x + self.r >= WIDTH-10:
            self.vx = -self.vx
            self.x = self.x - (self.x + self.r - (WIDTH-10))
        if self.x - self.r <= WIDTH-200+10:
            self.vx = -self.vx
            self.x = self.x + ((WIDTH-200+10) - (self.x - self.r))

        if self.y + self.r >= HEIGTH-10:
            self.vy = -self.vy
            self.y = self.y - (self.y + self.r - (HEIGTH-10))
        if self.y - self.r <= HEIGTH-300+10:
            self.vy = -self.vy
            self.y = self.y + ((HEIGTH-300+10) - (self.y - self.r))

        canv.coords(
                self.id,
                self.x - self.r,
                self.y - self.r,
                self.x + self.r,
                self.y + self.r)

    def hit(self):
        """Попадание шарика в цель."""
        global points
        points += 1
        canv.coords(self.id, -10, -10, -10, -10)


def new_game(event=''):
    global gun, screen1, balls, bullet, canv, root

    targets = [target(), target()]
    bullet = 0
    balls = []
    canv.bind('<Button-1>', g1.fire2_start)
    canv.bind('<ButtonRelease-1>', g1.fire2_end)
    canv.bind('<Motion>', g1.targetting)

    while targets or balls:
        boll_dell = []
        target_dell = []

        for j in range(len(targets)):
            targets[j].move()

        for i in range(len(balls)):
            if not balls[i].move():
                boll_dell.append(i)
            for j in range(len(targets)):
                if balls[i].hittest(targets[j]):
                    targets[j].hit()
                    target_dell.append(j)
                    canv.itemconfig(id_points, text=points)

        for e in boll_dell[::-1]:
            balls.pop(e)

        for e in target_dell[::-1]:
            targets.pop(e)

        if not targets:
            canv.bind('<Button-1>', '')
            canv.bind('<ButtonRelease-1>', '')
            canv.bind('<Motion>', '')
            canv.itemconfig(screen1, text='Вы уничтожили цели за ' + str(bullet) + ' выстрелов')

        canv.update()
        g1.targetting()
        g1.power_up()
        time.sleep(0.03)

    canv.itemconfig(screen1, text='')
    canv.delete(gun)
    root.after(750, new_game)


root = tk.Tk()
root.geometry(str(WIDTH) + 'x' + str(HEIGTH))
canv = tk.Canvas(root, bg='white')
canv.pack(fill=tk.BOTH, expand=1)
screen1 = canv.create_text(400, 300, text='', font='28')
g1 = gun()
points = 0
id_points = canv.create_text(30, 30, text=points, font='28')

root.after(10, new_game)
root.mainloop()
