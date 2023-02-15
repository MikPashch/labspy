import turtle

turtle.shape('turtle')
x = 1
for i in range(20):
    for j in range(30):
        turtle.forward(x)
        turtle.left(6)
    x += 1
