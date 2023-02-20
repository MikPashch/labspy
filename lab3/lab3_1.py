from random import *
import turtle

turtle.shape('turtle')

for i in range(50):
    turtle.forward(randint(10, 25))
    turtle.left(randint(1, 100))
    turtle.forward(randint(1, 25))
    turtle.right(randint(-180, 180))
    turtle.forward(randint(1, 25))