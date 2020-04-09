import graphics as gr
import math

SIZE_X = 800
SIZE_Y = 800

g = 9.81
omega_0 = 9.8
alpha_0 = 0
lp = 200
dt = 0.01
t_0 = 0

x0 = 400
y0 = 400



l = 2
B = 0
m = 10
alpha = alpha_0
omega = omega_0
w0 = g/l;
gamma = B/m;
t = t_0;

window = gr.GraphWin("Model", SIZE_X, SIZE_Y)
#  Начальное положение шарика
coords = gr.Point(x0, y0)
#  Скорость
velocity = gr.Point(0, 0)
acceleration = gr.Point(0, 0)

rectangle = gr.Rectangle(gr.Point(0, 0), gr.Point(SIZE_X, SIZE_Y))
rectangle.setFill('green')
rectangle.draw(window)

sun = gr.Circle(gr.Point(400, 400), 50)
sun.setFill('yellow')
sun.draw(window)

#Обьект Circle создается здесь лишь ОДИН раз
circle = gr.Circle(coords, 10)
circle.setFill('red')
circle.draw(window)



while True:
    omega = omega + (-1*(w0**2) * math.sin(alpha) - gamma * omega) * dt;
    alpha = alpha + omega * dt;
    x1 = lp * math.sin(alpha)
    y1 = lp * math.cos(alpha)
    circle.move(x0 + x1 - circle.getCenter().x,
                y0 + y1 - circle.getCenter().y)
    
    gr.time.sleep(0.05)
