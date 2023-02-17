import turtle
import numpy as np

turtle.shape('turtle')

r = 50
n = 3
a = r * 2 * np.sin(np.pi / 180 * (360 / (2 * n)))
alpha = (360 / (2 * n))     # 60degree
delta = 25

for i in range(15):
    turtle.left(180 - (alpha / 2))
    for y in range(n):
        turtle.forward(a)
        turtle.left(360 / n)
    turtle.right(180 - (alpha / 2))
    turtle.penup()
    turtle.forward(delta)
    turtle.pendown()
    n += 1
    r = r + delta
    a = r * 2 * np.sin(np.pi / 180 * (360 / (2 * n)))
    alpha = 180 - (360 / n)
