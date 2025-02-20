### PH336 Test 2
### Problem 2
###
### Logan Richan

from matplotlib import pyplot as plt
import numpy as np
from scipy.optimize import curve_fit

theta=np.array([0, 5, 10, 15, 20, 25, 30, 35, 40, 45, 50, 55, 60, 65, 70, 75, 80, \
85, 90, 95, 100, 105, 110, 115, 120, 125, 130, 135, 140, 145, 150, \
155, 160, 165, 170, 175, 180],float) # Theta in degrees

cosTheta=np.cos(theta*np.pi/180.) # cosine of theta

wvlngth=np.array([0.179, 0.179, 0.181, 0.18, 0.18, 0.182, 0.184, 0.183, 0.186, 0.186, \
0.188, 0.19, 0.192, 0.192, 0.197, 0.198, 0.199, 0.202, 0.202, 0.206, \
0.207, 0.211, 0.211, 0.213, 0.217, 0.218, 0.22, 0.221, 0.222, 0.224, \
0.225, 0.226, 0.228, 0.226, 0.228, 0.229, 0.229])*1e-10 # Wavelengths in m

def linfit(x,a0,a1): # linear fit model
    return (a0 + a1*x)
guess=[1,-1]

fit,error=curve_fit(linfit,cosTheta,wvlngth,p0=guess) # get parameters of fit model

# Show parameters with their errors
print("a0, a1: ", fit)
print("With errors:", np.sqrt(np.diag(error)))

# Plot the fit with the points of data
plt.plot(theta,linfit(cosTheta,*fit),'--k')
plt.plot(theta,wvlngth,'.b')
plt.title('Compton Scattering')
plt.xlabel('scattering angle (degrees)')
plt.ylabel('scattered wavelength (m)')
plt.show()

# get a1, mass of electron, and c with uncertainties
a1,da1 = fit[1], np.sqrt(error[1,1]) # a1 = h/(me*c)
me,dme = 9.11e-31, 0.01e-31 # in kg
c,dc = 3.00e8, 0.01e8 # in m/s

# Get h with uncertainty
h = -a1*me*c # in J*s
dh = np.sqrt((-me*c*da1)**2 + (-me*dc*a1)**2 + (-dme*c*a1)**2)

# Show h
print("h = " + str(h) + " +/- " + str(dh) + " J*s")
print("h = 6.69x10^-34 +/- 0.06x10^-34 J*s")
