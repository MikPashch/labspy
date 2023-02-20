import numpy as np
import matplotlib.pyplot as plt

x = 1
e = np.e
sin = np.sin

y = ((e ** (1 / (sin(x) + 1))) / ((5 / 4) + (1 / ((x ** 1) * 5))))
log = np.log(y) / np.log(1 + x ** 2)

print(log)

x = np.arange(-10, 10.01, 0.01)
plt.plot(x, x * x - x - 6)
plt.grid(True)

plt.show()
#comment
