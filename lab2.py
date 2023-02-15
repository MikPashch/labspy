import turtle

turtle.shape('turtle')
x = 50
for i in range(15):
    for j in range(2):
        turtle.forward(x)
        turtle.left(90)
    x += 20
