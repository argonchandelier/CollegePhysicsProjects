# Logan Richan
# ph295

from numpy.fft import rfft, irfft
from numpy import loadtxt, copy
from matplotlib import pyplot as plt


data=loadtxt("dow.txt",float)

#print(data)

c = rfft(data)
size=len(c)
#k = copy(c)

for i in range(20,size):
    c[i]=0
#for i in range(35,size):
#    k[i]=0
    

#print(c)

#plt.plot(c)
#plt.xlim(0,20)

z = irfft(c)
#z2 = irfft(k)

plt.plot(data)
plt.plot(z)
#plt.plot(z2)
plt.show()
