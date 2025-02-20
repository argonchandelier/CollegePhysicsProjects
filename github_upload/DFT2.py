# Logan Richan
# ph295

from numpy import loadtxt
from matplotlib import pyplot as plt
from datetime import datetime

start=datetime.now()
data=loadtxt("pitch2.txt",float)

print(data)

plt.figure(1)
plt.subplot(121)
plt.plot(data)
plt.ylabel("Amplitude")
plt.xlabel("Time")

plt.subplot(122)
############
from numpy import zeros,loadtxt
from cmath import exp,pi
def dft(y):
    N = len(y)
    c = zeros(N//2+1,complex)
    for k in range(N//2+1):
        for n in range(N):
            c[k] += y[n]*exp(-2j*pi*k*n/N)
    return c

c = dft(data)
plt.plot(abs(c))
plt.xlim(0,500)
plt.xlabel("Frequencies")
plt.show()

for x in range (0,500):
    if abs(c[x]) > 28:
        print (x)

#####################

print(datetime.now()-start)