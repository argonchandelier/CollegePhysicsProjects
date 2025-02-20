# Logan Richan
# ph336

import numpy as np
from matplotlib import pyplot as plt
from scipy import interpolate as intp

plt.close('all')

x=[1.0,2.5,3.5,7.0,11.2,15.1]
y=[2.6,4.8,5.1,4.9,9.6,12.3]
plt.plot(x,y,'bo')

flin=intp.interp1d(x,y)

xeval=np.linspace(1.0,15.1,300)
plt.plot(xeval,flin(xeval),'-b',label='linear')

fcubic=intp.interp1d(x,y,kind='cubic')  # cubic spline
plt.plot(xeval,fcubic(xeval),'-g',label='cubic')

print(flin(3.0))
print(flin(9.0))
print(fcubic(3.0))
print(fcubic(9.0))

plt.legend()

plt.show()