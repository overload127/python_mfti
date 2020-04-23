#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# подключение библиотек
from random import randrange as rnd, choice
import tkinter as tk
import math
import time

WIDTH = 800
HEIGTH = 600


class Ball:
    gravity = 2
    # 0 <= glide <= 1
    glide = 0.05

    def __init__(self, x, y, vx, vy, r=10):
        """ Конструктор класса Ball
        Args:
            x - начальное положение мяча по горизонтали
            y - начальное положение мяча по вертикали
            r - радиус мяча
            vx - х координата вектора движения
            vy - у координата вектора движения
        """
        self.x = x
        self.y = y
        self.r = 10
        self.vx = vx
        self.vy = vy
        # атрибуты графики
        self.color = choice(['blue', 'green', 'red', 'brown'])
        self.id = canv.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color)

    def move(self):
        """ Переместить мяч по прошествии единицы времени.

        Метод описывает перемещение мяча за один кадр перерисовки. То есть,
        обновляет значения self.x и self.y с учетом скоростей self.vx и self.vy,
        силы гравитации, и силы трения, действующей на мяч,
        и стен по краям окна (размер окна 800х600).

        Returns:
            True - мяч ещё движется и может на что-то повлиять
            False - движение vzxf уже не может на кого-то повлиять.
        """
        # Проверяем остановку снаряда. Для удаления с поля.
        # Т.к. на снаряд может действовать сила тяжести,
        # то необходимоучитывать её и делать проверку по оси Y
        # немного больше
        if abs(self.vy) < self.gravity*0.6 and abs(self.vx) < 0.2:
            self.x = -100
            self.y = -100
            return False

        # применяем силу тяжести на движение
        self.vy += self.gravity

        # применяем силу трения на движение
        self.vx *= (1 - self.glide)
        self.vy *= (1 - self.glide)

        # Применяем вектор движения на положение мячика
        self.x += self.vx
        self.y += self.vy

        # Проверяем косание границы поля справа
        if self.x + self.r >= WIDTH-10:
            self.vx = -self.vx
            self.x = self.x - (self.x + self.r - (WIDTH-10))

        # Проверяем косание границы поля Внизу
        if self.y + self.r >= HEIGTH-10:
            self.vy = -self.vy
            self.y = self.y - (self.y + self.r - (HEIGTH-10))

        return True

    def hittest(self, obj):
        """ Функция проверяет сталкивалкивается ли данный обьект с целью,
        описываемой в обьекте obj.
        Проверка осуществляется на основании длинны растояния и радиусов объектов

        Args:
            obj: Обьект, с которым проверяется столкновение.
        Returns:
            True - в случае столкновения мяча и цели.
            False - если объекты не столкнулись.
        """
        x = self.x - obj.x
        y = self.y - obj.y
        length = (x**2 + y**2)**0.5
        if length <= self.r + obj.r:
            return True
        return False

    # Функции связанные с графикой
    def draw(self):
        """ Метод отрисовки объекта
        """
        canv.coords(
            self.id,
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r)


class Gun:
    power_start = 10

    def __init__(self, start_x=20, start_y=420):
        """ Конструктор класса Gun
        Args:
            start_x, start_y - начальная координата пушки
            end_x, end_y - конечная координата пушки

        power_start - начальная мощьпушки
        """
        self.aim = False
        self.angel = 1
        self.power = self.power_start
        self.start_x = start_x
        self.start_y = start_y
        # Расчитываем угол и вторые координаты пушки
        self.targetting()
        self.button_click = False
        # атрибуты графики
        self.id = canv.create_line(
            self.start_x, self.start_y,
            self.end_x, self.end_y, width=7)

    def fire_start(self, event):
        """ Метод фиксирует и запоминает нажатие кнопки
        Args:
            event - Информация о событии вызвавшем это действие.
                Обычно инфа о мышки
        """
        self.targetting(event)
        self.aim = True
        self.set_orange_color()

    def fire_end(self, event):
        """ Реагирует на события отжатия кнопки
        Рассчитывает мощь выстрела
        Создаёт снаряд?
        Args:
            event - Информация о событии вызвавшем это действие.
                Обычно инфа о мышки
        Returns:
            new_ball - возвращает снаряд с расчитыными параметрами.
        """
        global bullet, balls
        # финальный просчёт всех параметров пушки
        self.aim = False
        self.targetting(event)
        # Рассчёт всех параметров снаряда
        vx = self.power * math.cos(self.angel)
        vy = self.power * math.sin(self.angel)

        # Создание нового мяча
        new_ball = Ball(self.end_x, self.end_y, vx, vy, 10)

        # Возврат к начальной мощности пушки
        self.power = 10
        balls.append(new_ball)
        bullet += 1
        self.set_black_color()

    def power_up(self):
        """ Если это подготовка к выстрелу то увеличиваем мощь пушки.
        Ограничение мощности заряда = 100
        """
        if self.aim:
            if self.power < 100:
                self.power += 1

    def targetting(self, event=0):
        """ Прицеливание. Зависит от положения мыши.
        Так же вызывается при инициализации.
        Args:
            event - Информация о событии вызвавшем это действие.
                Обычно инфа о мышки
        """
        if event and event.x-self.start_x:
            self.angel = math.atan((event.y-self.start_y) / (event.x-self.start_x))

        # Расчёт конечных координат пушки
        self.end_x = self.start_x + self.power * math.cos(self.angel)
        self.end_y = self.start_y + self.power * math.sin(self.angel)

    # Функции связанные с графикой
    def set_orange_color(self):
        """ Событие реагирование на заряд пушки
        Устанавливает цвет пушки в оранжевый
            event - Информация о событии вызвавшем это действие.
                Обычно инфа о мышки
        """
        canv.itemconfig(self.id, fill='orange')

    def set_black_color(self):
        """ Событие реагирование на выстрел пушки
        Устанавливает цвет пушки в чёрный
            event - Информация о событии вызвавшем это действие.
                Обычно инфа о мышки
        """
        canv.itemconfig(self.id, fill='black')

    def draw(self):
        """ Метод отрисовки объекта
        """
        canv.coords(
            self.id,
            self.start_x,
            self.start_y,
            self.end_x,
            self.end_y)


