# Logan Richan
# DFT Algorithm
# ph385

import numpy as np
from matplotlib import pyplot as plt

# Find discrete fourier transform coefficients
def DFT(samples):
    from numpy import exp, pi
    # Initial number of points and coefficients
    N = len(samples)
    gamma = []
    
    # Find coefficients
    for k in range(N//2 + 1): #N//2
        gammaK=0
        for n, yn in enumerate(samples):
            gammaK += yn * exp(-2j * pi * k * n/N) # Coefficient formula
        gamma.append(gammaK/N)
    return gamma
    
fS = 300. # Sampling frequency in Hz
dt = 1/fS # Time between samples
samplingTime = 1 # in s
nSamples = int(samplingTime/dt)

t = np.linspace(0,samplingTime,nSamples) # time values
f = np.cos(5 * 2 * np.pi * t) + 3*np.sin(170 * 2 * np.pi * t) # Function to perform transform on

gamma = DFT(f)
print(gamma)
k = np.linspace(0,fS//2,nSamples//2 + 1) # new k
plt.plot(k,np.abs(gamma)) # plot frequencies
plt.show()

# The real part of the coefficient * 2 is equal to alpha_k, while the imaginary * 2 corresponds to the 
# beta_k, and for k=0 the coefficient is just alpha, which is the first coefficient