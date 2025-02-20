# Logan Richan
# ph336

import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
from scipy import interpolate as intp

plt.close('all')
x=[2.5, 2.6, 2.7, 2.8, 2.9, 3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7, 3.8, 3.9, 4.0, 4.1, 4.2,
4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 5.0, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 5.8, 5.9, 6.0]
y=[0.00, 0.89, 1.65, 2.31, 2.91, 3.52, 4.18, 4.92, 5.60, 6.02, 6.09, 5.91,
5.70, 5.59, 5.58, 5.64, 5.71, 5.78, 5.84, 5.89, 5.93, 5.95, 5.98, 5.99,
6.00, 6.01, 6.00, 5.99, 5.98, 5.97, 5.95, 5.93, 5.91, 5.88, 5.86, 5.83]

x2=[2.5, 2.6, 2.7, 2.8, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8,
4.9, 5.0, 5.1, 5.2, 5.3, 5.4, 5.5, 5.6, 5.7, 5.8, 5.9, 6.0]
y2=[0.00, 0.89, 1.65, 2.31, 5.71, 5.78, 5.84, 5.89, 5.93, 5.95, 5.98, 5.99,
6.00, 6.01, 6.00, 5.99, 5.98, 5.97, 5.95, 5.93, 5.91, 5.88, 5.86, 5.83]

plt.plot(x,y,'bo') # peak wavelength at 3.5 Angstroms

xeval=np.linspace(2.5,6.0,300) # evaluate on a much finer mesh than the original data set to get a better plot

fcubic=intp.interp1d(x2,y2,kind='cubic')  # cubic spline
expected_baseline_intensities = fcubic(xeval)

plt.plot(xeval,expected_baseline_intensities,'-g',label='cubic')
plt.xlabel("wavelength in Angstroms")
plt.ylabel("Intensity")

yBackgr=[0.00, 0.89, 1.65, 2.31, fcubic(2.9), fcubic(3.0), fcubic(3.1), fcubic(3.2),
fcubic(3.3), fcubic(3.4), fcubic(3.5), fcubic(3.6), fcubic(3.7), fcubic(3.8), fcubic(3.9), 
fcubic(4.0), 5.71, 5.78, 5.84, 5.89, 5.93, 5.95, 5.98, 5.99, 6.00, 6.01, 6.00, 5.99, 5.98,
5.97, 5.95, 5.93, 5.91, 5.88, 5.86, 5.83]

y3 = np.array(y) - np.array(yBackgr)

def f(x,A,mu,sigma):
    return(A * 1/float(sigma*np.sqrt(2*np.pi)) * np.exp(-0.5 * ((x-mu)/float(sigma))**2))

guess=[1,3.5,1]

fit,error=curve_fit(f,x,y3,p0=guess)

print("A, mu, sigma: ", fit)
print("With errors:", np.sqrt(np.diag(error)))

isolated_rel_intensities = f(xeval,*fit)
plt.plot(xeval, isolated_rel_intensities+expected_baseline_intensities, '--m')


plt.figure(2)
plt.xlabel("wavelength in Angstroms")
plt.ylabel("Intensity")
plt.title("Isolated Emission Peak")
plt.plot(x,y3,'ob')
plt.plot(xeval,isolated_rel_intensities,'--r')
plt.show()
# The peak is now estimated to be at 3.4 Angstroms, which is slightly lower than the previous estimate