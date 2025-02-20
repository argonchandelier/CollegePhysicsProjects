# Logan Richan
# ph295

from numpy import pi, sin, zeros, arange
from matplotlib import pyplot as plt

A=10 #in C
B=12
tau=365 #days
D=0.1

a=0
b=20
N=50
h=(b-a)/float(N-1) # distance step in meters
yPts=arange(a,b+h,h)
Tpts=zeros(N,float)

dt=.5 # time step in days
#print(h)
c=dt*D/(float(h)**2) #causes errors if too large, probably due to rounding error in the "j" loop
print(c)

def TptsCalc(t):
    T = A+B*sin(2*pi*t/tau)
    return T

Tpts[0]=TptsCalc(0) #10 #=TptsCalc(0) == 10
Tpts[1:N-1]=10
Tpts[N-1]=11

Tpts2=Tpts

fig=1
#t=1
tPts=arange(dt,3650,dt)
T0before=diffBefore=0
#for t in range(1,365*10):
for t in tPts:
    #Tpts2[1:N-1]=Tpts[1:N-1] + c*(Tpts[0:N-2]+Tpts[2:N]-2*Tpts[1:N-1])
    Tpts2[0]=TptsCalc(t)
    for j in range(1,N-1):
        Tpts2[j] = Tpts[j] + c*(Tpts[j+1]+Tpts[j-1]-2*Tpts[j])
    Tpts=Tpts2
    
    #if t>=365*9 and (t-365*9)%(365/4)==0:
    if t>=365*9 and (((Tpts[0]-T0before)>=0 and diffBefore<0) or ((Tpts[0]-T0before)<=0 and diffBefore>0) or (Tpts[0]>=10 and T0before<10) or (Tpts[0]<=10 and T0before>10)):
        #(Tpts[0]>=before and Tpts[0]<before) or (Tpts[0]<=before and Tpts[0]>before)
        plt.figure(fig)
        plt.plot(yPts, Tpts)
        #plt.show()
        #fig+=1
        print(t)
        plt.gca().legend(("Year 10 start","3 months into Year 10","6 months into Year 10","9 months into Year 10"))#,"Year 10 end"))
    #t+=dt
    diffBefore=Tpts[0]-T0before
    T0before=Tpts[0]
    

#plt.plot(yPts, Tpts)###
#print(Tpts)
plt.xlabel("Depth (m)")
plt.ylabel("Temperature (C)")
plt.show()
