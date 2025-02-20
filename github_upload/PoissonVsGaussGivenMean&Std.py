# Logan Richan
# ph336
# Problem 1

from matplotlib import pyplot as plt
from numpy import mean, std, exp, pi
from math import factorial, gamma

# Inputs
u=100.
sigma=u**0.5
N=250

P1=[]
G1=[]
X=[]

for x in range(N):
    X.append(x)
    
    P1.append(u**x*exp(-u)/factorial(x))
    G1.append((2*pi*sigma**2)**(-0.5)*exp(-(x-u)**2/(2*sigma**2)))
plt.plot(X,P1)
plt.plot(X,G1)
plt.show()