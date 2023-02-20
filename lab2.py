import turtle
import numpy as np

r1 = 50
r2 = 15

turtle.shape('turtle')
turtle.penup()
turtle.setposition(-400, 0)
turtle.left(90)
turtle.pendown()

for i in range(10):
    turtle.circle(-r1, 180)
    turtle.circle(-r2, 180)
