# Logan Richan
# ph295

from numpy import sin, array, arange, zeros,pi,log
from matplotlib import pylab as plt


a=2.
b=5.
N=100
h=(b-a)/float(N)
tpoints=arange(a,b,h)
x=1.
xact=25/(4+3*log(2)-3*log(5))
print(xact)

def f(x,t):
    return 2*x/t+3*x**2/t**3

def Euler(x):
    for t in tpoints:
        x+=h*f(x,t)
    return x

def O2(x):
    for t in tpoints:
        k1=h*f(x,t)
        k2=h*f(x+0.5*k1, t+0.5*h)
        x+=k2
    return x

def O4(x):
    for t in tpoints:
        k1=h*f(x, t)
        k2=h*f(x+0.5*k1, t+0.5*h)
        k3=h*f(x+0.5*k2, t+0.5*h)
        k4=h*f(x+k3, t+h)
        x+=(k1+ 2*k2+ 2*k3+ k4)/6
    return x

x1=Euler(x)
x2=O2(x)
x4=O4(x)

print(x1, (xact-x1)/xact*100)
print(x2, (xact-x2)/xact*100)
print(x4, (xact-x4)/xact*100)

def P(n,x):
    y=0
    if n==0:
        y= 1
    elif n==1:
        y= x
        print(x)
    elif n==2:
        y= 0.5*(3.*x**2-1)
    elif n==3:
        y= 0.5*(5.*x**3-3*x)
    elif n==4:
        y= (1./8.)*(35*x**4-30*x**2+3)
    elif n==5:
        y= (1./8.)*(63*x**5-70*x**3+15*x)
    return y
    

def graph(n):
    a=-1.
    b=1.
    N=100
    h=(b-a)/float(N)
    xvalues=arange(-1,1+h,h)
    Pnxvalues=zeros(N+1,float)
    i=0
    for x in xvalues:
        Pnxvalues[i]=P(n,x)
        i+=1
    plt.plot(xvalues,Pnxvalues,label='i')
    plt.gca().legend(('P_0','P_1','P_2','P_3','P_4','P_5'))
    plt.xlabel('x')
    plt.ylabel('P_n(x)')

for n in range(0,6):
    graph(n)

plt.show()
