# Logan Richan
# ph336

import numpy as np
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt

plt.close('all')

t = [0.5, 1.0, 1.5, 2.0, 2.5, 3.0, 3.5, 4.0, 4.5, 5.0, 5.5, 6.0, 6.5, 7.0, 7.5, 8.0, 8.5, 9.0, 9.5,\
10.0, 10.5, 11.0, 11.5, 12.0, 12.5, 13.0, 13.5, 14.0, 14.5, 15.0, 15.5, 16.0, 16.5, 17.0,\
17.5, 18.0, 18.5, 19.0, 19.5, 20.0] 
counts = [816, 733, 660, 593, 539, 498, 440, 407, 374, 334, 312, 279, 250, 237, 218, 187, 179,\
168, 163, 144, 142, 127, 117, 118, 108, 98, 85, 86, 90, 81, 74, 71, 73, 57, 56, 56, 62,\
58, 62, 61]

def f(x,halfL,A,k):
    return(A * 0.5**(x/float(halfL)) + k)

guess=[1,1,1]

fit,error=curve_fit(f,t,counts,p0=guess)

print(fit) # half life of 3.226 min, background = k = 45
print("errors:",np.sqrt(np.diag(error)))

plt.plot(t,counts,'ob')
X=np.linspace(0,20.5)
plt.plot(X,f(X,*fit),'--r')
plt.show()
