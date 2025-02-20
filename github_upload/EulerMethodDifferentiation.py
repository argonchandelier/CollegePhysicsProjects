# Logan Richan
# ph295

from numpy import sin, arange
from matplotlib import pyplot as plt

def f(x,t):
    f=x**(.5)+sin(t)
    return f

a=0.
b=1000.
N=1000
h=(b-a)/N
xpt=[]
time=arange(a,b,h)
x=1
for t in time:
    xpt.append(x)
    x+=h*f(x,t)
    
plt.plot(time,xpt)
print(x)
plt.show()
