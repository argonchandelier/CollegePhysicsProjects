# Logan Richan
# ph150
# Drag and Uncertainties

'''
NOTES:

Uncertainties:
-radius
-mass
-drag constant
-initial height
-air density


'''

#From ph150c10lab:

from numpy import sqrt,cos,sin,pi
from matplotlib import pyplot as plt
from random import uniform

#m=.415kg, A=0.392m^2, large ball
#Large, small, blue, 
mv=[0.415,0.08,0.0117,.0451]
Av=[0.392,0.096,2.11e-5,2.87e-5]
tv=[0,0,0,0]
for i in range(0,1):
    mMean=mv[i]#.415 #kg
    mUncertainty=mMean/10.
    
    AMean=Av[i]#0.392 # Cross sectional area
    AUncertainty=AMean/10.
    
    pMean=.7364 # density 1.29 kg/m^3 #.7364 at 5000ft elevation
    pUncertainty=.15
    
    CMean=.5 # Drag coefficient, depends on the geometry of the object
    CUncertainty=.1
    
    gMean=9.8
    gUncertainty=0.15
    
    hMean=16.9
    hUncertainty=0.5
    #####

    n=200
    for j in range(n):
        m = uniform(mMean - mUncertainty, mMean + mUncertainty)
        A = uniform(AMean - AUncertainty, AMean + AUncertainty)
        p = uniform(pMean - pUncertainty, pMean + pUncertainty)
        C = uniform(CMean - CUncertainty, CMean + CUncertainty)
        g = uniform(gMean - gUncertainty, gMean + gUncertainty)
        h = uniform(hMean - hUncertainty, hMean + hUncertainty)
        
    
        #####
        y=[h]
        v=[20] # velocity
        th=45
        vx=cos(th*pi/180)*v[0]
        vy=sin(th*pi/180)*v[0]
        print(vx,vy)
        
        x=[0]
        ax=0
        ay=0
        
        t=[0]
        dt=.01
        
        # x.append(x[-1]+vx[-1]*dt)
            
        def FD(v,vn):
            return .5*p*A*C*v*vn
        k=0
        while y[k]>0:
            yValue=y[-1]+vy*dt
            if yValue > 0:
                #print(yValue)
                y.append(yValue)                
                t.append(t[-1]+dt)
                x.append(x[-1]+vx*dt)
                '''
                if yValue>0:
                    y.append(yValue)
                else:
                    y.append(0)
                    '''
                vy+=ay*dt
                vx+=ax*dt
                v.append(sqrt(vx**2+vy**2))
                ax=-FD(v[-1],vx)/m
                ay=-g - FD(v[-1],vy)/m
                '''
                if y>=0:
                    plt.plot(t,y)
                else:
                    plt.plot(t,0)
                '''
                k+=1
            else:
                y[k]=0
        #print(vx)
        #t.append(t[-1]+dt)
        #y.append(0)
        #plt.subplot(121)
        plt.plot(x,y)
        
        #plt.subplot(122)
        #plt.plot(t,x)
        
        ##plt.show()
        tv[i]=t
        #print('Big Beach Ball Time: {:8.3f}'.format(tv[0]))
    '''
    print('Small Beach Ball Time: {:8.3f}'.format(tv[1]))
    print('Blue Ball Time: {:8.3f}'.format(tv[2]))
    print('Styrofoam Time: {:8.3f}'.format(tv[3]))
    '''

plt.show()

'''
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


for j in range(200):
    c = uniform(cMean - cUncertainty, cMean + cUncertainty)
    x = uniform(xMean - xUncertainty, xMean + xUncertainty)
    v = uniform(vMean - vUncertainty, vMean + vUncertainty)
    
    #Note: Ideally, when v reaches a certain point, cos(v**2)=0,
    #   so ax=0, and velocity will never change from that point on.
    #   This can be shown for extremely small dt values, but would
    #   take too long to compute
    def axCalc(v,t):
        ax=c*cos(v**2)*(t**(1.5))
        #print(v**2,t**(1.5),ax,cos(v**2))
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
    plt.subplot(121)
    plt.plot(tvalues,xvalues)
    plt.show()
    
    endXvalues[j]=x
print(endXvalues)
plt.subplot(122)
plt.hist(endXvalues, bins=10)
plt.show()

'''



