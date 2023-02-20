import numpy as np
import matplotlib.pyplot as plt

x = int(input())
x1 = int(input())
x2 = int(input())
x3 = int(input())

with plt.xkcd():
    plt.pie([x, x1, x2, x3], labels=('Man', 'Woman', 'Middle', 'Unknowing'))
    plt.title('Quantity of people on the world')

plt.show()
# comment for test commit
