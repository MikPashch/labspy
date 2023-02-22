import turtle as t

t.shape('turtle')
t.color('blue')
t.width(5)

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 'space']
step1 = 50
step2 = step1 * 2
step3 = (2 * (step1**2)) ** 0.5
step4 = (step1**2 + step2**2) ** 0.5
step5 = step1 * 0.25

numbers[1] = [t.right(90), t.forward(step2), t.right(180), t.forward(step2),
              t.left(135), t.forward(step3), t.right(180), t.forward(step3), t.right(45)]

numbers[10] = [t.penup(), t.forward(step5 + step1), t.pendown()]

numbers[4] = [t.left(270), t.forward(step2), t.right(180), t.forward(step1),
              t.left(90), t.forward(step1), t.right(90), t.forward(step1),
              t.penup(), t.right(90), t.forward(step1), t.pendown()]

numbers[10] = [t.penup(), t.forward(step5 + step1), t.pendown()]

numbers[1] = [t.right(90), t.forward(step2), t.right(180), t.forward(step2),
              t.left(135), t.forward(step3), t.right(180), t.forward(step3), t.right(45)]

numbers[10] = [t.penup(), t.forward(step5 + step1), t.pendown()]

numbers[7] = [t.left(180), t.forward(step1), t.right(180), t.forward(step1), t.right(135),
              t.forward(step3), t.left(45), t.forward(step1), t.left(90),
              t.penup(), t.forward(step1), t.left(90), t.forward(step2), t.right(90), t.pendown()]

numbers[10] = [t.penup(), t.forward(step5 + step1), t.pendown()]

numbers[0] = [t.right(90), t.forward(step2), t.right(90), t.forward(step1),
              t.right(90), t.forward(step2), t.right(90), t.forward(step1)]

numbers[10] = [t.penup(), t.forward(step5 + step1), t.pendown()]

numbers[0] = [t.right(90), t.forward(step2), t.right(90), t.forward(step1),
              t.right(90), t.forward(step2), t.right(90), t.forward(step1)]

