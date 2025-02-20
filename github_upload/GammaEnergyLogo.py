# v1 built with shift=1. & freqMultiplier=2


from numpy import sin, zeros, arange, pi
from matplotlib import pyplot as plt

a = 0.
b = 5.
N = 1000.
h = (b-a) / N

x = arange(a, b+h, h)
y = zeros(int(N) + 1)

shift = 1./1.
freqMultiplier = 2

i = 0
for xValue in x:
    y[i] = sin((xValue + shift) * 2*pi * freqMultiplier)
    i+=1

plt.plot(x, y, color = '#7d21d8', linewidth = 6.1)
plt.show()