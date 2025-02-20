# Logan Richan
# ph295

from numpy import zeros, array, arange
from matplotlib import pylab as plt

# Constants
m=20.
k=20.
v0=0.
x0=1.

# Time interval
a=0
b=15
h=dt=0.1
tpts=arange(a,b,dt)

# initialize x points
N=len(tpts)
xpts=zeros(N,float)

def f(r,c): # (d^2/dt^2)x evaluation
    x = r[0]
    v = r[1]
    fx = v
    fv = (-k*x-c*v)/m
    return array([fx,fv],float)

for c in array([5,40,200],float): # Plot Displacement vs. time for all 3 damping coefficients
    r=array([x0,v0],float)
    i=0
    for t in tpts:
        xpts[i]=r[0]
        k1 = h*f(r,c)
        k2 = h*f(r+0.5*k1,c)
        k3 = h*f(r+0.5*k2,c)
        k4 = h*f(r+k3,c)
        r += (k1+k2+k3+k4)/6.
        i+=1
    plt.plot(tpts,xpts)

plt.xlabel("Time (s)")
plt.ylabel("Displacement (m)")
plt.gca().legend(("Underdamped","Critically damped","Overdamped"))
plt.show()
