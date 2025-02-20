# Logan Richan
# ph295

from numpy import tanh,cosh,arange,zeros
from matplotlib import pyplot as plt

h=0.01 #Step size in Central differences method

def y(x):
    f=1+0.5*tanh(2*x)
    return f

def dydx(y,x):
    der=(y(x+h/2)-y(x-h/2))/h
    return der

def g(x):
    g=(cosh(2*x))**(-2)
    return g

a=-2
b=2
h2=0.01 #step size in graphing
arraySize=int(((b-a)/h2)+1)

xArray=zeros(arraySize,float)
fArray=zeros(arraySize,float)
dfdxArray=zeros(arraySize,float)
gArray=zeros(arraySize,float)

i=0

for x in arange(a,b+h2,h2):
    xArray[i]=x
    fArray[i]=y(x)
    dfdxArray[i]=dydx(y,x)
    gArray[i]=g(x)
    i+=1

plt.plot(xArray,fArray,label='y(x)')
plt.plot(xArray,dfdxArray,label='dy/dx Estimated')
plt.plot(xArray,gArray,'b',linestyle='dashed',label='dy/dx Actual')
plt.legend(loc='upper left')

plt.show()