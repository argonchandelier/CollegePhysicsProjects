# Logan Richan
# ph385

from numpy import linspace,sin,cosh

N=100
a=0.
b=5.
x,dx=linspace(a,b,N,retstep=True)
#dx = (b-a)/float(N)
y=sin(x)*cosh(x)
yprime = (y[2:]-y[:-2])/(2*dx)
print(yprime)
