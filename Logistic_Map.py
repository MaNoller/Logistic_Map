import numpy as np
import matplotlib as plt

def Logistic(r,x):
    x_r=r*x*(1-x)
    return x_r

x = np.linspace(0, 1)
fig, ax = plt.subplots(1, 1)
ax.plot(x, Logistic(2, x), 'k')

plt.show()
