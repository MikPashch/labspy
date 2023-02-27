import turtle

turtle.shape('turtle')

x = 30  # m
y = 30  # m
Vx = 20  # m/s
Vy = 20  # m/s
dt = 0.1  # s
ay = - 9.8  # m/s**2
el_cof = 0.7

while Vy > 1:
    while y >= 0:
        turtle.goto(x, y)
        x += Vx * dt
        y += Vy * dt + ay * (dt ** 2) / 2
        Vy += ay * dt
    y = 0
    Vy = Vx * el_cof
    Vx = Vx * el_cof
