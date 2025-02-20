# Logan Richan
# ph295

from numpy import loadtxt, zeros, exp, pi
from matplotlib import pylab as plt

data=loadtxt("outputA.txt")
print(data)

def dft(y): # Calculates the Discrete Fourier Transform of the data
    N = len(y)
    c = zeros(N//2+1,complex)
    for k in range(N//2+1):
        for n in range(N):
            c[k] += y[n]*exp(-2j*pi*k*n/N)
    return c
    
c=dft(data)  

plt.plot(abs(c))
plt.show()

