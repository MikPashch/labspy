import numpy as np
import matplotlib.pyplot as plt

sin = np.sin
tan = np.tan
exp = np.exp

x = np.arange(0, 100, 0.01)
plt.plot(np.log((x**2 + 1) * exp(-(abs(x)/10))) / np.log(1 + tan(1 / (1 + (sin(x)**2)))))
plt.grid(True)

plt.show()
