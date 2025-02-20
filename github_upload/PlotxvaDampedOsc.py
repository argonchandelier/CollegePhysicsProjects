# Logan Richan
# ph150

from numpy import sin, exp, arange, zeros, cos, pi
from matplotlib import pyplot as plt

#'''
def f(x,t):
    a=10*sin(x)*exp(-.5*t)
    return a

N=200
x=zeros(N,float)
v=zeros(N,float)
a=zeros(N,float)
t=zeros(N,float)

t[0]=0
x[0]=0
v[0]=1
a[0]=f(x[0],t[0])

dt=0.1

for i in range(1,N):
    t[i]=t[i-1]+dt
    x[i]=x[i-1]+v[i-1]*dt
    a[i]=f(x[i],t[i])
    #v[i]=((a[i]+a[i-1])/2.)*dt+v[i-1]
    v[i]=a[i-1]*dt+v[i-1]
    print(t[i],x[i],v[i],a[i])

plt.plot(t,x,'-r',label='x')
plt.plot(t,v,'-b',label='v')
plt.plot(t,a,'-g',label='a')
plt.show()

'''
v=3.2
th=45*pi/180


x=0
y=0
vx=v*cos(th)
vy=v*sin(th)
ay=-9.8
dt=0.05

while y>=0:
    plt.plot(x,y,'o')
    plt.show()
    x+=vx*dt
    y+=vy*dt
    vy+=ay*dt
'''
    