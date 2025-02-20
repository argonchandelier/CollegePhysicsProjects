# Logan Richan
# ph295

from numpy import zeros, arange
from matplotlib import pyplot as plt
from datetime import datetime

start=datetime.now()

D=1.172e-5 # Thermal diffusivity in m^2/s
N=125 # Number of sections of the beam used

# Beam range
a=0.
b=4.68
dx=(b-a)/float(N)
x=arange(a,b,dx)

# Initial Temperatures of the beam
T=zeros(N,float)
T[0]=135
T[1:(N-1)]=22.5
T[N-1]=22.5
Tnew=T

# Set up diffusion variables
dt=0.1
c=dt*D/(dx**2)
t=0

# Diffusion calculation using FTCS method
while T[int(N/2)]<50.0: 
    for i in range(1,N-1):
        Tnew[i] = T[i] + c*(T[i+1]+T[i-1]-2*T[i])
    T=Tnew
    t+=dt

print(t) # Find the total time

plt.plot(x,T)
plt.xlabel("Distance from fire on beam (in m)")
plt.ylabel("Temperature (in C)")
print(datetime.now()-start) # ~5 min
plt.show()
