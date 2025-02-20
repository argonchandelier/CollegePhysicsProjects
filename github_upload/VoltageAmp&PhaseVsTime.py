from numpy import array,zeros,e,arange
from cmath import polar
from numpy.linalg import solve
from matplotlib import pyplot as plt
from datetime import datetime

start=datetime.now()

R1=1e3 #in Ohms
R2=2e3
R3=1e3
R4=2e3
R5=1e3
R6=2e3

C1=1e-6 #in Farads
C2=0.5e-6

xPlus=3 #in Volts
omega=1000 #in s^-1

R=array([1,R1,R2,R3,R4,R5,R6],float)
Rinv=1./R
C=array([1,C1,C2],float)
iwC=1j*omega*C

A = array([[(Rinv[1]+Rinv[4]+iwC[1]), -iwC[1]                        , 0                       ],
           [-iwC[1]                 , (Rinv[2]+Rinv[5]+iwC[1]+iwC[2]), -iwC[2]                 ],
           [0                       , -iwC[2]                        , (Rinv[3]+Rinv[6]+iwC[2])]], complex)
           
v = xPlus * array([Rinv[1], Rinv[2], Rinv[3]], float)

x = solve(A,v)
print(x)

#V=Acos(wt+phaseconstant)
#Use polar of x (not V)
for i in range(0,3):
    r2,theta2=polar(x[i])
    print(r2)
    print(theta2)

period=zeros(3,float)
for i in range(0,3):
    j=0
    X=10000
    r=zeros(X,float)
    theta=zeros(X,float)
    Vvalues=zeros(X,complex)
    tValues=zeros(X,float)
    k=1
    diff=zeros(2,float)
    a=float(0)
    b=float(.02)
    for t in arange(a,b,(b/X)):
        Vvalues[j] = x[i]*e**(1j*omega*t)
        r[j],theta[j] = polar(Vvalues[j])
        tValues[j] = t
        if (j-1)>0 and k<3: #period calculation
            if theta[j-1]>=0 and theta[j]<0:  
                diff[k-1]=tValues[j]
                if k==2:
                    period[i]=diff[1]-diff[0]  
                k+=1
        j+=1
    plt.figure(1)
    plt.plot(tValues,r)
    plt.gca().legend(("V1 Amplitude","V2 Amplitude","V3 Amplitude"))
    plt.figure(2)
    plt.plot(tValues,theta)
    plt.gca().legend(("V1 Phase", "V2 phase", "V3 phase"))
    print("Voltage", i+1, " amplitude = ", r[0], " period = ", period[i])

print(datetime.now()-start)
plt.show()

