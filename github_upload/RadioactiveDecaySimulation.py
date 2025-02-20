# Logan Richan
# Ph295 assignment

from random import random
from numpy import arange, zeros, log, sort
from matplotlib import pyplot as plt
from datetime import datetime
start=datetime.now()

# Constants
tau=3.053*60
u=log(2)/tau

# Get the decay times of Tl
Natoms=100000
Rand=zeros(Natoms,float)
for i in range(Natoms):
    Rand[i]=random()
Rand=sort(Rand)
TlTimes=zeros(Natoms,float)
TlTimes=-(1./u)*log(1-Rand) # Eq. 2

# Set up graph
dt=1 #seconds
tmax=tau*10
tPts=arange(0,tmax,dt)
Ntimes=len(tPts)
TlPts=zeros(Ntimes,int)
PbPts=zeros(Ntimes,int)

# Get points
Ndecay=0
i=0
for t in tPts:
    while Ndecay<Natoms and TlTimes[Ndecay]<t:
        Ndecay+=1
    PbPts[i]=Ndecay
    TlPts[i]=Natoms-Ndecay
    i+=1

plt.plot(tPts,TlPts)
plt.plot(tPts,PbPts)

plt.gca().legend(("Tl","Pb"))
plt.xlabel("Time (s)")
plt.ylabel("Number of particles")
plt.show()

print(datetime.now()-start)