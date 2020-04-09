#!/usr/bin/python3

# подключение библиотеки под синонимом gr
import graphics as gr
import random

WIDTH = 800
HEIGHT = 600
WIDTH_BOOK = 20
MAX_BOOK = WIDTH // WIDTH_BOOK

def main():
    random.seed()
    # Инициализация окна с названием "Russian game" и размером 100х100 пикселей
    window = gr.GraphWin("Russian game", WIDTH, HEIGHT)
    draw_all(window)
    
    # Ожидание нажатия кнопки мыши по окну.
    window.getMouse()
    # Закрытие окна после завершения работы с графикой
    window.close()

def draw_shelf(window, x, y, widtg, height):
    for i in range(y,y-height,-50):
        line = gr.Line(gr.Point(x, i), gr.Point(x+widtg, i))
        line.setWidth(5)
        line.draw(window)

def draw_all_book(window):
    for i in range(50,HEIGHT,50):
        for k in range(random.randint(0, MAX_BOOK)):
            x = k * WIDTH_BOOK
            y = i - 5

            draw_book(window, x, y, WIDTH_BOOK-2, 40)

def draw_book(window, x, y, widtg, height):
    book = gr.Rectangle(gr.Point(x, y), gr.Point(x + widtg, y-height))
    book.setFill(gr.color_rgb(random.randint(0, 255),
                              random.randint(0, 255),
                              random.randint(0, 255)))
    book.draw(window)
    book_name = gr.Rectangle(gr.Point(x+4, y-2), gr.Point(x + widtg-4, y-height+12))
    book_name.setFill(gr.color_rgb(0,0,0))
    book_name.draw(window)

def draw_book_on_shelf(window, x, y, widtg, height):
    for i in range(y,y-height,-50):
        for k in range(x, x+widtg-WIDTH_BOOK,WIDTH_BOOK):
            draw_book(window, k, i, WIDTH_BOOK-2, 40)
    

def draw_rack(window, x, y, widtg, height):
    rack = gr.Rectangle(gr.Point(x, y), gr.Point(x+widtg, y-height))
    rack.setFill(gr.color_rgb(random.randint(0, 255),
                              random.randint(0, 255),
                              random.randint(0, 255)))
    rack.setWidth(5)
    rack.draw(window)
    draw_shelf(window, x, y, widtg, height)

    draw_book_on_shelf(window, x+5, y-3, widtg-10, height-6)
    
    

def draw_all(window):
    # Создание круга с радиусом 10 и координатами центра (50, 50)
    my_circle = gr.Circle(gr.Point(50, 50), 10)
    
    # Создание отрезка с концами в точках (2, 4) и (4, 8)
    my_line = gr.Line(gr.Point(2, 4), gr.Point(4, 8))
        

    window.setBackground(gr.color_rgb(139, 69, 19))
    # Отрисовка примитивов в окне window
    #draw_shelf(window)
    #draw_all_book(window)

    draw_rack(window,100,500,200,400)
    draw_rack(window,400,450,150,300)
    
    my_circle.draw(window)
    my_line.draw(window)

    

main()
