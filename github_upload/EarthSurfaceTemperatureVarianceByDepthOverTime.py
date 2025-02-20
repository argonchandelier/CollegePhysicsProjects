# Logan Richan
# ph295

from numpy import pi, sin, zeros, arange
from matplotlib import pyplot as plt

# CONSTANTS
A=10 #in C
B=12
tau=365 #days
D=0.1

# POINTS
a=0
b=20
N=50
dy=(b-a)/float(N-1) # distance step in meters
yPts=arange(a,b+dy,dy)
Tpts=zeros(N,float)

# TIME STEP AND C
dt=1 # time step in days
c=dt*D/(float(dy)**2) #h*D/a^2 in original equation (Eq.3)
print(c)

# EQUATION 1
def TptsCalc(t):
    T = A+B*sin(2*pi*t/tau)
    return T

# STARTING POINTS
Tpts[0]=TptsCalc(0) # =10 
Tpts[1:N-1]=10
Tpts[N-1]=11
Tpts2=Tpts

# FTCS method
tPts=arange(0,tau*10,dt) #from 0-10 years with dt step size
T0before=diffBefore=0
for t in tPts: # iteration throughout time
    Tpts2[0]=TptsCalc(t)
    for j in range(1,N-1): # iteration throughout depth
        Tpts2[j] = Tpts[j] + c*(Tpts[j+1]+Tpts[j-1]-2*Tpts[j]) # Eq. 3 iteration
    Tpts=Tpts2
    
    #When to plot
    #if t>=365*9 and (t-365*9)%(365/4)==0: # t integer logic
    if t>=365*9 and (((Tpts[0]-T0before)>=0 and diffBefore<0) or ((Tpts[0]-T0before)<=0 and diffBefore>0) or (Tpts[0]>=10 and T0before<10) or (Tpts[0]<=10 and T0before>10)): # t float logic
        plt.plot(yPts, Tpts) # Plot
    diffBefore=Tpts[0]-T0before #used in float logic
    T0before=Tpts[0]            #

# Labels
plt.gca().legend(("Year 10 start","3 months into Year 10","6 months into Year 10","9 months into Year 10","Year 10 end"))
plt.xlabel("Depth (m)")
plt.ylabel("Temperature (C)")
plt.show()
