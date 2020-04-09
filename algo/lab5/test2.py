import graphics as gr

SIZE_X = 800
SIZE_Y = 800

window = gr.GraphWin("Model", SIZE_X, SIZE_Y)

#Обьект Circle создается здесь лишь ОДИН раз
circle = gr.Circle(gr.Point(400, 400), 10)
circle.draw(window)

while True:
    #Метод move передвигает обьект circle на (1, 1) относительно его текущего положения
    circle.move(1, 1)

    gr.time.sleep(0.02)
