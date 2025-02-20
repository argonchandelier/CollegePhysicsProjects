# Logan Richan
# ph295

from numpy import sin, array, arange, zeros,pi
from matplotlib import pylab as plt

g= 9.81
l= 0.1

a=0.
b=10
N=1000
h=(b-a)/float(N)
tpoints=arange(a,b,h)
th=179.999
w=0

omegapoints=zeros(N,float)
thetapoints=zeros(N,float)
r=array([th*pi/180,w*pi/180],float) #theta[0],omega[0]

def f(r,t):
    theta = r[0]
    omega = r[1]
    ftheta = omega
    fomega = -(g/l)*sin(theta)
    return array([ftheta,fomega],float)

i=0
for t in tpoints:
    omegapoints[i]=r[1]
    thetapoints[i]=r[0]
    k1=h*f(r, t)
    k2=h*f(r+0.5*k1, t+0.5*h)
    k3=h*f(r+0.5*k2, t+0.5*h)
    k4=h*f(r+k3, t+h)
    r+=(k1+ 2*k2+ 2*k3+ k4)/6
    i+=1
thetapoints*=180/pi
#plt.subplot(121)
plt.plot(tpoints,thetapoints)
plt.xlabel("t")
plt.ylabel("theta")
#plt.plot(tpoints,omegapoints)
'''
plt.subplot(122)
plt.plot(thetapoints,omegapoints)
plt.xlabel("theta")
plt.ylabel("omega")
'''
plt.show()
