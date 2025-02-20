# Logan Richan
# ph295

from random import random
from numpy import arange, zeros
from matplotlib import pyplot as plt
from datetime import datetime
start=datetime.now()

h=1.
tau1=46.*60.
tau2=2.2*60.
tau3=3.3*60.

p1=1-2**(-h/tau1)
p2=1-2**(-h/tau2)
p3=1-2**(-h/tau3)

tmax=20000
tPts=arange(0,tmax,h)
N=len(tPts)

Natoms=10000
BiPts=zeros(N,int)
TlPts=zeros(N,int)
PbPts=zeros(N,int)
BiFPts=zeros(N,int)
BiPts[0]=Natoms
TlPts[0]=0
PbPts[0]=0
BiFPts[0]=0

i=0
for t in range(len(tPts)-1):
    i+=1
    decay1=0
    decay2=0
    decay3=0
    decay4=0
    for j in range(BiPts[i-1]):
        if p1>random():
            x=random()
            if x<0.9791:
                decay1+=1
            else:
                decay2+=1
    for j in range(TlPts[i-1]):
        if p2>random():
            decay3+=1
    for j in range(PbPts[i-1]):
        if p3>random():
            decay4+=1
    BiPts[i]=BiPts[i-1]-decay1-decay2
    TlPts[i]=TlPts[i-1]-decay3+decay2
    PbPts[i]=PbPts[i-1]-decay4+decay1+decay3
    BiFPts[i]=BiFPts[i-1]+decay4

plt.plot(tPts,BiPts)
plt.plot(tPts,TlPts)
plt.plot(tPts,PbPts)
plt.plot(tPts,BiFPts)
plt.xlabel("Time (s)")
plt.ylabel("Number of particles")
plt.gca().legend(("Bi-213","Tl","Pb","Bi-209"))
plt.show()
print(datetime.now()-start)