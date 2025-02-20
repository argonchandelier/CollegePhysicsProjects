# Logan Richan
# ph295

from matplotlib import pyplot as plt
from numpy import arange, zeros

a=0.
b=20.
N=100
h=(b-a)/float(N-1)
zPoints=arange(a,b+h,h)
Jpoints=zeros(N,float)

def fact(x):
    z=1
    for i in range(1,x+1):
        z*=i
    return z

mMax=50
def Bessel(n,z):
    sum=0
    for m in range(0,mMax):
        sum+=(float((-1)**m)) / float(fact(m)*fact(m+n)) * float((z/2)**(2*m+n))
    return sum

for n in range(5):
    i=0
    for z in zPoints:
        Jpoints[i]=Bessel(n,z)
        i+=1
    plt.plot(zPoints,Jpoints)
    plt.gca().legend(("J0", "J1", "J2", "J3", "J4"))
plt.show()
