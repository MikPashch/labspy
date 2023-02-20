import turtle as t

t.shape("turtle")
t.penup()
t.goto(0, - 200)
t.pendown()


t.begin_fill()
t.color("yellow")
t.circle(200)
t.end_fill()
t.penup()

t.goto(-90, 50)
t.pendown()
t.begin_fill()
t.color('blue')
t.circle(35)
t.end_fill()
t.penup()

t.goto(90, 50)
t.pendown()
t.begin_fill()
t.color('blue')
t.circle(35)
t.end_fill()
t.penup()

t.goto(0, 20)
t.right(90)
t.color('black')
t.pendown()
t.width(10)
t.forward(40)
t.penup()

t.goto(100, -40)
t.color('red')
t.pendown()
t.width(10)
t.circle(-100, 180)
t.penup()