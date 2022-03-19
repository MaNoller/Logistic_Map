import numpy as np
import matplotlib.pyplot as plt
from matplotlib.widgets import Slider

def Logistic(r,x):
    x_r=r*x*(1-x)
    return x_r

thresh=0.05
num=100
x_0=0.3


def cobweb(r,x,num,ax):
    for i in range(num):
        y=Logistic(r,x)
        ax.plot([x,x],[x,y],'r')
        ax.plot([x,y],[y,y],'r')
        x=y
    ax.set_xlim(0, 1)
    ax.set_ylim(0, 1)

def start_plot(r,x_0,num):
    xl = np.linspace(0, 1)
    fig, ax = plt.subplots()
    ax2=ax
    ax2.plot(xl, Logistic(r, xl), 'k')
    ax.plot(xl, xl, 'k')
    cobweb(r,x_0,num,ax2)
    plt.subplots_adjust(bottom=0.2)
    return fig,ax,ax2


fig,ax,ax2 = start_plot(3.7,x_0,num)
axfreq = plt.axes([0.2, 0.1, 0.65, 0.03])
freq_slider = Slider(
    ax=axfreq,
    label='Frequency [Hz]',
    valmin=0.001,
    valmax=4,
    valinit=3,
)

def update(val):
    ax2.cla()
    xl = np.linspace(0, 1)
    ax2.plot(xl, Logistic(freq_slider.val, xl), 'k')
    ax.plot(xl, xl, 'k')
    cobweb(freq_slider.val,x_0,num,ax2)
    fig.canvas.draw_idle()

freq_slider.on_changed(update)

plt.show()
