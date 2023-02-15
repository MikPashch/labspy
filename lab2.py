import turtle

turtle.shape('turtle')
x = 100

for i in range(12):

    for s in range(1):
        turtle.forward(x)
        turtle.stamp()
        turtle.left(180)
        turtle.forward(x)
        turtle.left(180)

    turtle.left(30)

