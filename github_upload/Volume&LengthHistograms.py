# Logan Richan
# Ph150 assignment

from numpy import array,size,sqrt,std,mean
from matplotlib import pyplot

x=array([5.09,4.22,5.11,4.76,5.06,4.64,4.28,4.52,4.99,4.97])

def calculator(a):
    N=size(a)
    themean=sum(a)/N
    sd=sqrt((1./N)*sumsquares(a,N,themean))
    #sdm=sd/sqrt(N)
    #print(N)
    
    print("mean:", themean)
    print("sd:", sd)
    #print(sdm)
    

def sumsquares(a,N,themean):
    sum=0
    for i in range(0,N):
        sum+=((a[i]-themean)**2)
    #print(sum)#
    return sum

#calculator(x)

#--------------------------------------------------------------

from numpy import loadtxt
data=array(loadtxt('widthlargest.txt'))
#calculator(data)

#pyplot.hist(data, bins=100)
pyplot.show()

#print(mean(data))
#print(std(data))

length=loadtxt('lengthlargest.txt')
width=loadtxt('widthlargest.txt')
height=loadtxt('heightlargest.txt')

Volume=length*width*height
pyplot.figure(1)
pyplot.hist(Volume, bins=100)
pyplot.show()
pyplot.figure(2)
pyplot.hist(length, bins=100)
pyplot.show()
