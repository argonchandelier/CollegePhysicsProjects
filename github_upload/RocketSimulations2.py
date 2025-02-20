from numpy import zeros, pi, sin, cos, sqrt
from matplotlib import pyplot as plt
from random import uniform


def thrustA8(t):
    if t < 0.25:
        return  10 / 0.25 * t
    elif t < 0.3:
            return -10 / 0.075 * t + 43.3
    elif t < 0.67:
        return -1.3 / 0.37 * t + 4.25
    elif t < 0.71:
        return -1.7 / 0.04 * t + 30.3
    else:
        return 0

def thrustB6(t):
    if t < 0.175:
        return  12/0.175 * t
    elif t < 0.3:
        return -6.4 / 0.13 * t + 20.5
    elif t < 0.8:
        return -0.9 / 0.5 * t + 6.3
    elif t < 0.85:
        return -4.9 / 0.05 * t + 83.25
    else:
        return 0
        
def mass(t):
    #    return 0.061
    #.066
    if t < 0.75:
        return 0.066 - .0094 * t
    else:
        return 0.059

###############################
mrMean=1 #rocket mass multiplier
mrUnc=.15

gMean=9.8
gUnc=0.15

AxMean=0.68*0.025#
AxUnc=AxMean*0.2
AyMean=pi * (0.01*1.25)**2
AyUnc=AyMean*0.2

CxMean=.5#
CxUnc=.3
CyMean=.75
CyUnc=.2

pMean=.7364
pUnc=.15


A2xMean=.17*.27+AxMean#
A2xUnc=A2xMean*0.3
A2yMean=pi*(.01*15.5)**2
A2yUnc=A2yMean*0.2

C2xMean=0.75#
C2xUnc=.4
C2yMean=1.75
C2yUnc=.2

thMean=90.
thUnc=5.

vWMean=0.  # velocity of wind
vWUnc=1.

tDMean=3.7 #time to deploy parachute
tDUnc=0.5
############################################

N=200
endTimes=zeros(N,float)
yMax=zeros(N,float)

for i in range(N):
    mr = uniform(mrMean + mrUnc, mrMean - mrUnc)
    g = uniform(gMean + gUnc, gMean - gUnc)
    Ax = uniform(AxMean + AxUnc, AxMean - AxUnc)
    Ay = uniform(AyMean + AyUnc, AyMean - AyUnc)
    Cx = uniform(CxMean + CxUnc, CxMean - CxUnc)
    Cy = uniform(CyMean + CyUnc, CyMean - CyUnc)
    p = uniform(pMean + pUnc, pMean - pUnc)
    A2x = uniform(A2xMean + A2xUnc, A2xMean - A2xUnc)
    A2y = uniform(A2yMean + A2yUnc, A2yMean - A2yUnc)
    C2x = uniform(C2xMean + C2xUnc, C2xMean - C2xUnc)
    C2y = uniform(C2yMean + C2yUnc, C2yMean - C2yUnc)
    th = uniform(thMean + thUnc, thMean - thUnc)
    vW = uniform(vWMean + vWUnc, vWMean - vWUnc)
    tD = uniform(tDMean + tDUnc, tDMean - tDUnc)
    
    y=[0]
    v=[0]
    #th=45
    
    vy=0
    vx=0
    x=[0]
    ax=0.
    ay=0.
    aa=0.
    a=[0.]
    
    t=[0]
    dt=0.01
    def FD(v,vn,A,C):
        return .5*p*A*C*v*vn
    k=0
    while thrustA8(t[k])/(mr*mass(t[k]))*sin(th*pi/180) < abs(g):
        t.append(t[-1]+dt)
        y.append(0)
        x.append(0) #####
        v.append(0)
        a.append(0)
        k+=1
    hasFuel=1
    calc=1
    #plt.plot(t[k],y[k],'.') ##
    while y[k]>=0:
        y.append(y[-1]+vy*dt)
        x.append(x[-1]+vx*dt) #####
        t.append(t[-1]+dt)
        
        '''
        if hasFuel==1:
            if (thrustA8(t[k]) == 0):
                C=C2
                A=A2
                hasFuel=0
                #plt.plot(t[k],y[k],'.') ##
        '''
        if calc==1:
            if t[k]>tD:
                Cx=C2x
                Cy=C2x
                Ax=A2x
                Ay=A2y
                calc=0
        
        vy+=ay*dt
        vx+=ax*dt #####
        if y[-1]>y[k]:
            yMax[i]=y[k]
        #v.append(vy) ##
        #print(vy)
        v.append(sqrt(vx**2+vy**2))
        #ax=-FD(v[-1],vx,A,C)/(mr*mass(t)) #####
        if vy>=0:
            ay=-g + (thrustA8(t[k])-FD(v[-1],vy,Ay,Cy))/(mr*mass(t[k]))*sin(th*pi/180)
        else:
            ay=-g + (thrustA8(t[k])-FD(v[-1],vy,Ay,Cy))/(mr*mass(t[k]))*sin(th*pi/180)
        if vx-vW>=0:
            ax=(thrustA8(t[k])-FD(v[-1],vx-vW,Ax,Cx))/(mr*mass(t[k]))*cos(th*pi/180)
        else:
            ax=(thrustA8(t[k])+FD(v[-1],vx-vW,Ax,Cx))/(mr*mass(t[k]))*cos(th*pi/180)
        a.append(ay)
        
        k1=vy
        k2=Ay
        k3=Cy
        
        k+=1
    #'''
    if y[k]<0:
        y[k]=0
    #'''
    plt.subplot(221)
    plt.plot(t,y)
    plt.title("Time vs. Height")
    #plt.show()
    
    plt.subplot(222)
    plt.title("Time vs. Distance")
    plt.plot(t,x)
    
    endTimes[i]=t[k]

plt.subplot(223)
plt.hist(yMax, bins=10)
plt.title("Max heights")
#plt.show()

plt.subplot(224)
plt.hist(endTimes, bins=10)
plt.title("End times")
plt.show()
