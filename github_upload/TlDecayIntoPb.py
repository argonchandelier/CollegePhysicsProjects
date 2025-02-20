# Logan Richan
# ph295

from random import random
from numpy import arange, zeros
from matplotlib import pyplot as plt
from datetime import datetime
start=datetime.now()

h=1
tau=3.053*60

p=1-2**(-h/tau)

tmax=tau*10
tPts=arange(0,tmax,h)
N=len(tPts)

Natoms=1000
TlPts=zeros(N,int)
PbPts=zeros(N,int)
TlPts[0]=Natoms
PbPts[0]=0
#pts=zeros(N,float) ###

i=0
for t in range(len(tPts)-1):
    i+=1
    decay=0
    for j in range(TlPts[i-1]):
        if p>random():
            decay+=1
    TlPts[i]=TlPts[i-1]-decay
    PbPts[i]=PbPts[i-1]+decay
    #pts[i]=uniform(0,1)
    
#print(pts)
#print(TlPts)
plt.plot(tPts,TlPts)
plt.plot(tPts,PbPts)
plt.gca().legend(("Tl","Pb"))
plt.show()
print(datetime.now()-start)