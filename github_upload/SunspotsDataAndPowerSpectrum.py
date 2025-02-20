# Logan Richan
# ph295

from numpy import loadtxt, zeros
from matplotlib import pyplot as plt
from cmath import exp, pi

data=loadtxt("sunspots.txt",float)
N = len(data)

def dft(y): # Calculates the Discrete Fourier Transform of the data
    c = zeros(N//2+1,complex)
    for k in range(N//2+1):
        for n in range(N):
            c[k] += y[n,1]*exp(-2j*pi*k*n/N)
    return c

def plot(y): # Plots the original data
    values1 = zeros(N,float)
    values2 = zeros(N,float)
    for i in range(0,N):
        values1[i] = y[i,0]
        values2[i] = y[i,1]
    plt.subplot(121)
    plt.plot(values1,values2)
    plt.xlabel("Time (in years)")
    plt.ylabel("Sunspots")
    plt.title("Sunspots Data")
    #plt.show()

for i in range(0,N): # Converts the time values into the corresponding year
    data[i,0] /= 12
    data[i,0] += 1749

plot(data) #T =~131 months by inspection

# Computes and plots the Fourier transform squared to get the power spectrum
c = dft(data)
c2 = c**2
c2[0] = 0
plt.subplot(122)
plt.plot(abs(c2))
plt.xlabel("k values")
plt.ylabel("|c_k|^2")
plt.title("Power spectrum of the sunspot signal")
plt.show()

# Computes the maximum k value
N2 = len(c2)
kMax=0
for k in range(0,N2):
    if abs(c2[k])>abs(c2[kMax]):
        kMax=k
print(kMax)

# Computes the period
kMax=float(kMax)
totalTime=float(N-1) #in months
print(totalTime/kMax)

#=(data[N-1,0]-data[0,0])*12 # in months