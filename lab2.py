import turtle
import turtle as t

t.shape("turtle")

a = 500
turtle.left(180)
t.forward(a)
n = 11

for i in range(n - 1):
    t.left(180 - 360/(2*n))
    t.forward(a)
