# Logan Richan
# ph150

from matplotlib import pyplot as plt
from numpy import array, arange, pi
import scipy.optimize as opt


#h=array([44.19995677,  8.73991549, 11.49192912,  9.91067308, 37.9143907415, 15.47046519,  41.17216319,  10.68610783,  50.25852089,  16.16540785], float)
#t=array([1.89951566, 0.84466709, 0.96856423, 0.89946347, 1.75927607, 1.123786061, 1.8333011,   0.93398894,  2.02552127,  1.14874938], float)
d=array([2.5,2.2,2.1,1.3,1.3],float) #cm
m=array([65,45,44.75,8.5,8.5],float) #g

#V=(4./3.)*pi*(d/2)**3 = pi/6 * d**3

#pGuess=m/V
# Density p * Volume V = mass m

def fitFunc(t,a):
    return 0.5*a*t**2

# p*V = m
def fitFunc2(d,p):
    return p*pi/6*d**3

params,uncertainties=opt.curve_fit(fitFunc2,d,m)
print("fitting parameter: ", params)
p=params[0]
print(uncertainties)
times=arange(0,2,.05)
#heights=0.5*a*times**2

dValues=arange(1,3,0.05)
mValues=p*pi/6*dValues**3

#print(uncertainties)

plt.plot(d,m,".")
plt.plot(dValues,mValues)
#plt.plot(times, heights)
plt.show()
