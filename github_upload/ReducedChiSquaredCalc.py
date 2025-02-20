### PH336 Test 3
### Problem 2
###
### Logan Richan

import numpy as np

th = np.array([0, 10, 20, 30, 40, 50, 60],float)*np.pi/180. + 1e-10
x = np.array([3.28, 4.09, 4.83, 5.35, 5.50, 5.21, 4.44])

dth=1.*np.pi/180.
dx=0.02
v0=6.82
dv0=0.02
y0=1.173
dy0=0.002
g=9.8004
dg=0.0002

def exppx(th,v0,g,y0):
    return v0**2*np.sin(th)*np.cos(th)/float(g) * (1+np.sqrt(1 + 4.*y0*g/float(2*v0**2*(np.sin(th))**2)))

chiSq=0.
for i in range(len(x)):
    chiSq += (x[i] - exppx(th[i],v0,g,y0))**2 / float(dx**2)

redChiSq=chiSq/6.
print("reduced chi squared value: " + str(redChiSq))