import numpy as np
import matplotlib.pyplot as plt

def Logistic(r,x):
    x_r=r*x*(1-x)
    return x_r

thresh=0.05
number=15
x_0=0.6


def cobweb(r,x,number):
    xl = np.linspace(0, 1)
    fig, ax = plt.subplots(1, 1)
    ax.plot(xl, Logistic(r, xl), 'k')
    ax.plot(xl, xl, 'k')

    for i in range(number):
        y=Logistic(r,x)
        ax.plot([x,x],[x,y],'r')
        ax.plot([x,y],[y,y],'r')
        x=y
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)


cobweb(4,x_0,1000)

plt.show()
