# Logan Richan
# ph336

from matplotlib import pyplot as plt
from numpy import pi, std, mean, array
from numpy.random import randn

#plt.close('all')

def randomize(a,da):
    return (a+randn()*da)

g=9.80 #m/s^2
y0,dy0=0.45,0.01 #distance in m
b,db=25.7,0.1 #coefficient for linear drag, D=-bv
pf,dpf=940.2,0.1 #density of oil in kg/m^3
pb,dpb=2700.5,2.0 #density of metal ball
D,dD=0.180,0.005 #diameter in meters

dt=0.002

T=[]

for n in range(1000):
    Y0=randomize(y0,dy0)
    dia=randomize(D,dD)
    Pf=randomize(pf,dpf)
    Pb=randomize(pb,dpb)
    drag=randomize(b,db)
    
    V=pi/6*dia**3
    m=Pb*V
    B=Pf*V*g
    
    y=[0.0]
    v=[0.0]
    t=[0.0]
    
    while y[-1]<Y0:
        a=g-(drag*v[-1]+B)/m
        y.append(y[-1]+v[-1]*dt)
        v.append(v[-1]+a*dt)
        t.append(t[-1]+dt)
    y = array(y)
    T.append(t[-1])
    plt.plot(t,-y)

plt.title('position vs. time')
#plt.figure(2)
#plt.plot(t,v)
plt.xlabel('time (s)')
plt.ylabel('depth (m)')
plt.show()

tfall=mean(T)
tUnc=std(T)

print('')
print('')