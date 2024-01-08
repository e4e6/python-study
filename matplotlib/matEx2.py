import numpy as np
import matplotlib.pyplot as plt

x = np.arange(0,6,0.1)
y1 = np.sin(x)
y2 = x

plt.plot(x,y1,label="sin")
plt.plot(x,y2,label="x", linestyle = "--")
plt.xlabel("x")
plt.ylabel("y")

plt.legend()
plt.title("sin and cos ex")
plt.show()