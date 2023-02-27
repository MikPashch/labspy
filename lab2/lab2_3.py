import turtle

turtle.shape('turtle')
x = 50
step = 0
for i in range(10):

    for s in range(4):
        turtle.forward(x)
        turtle.left(90)

    x += 40
    step -= 20
    turtle.penup()
    turtle.goto(step, step)
    turtle.pendown()