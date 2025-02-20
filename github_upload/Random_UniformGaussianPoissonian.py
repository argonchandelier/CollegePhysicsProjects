# Logan Richan
# ph336

from numpy.random import normal, random, poisson
from numpy import exp
from matplotlib import pyplot as plt
from math import factorial

nmax=100000

uniform=[random() for i in range(nmax)]
gaussian=[normal(0,1) for i in range(nmax)]
poissonian=[poisson(2) for i in range(nmax)]

plt.figure(1)
plt.hist(uniform)

plt.figure(2)
plt.hist(gaussian,bins=21)

plt.figure(3)
plt.hist(poissonian)

#poissonCheck:

expected3=2**(3)*exp(-2)/float(factorial(3))*nmax
expected5=2**(5)*exp(-2)/float(factorial(5))*nmax
print(expected3, expected5)


plt.show()
