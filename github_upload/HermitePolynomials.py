# Logan Richan
# ph 295

from numpy import zeros,arange,pi,sqrt,e
from math import factorial
from matplotlib import pylab as plt
from gaussxw import gaussxwab
from datetime import datetime

start=datetime.now()

def H(n,x): #the given Hermite polynomial function
    H=zeros(n+1,float)
    H[0]=1
    if n>=1:
        H[1]=2*x
    if n>=2:
        for i in range(2,n+1):
            H[i]=2*x*H[i-1]-2*(i-1)*H[i-2]
    return H[n]

def Psi(n,x): #the given wave function
    psi=(((2**n)*factorial(n)*sqrt(pi))**(-1./2.)) * (e**((x**2)/(-2.))) * H(n,x)
    return psi

def plots(h,a,b,n0,nf): #plotting the wave functions from n=n0 to n=nf
    N=(b-a)*int(1/h)+1
    xArray=zeros(N,float)
    PsiArray=zeros(N,float)
    for n in range(n0,nf+1):
        i=0
        for x in arange(a,b+h,h):
            xArray[i]=x
            PsiArray[i]=Psi(n,x)
            i+=1
        plt.plot(xArray,PsiArray)
        plt.gca().legend((n0,n0+1,n0+2,n0+3)) #will label the first 4 waves
    plt.show()

def ToBeIntegrated(n,x): #the function being integrated in part c
    f=(x**2)*((Psi(n,x))**2)
    return f

def integ(f,a,b,n): #integrating using Gaussian quadrature
    N=100
    x,w=gaussxwab(N,a,b)
    I=0
    for i in range(0,N):
        I+=w[i]*f(n,x[i])
    return I

def deriv(f,n,x): #taking the derivative to find where the given function smooths out
    h=0.01
    der=(f(n,x+h/2)-f(n,x-h/2))/h
    return der

def findMinOrMax(f,h,n): #approximating where the the given function goes to and stays at 0 (so that a finite limit can be approximated from an infinite one)...
    about0=10**(-8)
    func=1
    der=1
    m=0
    while func>about0 or der>about0:
        m+=h
        func=f(n,m) #...by finding where the function is about 0...
        der=deriv(f,n,m) #...at the same time its slope is about 0
        if func<0: #making sure to take absolute values
            func*=-1
        if der<0:
            der*=-1
    return m

def RMSpos(n): #using the definition for the root-mean-square position
    h=0.01
    a=findMinOrMax(Psi,-h,n)
    b=findMinOrMax(Psi,h,n)
    
    rms=sqrt(integ(ToBeIntegrated,a,b,n))
    return rms

plots(0.01,-4,4,0,3) # part a
runtime=datetime.now()-start

start2=datetime.now()
plots(0.01,-10,10,30,30) # part b
runtime2=datetime.now()-start2


n=int(input("n = ")) # part c
start3=datetime.now()
rms=RMSpos(n)
print("root mean square pos:", rms)
runtime3=datetime.now()-start3

print(runtime)
print(runtime2)
print(runtime3)
