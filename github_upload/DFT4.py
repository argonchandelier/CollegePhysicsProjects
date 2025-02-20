# Logan Richan
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
f = np.sin(5 * 2 * np.pi * t) + 3*np.sin(170 * 2 * np.pi * t) # Function to perform transform on

gamma = DFT(f)
print(nSamples)
k = np.linspace(0,fS//2,nSamples//2 + 1) # new k
#k = np.linspace(0,fS,nSamples + 1) #old k
plt.plot(k,np.abs(gamma)) # plot frequencies
plt.show()