# Logan Richan
# ph336
# Problem 3

from matplotlib import pyplot as plt
from numpy import pi, std, mean, cos, sin, linspace
from numpy.random import randn


g=9.80 #m/s^2
c,dc=0.48,0.02 # drag coefficient
x0,dx0=0,0.005 #in m
y0,dy0=1.043,0.005 #in m
v0,dv0=5.42,0.04 #in m/s
th,dth=40.0/180.*pi,0.5/180.*pi #theta in radians
d,dd=0.025,0.001 #diameter in m
p,dp=0.736,0.001 #in kg/m^3

dt=0.0005

def randomize(a,da):
    return (a+randn()*da)

def QD(p,A,C,v):
    k=1
    if v<0:
        k=-1
    return -k*(1./2.)*p*A*C*v**2 # in kg*m/s^2

X=[]
Y=[]
MM=[]

for M in linspace(0.0005,0.025,1000):
    C=randomize(c,dc)
    X0=randomize(x0,dx0)
    Y0=randomize(y0,dy0)
    V0=randomize(v0,dv0)
    TH=randomize(th,dth)
    D=randomize(d,dd)
    P=randomize(p,dp)
    
    A=pi/4*D**2
    
    vx=V0*cos(TH)
    vy=V0*sin(TH)
    x=X0
    y=Y0
    t=0
    
    while y > 0:
        ay=-g+QD(P,A,C,vy)/M
        ax=QD(P,A,C,vx)/M
        
        vx+=ax*dt
        vy+=ay*dt
        
        y+=vy*dt
        x+=vx*dt
        t+=dt
        
    X.append(x)
    Y.append(y)
    MM.append(M)

x=mean(X)
xUnc=std(X)
y=mean(Y)
yUnc=std(Y)

print(x)
print(xUnc)

plt.title('position vs. mass')
plt.xlabel('mass (kg)')
plt.ylabel('position (m)')
plt.plot(MM,X,'.')
plt.show()