# Logan Richan
# ph295

from numpy import arange,zeros,array
from matplotlib import pyplot as plt

def fact(n): # Factorial function
    x=1
    for i in range(1,n+1):
        x*=i
    return x

def Bessel(n,x): # The Bessel function
    J=0
    for m in range(20):
        J += ((-1)**m)/float(fact(m)*fact(n+m)) * (x/2.)**(2*m+n)
    return J

k3=array([8.6537,10.1735,11.6198],float) # k3 values for the first 3 Bessel functions
def graph(n): # Graph a Bessel function from x=0 to x=10
    xpts=arange(0,10+0.1,0.1)
    Jpts=zeros(101,float)
    i=0
    for x in xpts:
        Jpts[i]=Bessel(n,x*(k3[n]/10.)) # Getting Bessel function values and fixing the boundary at x=10
        i+=1
    plt.plot(xpts,Jpts)

for n in range(0,3): # Graph the first 3 Bessel functions
    graph(n)

plt.gca().legend(("J0","J1","J2"))
plt.show()
