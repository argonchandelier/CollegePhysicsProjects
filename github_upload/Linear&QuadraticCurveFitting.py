# Logan Richan
# ph336

import numpy as np
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit

def linfit(x,a0,a1):
    return (a0 + a1*x)
guess1=[1,1]

def quadfit(x,a0,a1,a2):
    return (a0 + a1*x + a2*x**2)
guess2=[1,1,1]

t = np.array([0.0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6, 0.7, 0.8, 0.9, 1.0, 1.1, 1.2, 1.3, 1.4, 1.5, 1.6, 1.7, 1.8,
1.9, 2.0, 2.1, 2.2, 2.3, 2.4, 2.5, 2.6, 2.7, 2.8, 2.9, 3.0, 3.1, 3.2, 3.3, 3.4, 3.5, 3.6, 3.7,
3.8, 3.9, 4.0, 4.1, 4.2, 4.3, 4.4, 4.5, 4.6, 4.7, 4.8, 4.9, 5.])

x = np.array([6.29, 6.52, 6.58, 6.79, 6.9, 6.89, 7.05, 7.00, 7.18, 7.36, 7.58, 7.72, 7.78, 7.95, 7.91,
8.18, 8.34, 8.57, 8.67, 8.78, 9.07, 9.06, 9.48, 9.58, 9.63, 9.9, 10.23, 10.32, 10.44,
10.82, 10.95, 11.2, 11.39, 11.63, 11.98, 12.15, 12.49, 12.62, 12.93, 13.22, 13.36,
13.57, 13.85, 14.26, 14.42, 14.68, 15.13, 15.48, 15.6, 15.9, 16.22])*0.01

plt.figure(1)
plt.xlabel("t in s")
plt.ylabel("x in m")
plt.plot(t,x,'.c')

v1 = (x[1:]-x[:-1])/(t[1:]-t[:-1])
t1 = (t[1:]+t[:-1])/2.

plt.figure(2)
plt.xlabel("t in s")
plt.ylabel("v in m/s")
plt.plot(t1,v1,'.b')

v2 = (x[5:]-x[:-5])/(t[5:]-t[:-5])
t2 = (t[5:]+t[:-5])/2.

plt.plot(t2,v2,'.r')

fitv1,errorv1=curve_fit(linfit,t1,v1,p0=guess1)
print("a0, a1: ", fitv1)
fitv2,errorv2=curve_fit(linfit,t2,v2,p0=guess1)
print("a0, a1: ", fitv2)

plt.plot(t,linfit(t,*fitv1),'--b')
plt.plot(t,linfit(t,*fitv2),'--r')

# part b

a1 = (v1[1:]-v1[:-1])/(t1[1:]-t1[:-1])
t3 = (t1[1:]+t1[:-1])/2.

plt.figure(3)
plt.xlabel("t in s")
plt.ylabel("a in m/s/s")
plt.plot(t3,a1,'.c')

a2 = (v2[5:]-v2[:-5])/(t2[5:]-t2[:-5])
t4 = (t2[5:]+t2[:-5])/2.

plt.plot(t4,a2,'.m')

fita1,errora1=curve_fit(linfit,t3,a1,p0=guess1)
print("a0, a1: ", fita1)
fita2,errora2=curve_fit(linfit,t4,a2,p0=guess1)
print("a0, a1: ", fita2)

plt.plot(t,linfit(t,*fita1),'--c')
plt.plot(t,linfit(t,*fita2),'--m')

# part c

fitx,errorx=curve_fit(quadfit,t,x,p0=guess2)
print("a0, a1, a2: ", fitx)

plt.figure(1)
plt.plot(t,quadfit(t,*fitx),'--k')

plt.figure(2)
plt.plot(t,linfit(t,fitx[1],2*fitx[2]),'--k')

plt.figure(3)
plt.plot(t,linfit(t,2*fitx[2],0),'--k')


plt.show()
