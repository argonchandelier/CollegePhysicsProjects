# Logan Richan
# ph295

from numpy import zeros, arange
from matplotlib import pyplot as plt

def ILeftGraph(f,a,b):
    N=20.
    h=(b-a)/N
    I=0
    for x in arange(a,b,h):
        y=f(x)
        I+=y*h
        plt.plot([x,x,x+h,x+h],[0,y,y,0])
    #plt.show()
    return I

def graph(f,a,b):
    N=1000
    h=(b-a)/(N-1)
    xvalues=zeros(N,float)
    yvalues=zeros(N,float)
    i=0
    for x in arange(a,b+h,h):
        xvalues[i]=x
        yvalues[i]=f(x)
        i+=1
    plt.plot(xvalues,yvalues)
    #plt.show()

def f(x):
    y=.1682*x**3-1.674*x**2+5.123*x-3.431
    return y


answer=ILeftGraph(f,0,5.492)
print(answer)
graph(f,0,5.492)
plt.show()