class Target:
    def __init__(self):
        """ Инициализация новой цели.
        Args:
        """
        self.vx = rnd(0, 10)
        self.vy = rnd(0, 10)
        self.x = rnd(WIDTH-200-self.vx, WIDTH-20-self.vx)
        self.y = rnd(HEIGTH-300-self.vy, HEIGTH-50-self.vy)
        self.r = rnd(2, 50)
        # атрибуты графики
        self.color = 'red'
        self.id = canv.create_oval(
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,
            fill=self.color)

    def move(self):
        """ Переместить цель по прошествии единицы времени.

        Метод описывает перемещение цели за один кадр перерисовки. То есть,
        обновляет значения self.x и self.y с учетом скоростей self.vx и self.vy,

        Returns:
            True - мяч ещё движется и может на что-то повлиять
            False - движение vzxf уже не может на кого-то повлиять.
        """
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

    # Функции связанные с графикой
    def draw(self):
        """ Метод отрисовки объекта
        """
        canv.coords(
            self.id,
            self.x - self.r,
            self.y - self.r,
            self.x + self.r,
            self.y + self.r,)


def new_round(event=''):
    global bullet, balls, points

    targets = [Target(), Target()]
    bullet = 0
    balls = []
    canv.bind('<Button-1>', gun.fire_start, gun.set_orange_color)
    canv.bind('<ButtonRelease-1>', gun.fire_end, gun.set_black_color)
    canv.bind('<Motion>', gun.targetting)

    while targets or balls:
        # physics block
        boll_dell = []
        target_dell = []

        for j in range(len(targets)):
            targets[j].move()

        for i in range(len(balls)):
            if not balls[i].move():
                boll_dell.append(i)
            for j in range(len(targets)):
                if balls[i].hittest(targets[j]):
                    points += 1
                    target_dell.append(j)
                    canv.itemconfig(text_points, text=points)

        for e in boll_dell[::-1]:
            ball = balls.pop(e)
            ball.x = -100
            ball.y = -100
            ball.draw()

        for e in target_dell[::-1]:
            target = targets.pop(e)
            target.x = -100
            target.y = -100
            target.draw()

        gun.targetting()
        gun.power_up()

        if not targets:
            canv.bind('<Button-1>', '')
            canv.bind('<ButtonRelease-1>', '')
            canv.bind('<Motion>', '')
            canv.itemconfig(screen_end, text='Вы уничтожили цели за ' + str(bullet) + ' выстрелов')

        # graphics block
        for ball in balls:
            ball.draw()

        for target in targets:
            target.draw()

        gun.draw()

        canv.update()

        time.sleep(0.03)

    canv.itemconfig(screen_end, text='')


def main():
    global canv, gun, text_points, screen_end, points

    root = tk.Tk()
    root.geometry(str(WIDTH) + 'x' + str(HEIGTH))
    canv = tk.Canvas(root, bg='white')
    canv.pack(fill=tk.BOTH, expand=1)
    screen_end = canv.create_text(400, 300, text='', font='28')
    points = 0
    text_points = canv.create_text(30, 30, text=points, font='28')
    gun = Gun()

    root.after(10, new_round)
    root.mainloop()


if __name__ == "__main__":
    main()
