# Logan Richan
# ph336

import numpy as np
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt

plt.close('all')

x = [5.0, 5.4, 5.8, 6.2, 6.6, 7.0, 7.4, 7.8, 8.2, 8.6, 9.0, 9.4, 9.8, 10.2] 
y = [0.22, 0.82, 2.10, 4.35, 7.56, 10.60, 12.38, 11.70, 9.18, 5.85, 3.11, 1.35, 0.44, 0.15]

def f(x,A,mu,sigma):
    return(A * 1/float(sigma*np.sqrt(2*np.pi)) * np.exp(-0.5 * ((x-mu)/float(sigma))**2))

guess=[1,1,1]

fit,error=curve_fit(f,x,y,p0=guess)

print("A, mu, sigma: ", fit)
print("With errors:", np.sqrt(np.diag(error)))

plt.plot(x,y,'ob')
X=np.linspace(5.,10.5)
plt.plot(X,f(X,*fit),'--r')
plt.show()
