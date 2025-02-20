# Logan Richan
# ph295

from numpy import zeros, arange
from numpy import loadtxt, copy
from numpy.fft import rfft, irfft
from matplotlib import pyplot as plt

data=loadtxt("gravity_wave_data.txt")

N=1024
h=.5/(N-1)
tvalues=zeros(1024,float)
i=0
for t in arange(0,.5+h,h):
    tvalues[i]=t
    i+=1
plt.subplot(221)
plt.plot(tvalues, data)
plt.title("Strain of 0.5 seconds")
plt.xlabel("Time in seconds")
plt.ylabel("Strain")
#plt.show()

k = rfft(data)
f = abs(copy(k))#/.5

plt.subplot(222)
plt.plot(arange(0,1024+1,2),f)
plt.title("Frequency vs. Magnitude")
plt.ylabel("Magnitude")
plt.xlabel("Frequency")
#plt.show()


f2 = copy(f)
for i in range(0,20//2):
    f2[i]=0
for i in range(int(80/2+1),int(1024/2)):
    f2[i]=0


plt.subplot(223)
plt.plot(arange(0,1024+1,2),f2)
plt.xlim(20,80)
plt.title("Filtered Frequencies vs. magnitude")
plt.xlabel("Filtered Frequencies")
plt.ylabel("Magnitude")
#plt.show()

cleanedData = irfft(f2)

plt.subplot(224)
plt.plot(tvalues, cleanedData)
plt.title("Filtered signal vs. time")
plt.xlabel("Time in seconds")
plt.ylabel("Filtered Signal")

plt.show()
