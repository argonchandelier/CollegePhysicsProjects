# Logan Richan
# ph150

from numpy import cos, arange, zeros
from random import uniform
from matplotlib import pyplot as plt

t0=0.
tf=30.

endXvalues=zeros(200,float)

cMean=5.
cUncertainty=0.5

xMean=0.
xUncertainty=0.5

vMean=10.
vUncertainty=0.25


plt.subplot(121)
for j in range(200):
    c = uniform(cMean - cUncertainty, cMean + cUncertainty)
    x = uniform(xMean - xUncertainty, xMean + xUncertainty)
    v = uniform(vMean - vUncertainty, vMean + vUncertainty)
    
    def axCalc(v,t):
        ax=c*cos(v**2)*(t**(1.5))
        return ax

    n=100.
    dt=1./n # = 0.01
    N=int(n*(tf-t0))
    tvalues=arange(t0,tf,dt)
    xvalues=zeros(N,float)
    vxvalues=zeros(N,float)
    axvalues=zeros(N,float)
    i=0
    for t in tvalues:
        ax=axCalc(v,t)
        x+=v*dt
        v+=ax*dt
        xvalues[i]=x
        vxvalues[i]=v
        axvalues[i]=ax
        i+=1

    plt.plot(tvalues,xvalues)
    #plt.show()
    
    endXvalues[j]=x
print(endXvalues)
plt.subplot(122)
plt.hist(endXvalues, bins=10)
plt.show()
