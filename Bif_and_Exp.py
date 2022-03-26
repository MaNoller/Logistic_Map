import numpy as np
import matplotlib.pyplot as plt
#from Logistic_Map import Logistic

def Logistic(r,x):
    x_r=r*x*(1-x)
    return x_r

fig, (ax,bx)=plt.subplots(2,1)


n = 10000
r = np.linspace(2.5, 4.0, n)
x = 1e-5 * np.ones(n)
iter=1000
plot=100
lyap_exp=np.zeros(n)
exp=[]

for i in range(iter):
    x = Logistic(r, x)
    lyap_exp += np.log(abs(r - 2 * r * x))
    if i >= (iter-plot):
        ax.plot(r, x, ',k', alpha=.25)
bx.plot(r,lyap_exp/iter,',k', alpha=.5, ms=.5)

plt.show()
