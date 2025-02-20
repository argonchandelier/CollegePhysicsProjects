from matplotlib import pyplot as plt
import numpy as np

wavelengths = np.array([1800, 2000, 2200, 2400, 2600, 2800, 3000, 3200, 3400, 3600, 3700, 3800, 3900,\
                        4000, 4100, 4200, 4300, 4400, 4500, 4600, 4800, 5000, 5500, 6000, 6500, 7000,\
                        7500, 8000, 9000,10000,11000,12000,14000,16000,18000,20000,25000,30000,35000], float)

fluxes =      np.array([   0,  1.2,  4.5,  6.4,   13,   25,   59,   85,  114,  115,  127,  121,  115,\
                         160,  187,  189,  183,  201,  213,  215,  213,  204,  198,  187,  167,  149,\
                         129,  114,   90,   74,   61,   50,   33,   22,   15,   10,  5.0,    1,    0])

plt.plot(wavelengths, fluxes)
plt.plot(wavelengths, fluxes,'.')
plt.xlabel("Wavelength in Angstroms")
plt.ylabel("Flux in ergs/cm^2/sec/Angstrom")
plt.show()

maxWavelength = wavelengths[fluxes.tolist().index(max(fluxes))]
print(maxWavelength, "A")
T1 = 2.898e7 / maxWavelength
print(T1, "K")

F_T = 0
for i in range(len(fluxes) - 1):
    F_T += (wavelengths[i+1] - wavelengths[i]) * (fluxes[i+1] + fluxes[i])
F_T *= 0.5
print(F_T, "ergs/cm^2/sec")

r = 1.50e13 # cm
R = 6.96e10 # cm
F = F_T * (r**2 / R**2)
print(F, "ergs/cm^2/sec")

sig = 5.67e-5 # ergs/cm^2/sec/K^4
T2 = (F / sig)**(0.25)
print(T2, "K")
