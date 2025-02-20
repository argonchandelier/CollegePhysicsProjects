# Logan Richan
# ph336

import numpy as np
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt

plt.close('all')

y = [0.500, 0.700, 0.900, 1.100, 1.300, 1.500, 1.700, 1.900, 2.100] 
t = [0.34, 0.40, 0.44, 0.49, 0.56, 0.60, 0.64, 0.69, 0.72]

def f(x,a,b):
    return(a*np.log(np.cosh(b*x)))

guess=[1,1]

fit,error=curve_fit(f,t,y,p0=guess)

print(fit)
print("vter = ", (fit[0]*9.8004)**(0.5))

plt.plot(t,y,'ob')
X=np.linspace(0.34,0.72)
plt.plot(X,f(X,*fit),'--r')
plt.show()
