# Logan Richan
# ph295

from numpy import array, arange, zeros
from matplotlib import pylab as plt

### CONSTANTS ###
S= 10.
R= 28.
B= 8./3.

### RANGE ###
a=0. # t initial
b=50. # t final
N=10000 #Many points needed for a smooth curve for x vs. z graph
h=(b-a)/float(N)

### POINTS ###
tPoints=arange(a,b,h)
xPoints=zeros(N,float)
yPoints=zeros(N,float)
zPoints=zeros(N,float)

### X, Y, &Z VALUES ###
r = array([0,1,0],float) #(x,y,z) = (0,1,0)

### GIVEN DIFFERENTIAL EQUATIONS ###
def f(r,t):
    x=r[0]
    y=r[1]
    z=r[2]
    fx=S*(y-x)
    fy=R*x-y-x*z
    fz=x*y-B*z
    
    return array([fx,fy,fz],float)

### PLOT USING 4TH ORDER RUNGE-KUTTA ###
def plot(r):
    i=0
    for t in tPoints:
        xPoints[i]=r[0]
        yPoints[i]=r[1]
        zPoints[i]=r[2]
        k1=h*f(r, t)
        k2=h*f(r+0.5*k1, t+0.5*h)
        k3=h*f(r+0.5*k2, t+0.5*h)
        k4=h*f(r+k3, t+h)
        r+=(k1+ 2*k2+ 2*k3+ k4)/6
        i+=1    
    plt.subplot(121)
    plt.plot(tPoints,yPoints)
    plt.xlabel('t')
    plt.ylabel('y')
    plt.subplot(122)
    plt.plot(xPoints,zPoints)
    plt.xlabel('x')
    plt.ylabel('z')
    plt.show()
plot(r)
