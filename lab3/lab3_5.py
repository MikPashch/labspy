import turtle
from random import randint

number_of_turtles = 20
steps_of_time_number = 50


pool = [turtle.Turtle(shape='circle') for i in range(number_of_turtles)]
for unit in pool:
    unit.penup()
    unit.speed(50)
    unit.goto(randint(-200, 200), randint(-200, 200))


for i in range(steps_of_time_number):
    for unit in pool:
        unit.forward(5)
        unit.left(randint(0, 360))

