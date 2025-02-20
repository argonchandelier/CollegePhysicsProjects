# Logan Richan
# ph295

from numpy import array, arange, zeros
from matplotlib import pylab as plt

pDrop=-100. #deltaP/deltax
u=1.
d=.1

a=0.
b=d
N=1000
h=(b-a)/N
err=1e-6
yPoints=arange(a,b,h)
vPoints=zeros(N,float)
kPoints=zeros(N,float)

def f(r):
    v=r[0]
    gr=r[1]
    fv=gr
    fgr=1/u * pDrop    
    return array([fv,fgr],float)

def g(gr):
    r=array([0,gr],float)
    i=0
    for t in yPoints:
        vPoints[i]=r[0]
        kPoints[i]=r[1]
        k1=h*f(r)
        k2=h*f(r+0.5*k1)
        k3=h*f(r+0.5*k2)
        k4=h*f(r+k3)
        r+=(k1+ 2*k2+ 2*k3+ k4)/6
        i+=1
    plt.plot(vPoints,-yPoints)
    plt.xlabel("vx")
    plt.ylabel("y")
    #plt.show()
    return r[0]

gr1=.01
gr2=10.
v1 = g(gr1)
v2 = g(gr2)
print(v1,v2)

while abs(v2-v1)>err:
    grM=(gr1+gr2)/2
    vM=g(grM)
    if v1*vM>0:
        gr1=grM
        v1=vM
    else:
        gr2=grM
        v2=vM

gr = (gr1+gr2)/2
print(gr)
#print(-pDrop*d/(2*u))

plt.show()
