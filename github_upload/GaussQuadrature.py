# Logan Richan
# ph295

from gaussxw import gaussxw
from math import sqrt, cos

N=100
a=0
b=1
x,w=gaussxw(N)
xp=0.5*(b-a)*x+0.5*(b+a)
wp=0.5*(b-a)*w
I=0

def f(x):
    f=(cos(sqrt(100*x))**2)
    return f
    
for k in range(0,N):
    I+=wp[k]*f(xp[k])
    print(I)

print(I)
