#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# подключение библиотек
import tkinter as tk
from random import randrange as rnd, choice

# -----------------------------------------------------------------------
# Константы
# -----------------------------------------------------------------------
C_ID, C_X, C_Y, C_R, C_MX, C_MY = 0, 1, 2, 3, 4, 5


# -----------------------------------------------------------------------
# Вспомогательные функции
# -----------------------------------------------------------------------
def new_ball(i):
    """
    Создаёт шар случайного цвета в случайном месте
    """
    circles[i][C_X] = rnd(100, 700)
    circles[i][C_Y] = rnd(100, 500)
    circles[i][C_R] = rnd(30, 50)
    circles[i][C_MX] = rnd(1, 25)
    circles[i][C_MY] = rnd(1, 25)
    circles[i][C_ID] = canv.create_oval(
        circles[i][C_X]-circles[i][C_R], circles[i][C_Y]-circles[i][C_R],
        circles[i][C_X]+circles[i][C_R], circles[i][C_Y]+circles[i][C_R],
        fill=choice(colors), width=0)


def move_ball():
    """
    Выполняет движение шара
    """
    for circle in circles:
        circle[C_X] += circle[C_MX]
        circle[C_Y] += circle[C_MY]

        # Проверка выхода шариков по координате х за границы экрана
        if circle[C_X] + circle[C_R] >= window_width:
            circle[C_X] = window_width - (circle[C_X] + circle[C_R]
                                          - window_width) - circle[C_R]
            circle[C_MX] *= -1
        elif circle[C_X] - circle[C_R] <= 0:
            circle[C_X] = circle[C_R] + abs(circle[C_X] - circle[C_R])
            circle[C_MX] *= -1

        # Проверка выхода шариков по координате у за границы экрана
        if circle[C_Y] + circle[C_R] >= window_heigth:
            circle[C_Y] = window_heigth - (circle[C_Y] + circle[C_R]
                                           - window_heigth) - circle[C_R]
            circle[C_MY] *= -1
        elif circle[C_Y] - circle[C_R] <= 0:
            circle[C_Y] = circle[C_R] + abs(circle[C_Y] - circle[C_R])
            circle[C_MY] *= -1

        # Движение шарика на холсте
        canv.coords(circle[C_ID], circle[C_X]-circle[C_R],
                    circle[C_Y]-circle[C_R], circle[C_X] + circle[C_R],
                    circle[C_Y] + circle[C_R])

    # далее функция сама себя перевызывает несколько раз в секунду
    root.after(100, move_ball)


def click(event):
    """
    Обработка щелчка мыши
    Начисление очков игроку
    Уничтожение страго шарика
    Создание нового
    """
    global count_points
    for i in range(count_circle):
        cur_x = abs(event.x - circles[i][C_X])
        cur_y = abs(event.y - circles[i][C_Y])

        length_from_centre_circle = (cur_x ** 2 + cur_y ** 2) ** 0.5

        if length_from_centre_circle <= circles[i][C_R]:
            count_points += 1
            canv.delete(circles[i][C_ID])
            new_ball(i)
            break

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
# Задаём количество шариков
count_circle = rnd(1, 10)
# Создаём список шариков
circles = [[0, 0, 0, 0, 0, 0] for i in range(count_circle)]

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
for i in range(count_circle):
    new_ball(i)
# первый вызов движения шара.
move_ball()

# Запуск главного цикла
tk.mainloop()
