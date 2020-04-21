#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# подключение библиотек
import tkinter as tk
from random import randrange as rnd, choice
import math

# -----------------------------------------------------------------------
# Константы
# -----------------------------------------------------------------------
ID, X, Y, R, MX, MY = 0, 1, 2, 3, 4, 5
SIZE = 3
FACTOR = 4
AXIS = 5
MOVE = 6
DELTA = 7


# -----------------------------------------------------------------------
# Вспомогательные функции
# -----------------------------------------------------------------------
def new_ball(i):
    """
    Создаёт шар случайного цвета в случайном месте
    """
    circles[i][X] = rnd(100, 700)
    circles[i][Y] = rnd(100, 500)
    circles[i][R] = rnd(30, 50)
    circles[i][MX] = rnd(1, 10)
    circles[i][MY] = rnd(1, 10)
    circles[i][ID] = canv.create_oval(
        circles[i][X]-circles[i][R], circles[i][Y]-circles[i][R],
        circles[i][X]+circles[i][R], circles[i][Y]+circles[i][R],
        fill=choice(colors), width=0)


def move_ball():
    """
    Выполняет движение шара
    """
    for circle in circles:
        circle[X] += circle[MX]
        circle[Y] += circle[MY]

        # Проверка выхода шариков по координате х за границы экрана
        if circle[X] + circle[R] >= window_width:
            circle[X] = window_width - (circle[X] + circle[R]
                                        - window_width) - circle[R]
            circle[MX] *= -1
        elif circle[X] - circle[R] <= 0:
            circle[X] = circle[R] + abs(circle[X] - circle[R])
            circle[MX] *= -1

        # Проверка выхода шариков по координате у за границы экрана
        if circle[Y] + circle[R] >= window_heigth:
            circle[Y] = window_heigth - (circle[Y] + circle[R]
                                         - window_heigth) - circle[R]
            circle[MY] *= -1
        elif circle[Y] - circle[R] <= 0:
            circle[Y] = circle[R] + abs(circle[Y] - circle[R])
            circle[MY] *= -1

        # Движение шарика на холсте
        canv.coords(circle[ID], circle[X]-circle[R],
                    circle[Y]-circle[R], circle[X] + circle[R],
                    circle[Y] + circle[R])

    root.after(33, move_ball)


def new_cube(i):
    """
    Создаёт кубик случайного цвета в случайном месте
    выбирает ось движения и степень отклонения
    """
    cubes[i][SIZE] = rnd(30, 50)
    cubes[i][FACTOR] = rnd(50, 100)
    cubes[i][AXIS] = choice(axis_move)
    cubes[i][MOVE] = rnd(5, 20)
    if cubes[i][AXIS] == axis_move[0]:
        # cube[AXIS] = "X"
        cubes[i][X] = rnd(cubes[i][SIZE]+cubes[i][FACTOR],
                          window_width-cubes[i][SIZE]-cubes[i][FACTOR])
        cubes[i][DELTA] = rnd(cubes[i][SIZE]+cubes[i][FACTOR],
                              window_heigth-cubes[i][SIZE]-cubes[i][FACTOR])
        cubes[i][Y] = cubes[i][DELTA]+math.sin(
            cubes[i][X]/(window_width*0.2))*cubes[i][FACTOR]
    else:
        # cube[AXIS] = "Y"
        cubes[i][DELTA] = rnd(cubes[i][SIZE]+cubes[i][FACTOR],
                              window_width-cubes[i][SIZE]-cubes[i][FACTOR])
        cubes[i][Y] = rnd(cubes[i][SIZE]+cubes[i][FACTOR],
                          window_heigth-cubes[i][SIZE]-cubes[i][FACTOR])
        cubes[i][X] = cubes[i][DELTA]-math.sin(
            cubes[i][Y]/(window_heigth*0.2)) * cubes[i][FACTOR]

    cubes[i][ID] = canv.create_rectangle(
        cubes[i][X]-cubes[i][SIZE], cubes[i][Y]-cubes[i][SIZE],
        cubes[i][X]+cubes[i][SIZE], cubes[i][Y]+cubes[i][SIZE],
        fill=choice(colors), width=0)


