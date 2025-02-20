# Logan Richan
# ph150
# Rocket Simulations

from numpy import zeros, pi
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


mrMean=1
mrUnc=.15

gMean=9.8
gUnc=0.15

AMean=pi * (0.01*1.25)**2
AUnc=AMean*0.2

CMean=.75
CUnc=.2

pMean=.7364
pUnc=.15


A2Mean=pi*(.01*15.5)**2
A2Unc=A2Mean*0.2

C2Mean=1.75
C2Unc=.2


N=200
endTimes=zeros(N,float)

plt.subplot(121)
for i in range(N):
    mr = uniform(mrMean + mrUnc, mrMean - mrUnc)
    g = uniform(gMean + gUnc, gMean - gUnc)
    A = uniform(AMean + AUnc, AMean - AUnc)
    C = uniform(CMean + CUnc, CMean - CUnc)
    p = uniform(pMean + pUnc, pMean - pUnc)
    A2 = uniform(A2Mean + A2Unc, A2Mean - A2Unc)
    C2 = uniform(C2Mean + C2Unc, C2Mean - C2Unc)
    
    y=[0]
    v=[0]
    #th=90
    
    vy=0#sin(th*pi/180)*v[0]
    #vx=0#sin(th*pi/180)*v[0] #####
    x=[0]
    #ax=0
    ay=0.
    a=[0.]
    
    t=[0]
    dt=0.01
    def FD(v,vn,A,C):
        return .5*p*A*C*v*vn
    k=0
    while thrustA8(t[k])/(mr*mass(t[k])) < abs(g):
        t.append(t[-1]+dt)
        y.append(0)
        x.append(0) #####
        v.append(0)
        a.append(0)
        k+=1
    hasFuel=1
    #plt.plot(t[k],y[k],'.') ##
    while y[k]>=0:
        y.append(y[-1]+vy*dt)
        #x.append(x[-1]+vx*dt) #####
        t.append(t[-1]+dt)
        
        if hasFuel==1:
            if (thrustA8(t[k]) == 0):
                C=C2
                A=A2
                hasFuel=0
                #plt.plot(t[k],y[k],'.') ##
        
        vy+=ay*dt
        #vx+=ax*dt #####
        v.append(vy) ##
        #v.append(sqrt(vx**2+vy**2))
        #ax=-FD(v[-1],vx,A,C)/(mr*mass(t)) #####
        if vy>=0:
            ay=-g + (thrustA8(t[k])-FD(v[-1],vy,A,C))/(mr*mass(t[k]))
        else:
            ay=-g + (thrustA8(t[k])+FD(v[-1],vy,A,C))/(mr*mass(t[k]))
        a.append(ay)
        
        k1=vy
        k2=A
        k3=C
        
        k+=1
    
    if y[k]<0:
        y[k]=0
    
    #plt.subplot(121)
    plt.plot(t,y)
    #plt.show()
    
    endTimes[i]=t[k]

# For first plot
plt.xlabel("Time")
plt.ylabel("Height")
plt.title("Rocket Height Simulations\nOver Time")


# For second plot
plt.subplot(122)
n_bins = 10
minim = round(min(endTimes),5)
maxim = round(max(endTimes), 5)
bin_width = round((maxim-minim) / float(n_bins), 5)
plt.hist(endTimes, bins=n_bins)
plt.xlabel("End Time")
plt.ylabel("Count")
plt.title("Histogram of Landing Times; 10 bins\n min: " + str(minim) + ", max: " + str(maxim) + ", bin width: " + str(bin_width))
plt.show()
