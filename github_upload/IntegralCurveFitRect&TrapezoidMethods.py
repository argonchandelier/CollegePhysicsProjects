# Logan Richan
# ph336

import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
import scipy as sci

def linfit(x,a0,a1):
    return (a0 + a1*x)
guess1=[1,1]

x = np.array([5.0, 10.0, 15.0, 20.0, 25.0, 30.0, 35.0, 40.0]) * 0.01
F = np.array([1.9, 3.7, 5.6, 7.3, 9.2, 11.0, 12.9, 14.6])

plt.figure(1)
plt.plot(x,F,'.b')

fit,error=curve_fit(linfit,x,F,p0=guess1)
plt.plot(x,linfit(x,*fit),'--r')

print("k = " + str(fit[1]))

# part b

rectAppx = sum((x[1:]-x[:-1])*F[:-1])
trapAppx = sum((x[1:]-x[:-1])*(F[1:]+F[:-1])/2.)
print("rect appx:", rectAppx)
print("trap appx:", trapAppx)

# part c

def comp(x):
    return (0.5*fit[1]*x**2)
    
print("Using 1/2 kx^2:", comp(0.4)-comp(0.05))

# part d

def Integ(x):
    return fit[0]*x + fit[1]*x**2/2.
print("Integrated:", Integ(0.4) - Integ(0.05))

plt.show()
