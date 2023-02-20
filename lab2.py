import turtle
import numpy as np

turtle.shape('turtle')

for i in range(3):
    turtle.circle(50, 360)
    turtle.circle(-50, 360)
    turtle.left(360 / 6)
