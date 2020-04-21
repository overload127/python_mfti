#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# подключение библиотек
import tkinter as tk
from random import randrange as rnd, choice


# -----------------------------------------------------------------------
# Вспомогательные функции
# -----------------------------------------------------------------------
def new_ball():
    """
    Удаляет все объекты с холста
    Создаёт шар случайного цвета в случайном месте
    """
    global circle_x, circle_y, circle_r
    global move_x, move_y
    global circle_id
    canv.delete(tk.ALL)
    circle_x = rnd(100, 700)
    circle_y = rnd(100, 500)
    circle_r = rnd(30, 50)
    move_x = rnd(1, 50)
    move_y = rnd(1, 50)
    circle_id = canv.create_oval(
        circle_x-circle_r, circle_y-circle_r,
        circle_x+circle_r, circle_y+circle_r,
        fill=choice(colors), width=0)
    root.after(1000, new_ball)


def move_ball():
    """
    Выполняет движение шара
    """
    global circle_x, circle_y, circle_r
    global move_x, move_y
    global circle_id

    circle_x += move_x
    circle_y += move_y

    if circle_x + circle_r >= window_width:
        circle_x = circle_x - (circle_x + circle_r - window_width)
        move_x *= -1
    elif circle_x - circle_r <= 0:
        circle_x = circle_x - (circle_x + circle_r - window_width)
        move_x *= -1

    if circle_y + circle_r >= window_heigth:
        circle_y = circle_y - (circle_y + circle_r - window_heigth)
        move_y *= -1
    elif circle_y - circle_r <= 0:
        circle_y = circle_y - (circle_y + circle_r - window_heigth)
        move_y *= -1

    canv.coords(circle_id, circle_x-circle_r, circle_y-circle_r,
                circle_x + circle_r, circle_y + circle_r)

    root.after(100, move_ball)


def click(event):
    """
    Обработка щелчка мыши
    Начисление очков игроку
    """
    global count_points
    cur_x = abs(event.x - circle_x)
    cur_y = abs(event.y - circle_y)

    length_from_centre_circle = (cur_x ** 2 + cur_y ** 2) ** 0.5

    if length_from_centre_circle <= circle_r:
        count_points += 1

    print(count_points)


# -----------------------------------------------------------------------
# основной текст программы
# -----------------------------------------------------------------------
# размеры экрана
window_width = 800
window_heigth = 600
# Список цветов.
# Используется для случайного задания  цвета шару
colors = ['red', 'orange', 'yellow', 'green', 'blue']
# подсчёт очков
count_points = 0
# Координаты шарика
circle_x, circle_y, circle_r = 0, 0, 0
# Вектор движения шарика
move_x, move_y = 0, 0

# Создаём главное окно
root = tk.Tk()
# Задаём размеры окна
root.geometry('800x600')

# Создаём внутри окна область для рисования
canv = tk.Canvas(root, bg='white')
# Заполняем всё доступное место нашим холстом (cfnvas)
canv.pack(fill=tk.BOTH, expand=1)
# Вешаем обработчик события (щелчёк ЛКМ)
canv.bind('<Button-1>', click)

# первый вызов создания шара.
# далее функция сама себя перевызывает раз в секунду
new_ball()
# первый вызов движения шара.
move_ball()
# далее функция сама себя перевызывает несколько раз в секунду
root.after(100, move_ball)

# Запуск главного цикла
tk.mainloop()