def move_cube():
    """
    Выполняет движение кубиков
    """
    for cube in cubes:
        if cube[AXIS] == axis_move[0]:
            # cube[AXIS] = "X"
            cube[X] += cube[MOVE]

            # Проверка выхода шариков по координате х за границы экрана
            if cube[X] + cube[SIZE] >= window_width:
                cube[X] = window_width - (cube[X] + cube[SIZE]
                                          - window_width) - cube[SIZE]
                cube[MOVE] *= -1
            elif cube[X] - cube[SIZE] <= 0:
                cube[X] = cube[SIZE] + abs(cube[X] - cube[SIZE])
                cube[MOVE] *= -1

            cube[Y] = cube[DELTA]+math.sin(
                cube[X]/(window_width*0.2))*cube[FACTOR]
            # Отрисовываем кубик при этом расчитываем координату по y
            canv.coords(
                cube[ID],
                cube[X]-cube[SIZE],
                cube[Y]-cube[SIZE],
                cube[X]+cube[SIZE],
                cube[Y]+cube[SIZE])
        else:
            # cube[AXIS] = "Y"
            cube[Y] += cube[MOVE]

            # Проверка выхода шариков по координате у за границы экрана
            if cube[Y] + cube[SIZE] >= window_heigth:
                cube[Y] = window_heigth - (cube[Y] + cube[SIZE]
                                           - window_heigth) - cube[SIZE]
                cube[MOVE] *= -1
            elif cube[Y] - cube[SIZE] <= 0:
                cube[Y] = cube[SIZE] + abs(cube[Y] - cube[SIZE])
                cube[MOVE] *= -1

            cube[X] = cube[DELTA]-math.sin(
                cube[Y]/(window_heigth*0.2)) * cube[FACTOR]
            # Отрисовываем кубик при этом расчитываем координату по х
            canv.coords(
                cube[ID],
                cube[X]-cube[SIZE],
                cube[Y]-cube[SIZE],
                cube[X] + cube[SIZE],
                cube[Y] + cube[SIZE])

    root.after(33, move_cube)


def click(event):
    """
    Обработка щелчка мыши
    Начисление очков игроку
    Уничтожение страго шарика
    Создание нового
    """
    global count_points
    global point_text
    find = False

    # Проверка коллизии с шариком
    for i in range(count_circle):
        global point_text
        cur_x = abs(event.x - circles[i][X])
        cur_y = abs(event.y - circles[i][Y])

        length_from_centre_circle = (cur_x ** 2 + cur_y ** 2) ** 0.5

        if length_from_centre_circle <= circles[i][R]:
            count_points += 1
            canv.delete(circles[i][ID])
            new_ball(i)
            find = True
            break

    # Проверка коллизии с кубиком если нен было колизии с шариком
    if not find:
        for i in range(count_cube):
            if (cubes[i][X] - cubes[i][SIZE] <= event.x <= cubes[i][X] + cubes[i][SIZE] and
               cubes[i][Y] - cubes[i][SIZE] <= event.y <= cubes[i][Y] + cubes[i][SIZE]):
                count_points += 3
                canv.delete(cubes[i][ID])
                new_cube(i)
                find = True
                break

    if find:
        canv.delete(point_text)
        point_text = canv.create_text(
            5, 25, text="Количество очков: " + str(count_points), anchor=tk.NW)


# -----------------------------------------------------------------------
# основной текст программы
# -----------------------------------------------------------------------
# размеры экрана
window_width = 800
window_heigth = 600
# Список цветов.
# Используется для случайного задания  цвета шару
colors = ['red', 'orange', 'yellow', 'green', 'blue']
# Используется для случайного задания  цвета шару
axis_move = ['X', 'Y']
# подсчёт очков
count_points = 0
# Задаём количество шариков
count_circle = rnd(1, 10)
# Задаём количество кубиков
count_cube = rnd(1, 10)
# Создаём список шариков
circles = [[0, 0, 0, 0, 0, 0] for i in range(count_circle)]
# Создаём список кубиков
cubes = [[0, 0, 0, 0, 0, 0, 0, 0] for i in range(count_cube)]

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
# Создаю объект для вывода текста
name_text = canv.create_text(5, 5, text="Никнейм: ", anchor=tk.NW)
point_text = canv.create_text(
    5, 25, text="Количество очков: " + str(count_points), anchor=tk.NW)

# первый вызов создания шара.
for i in range(count_circle):
    new_ball(i)

# первый вызов создания кубиков.
for i in range(count_cube):
    new_cube(i)

# первый вызов движения шара.
move_ball()
# первый вызов движения кубика.
move_cube()

# Запуск главного цикла
tk.mainloop()
