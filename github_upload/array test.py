from numpy import zeros
from pylab import plot,show

z=5
x=zeros([4,4],float)+z
y=zeros([4,4],float)+4
x[0]+=7
y[0]=4
y[0][1]=15
print(x[0][0],y[0][0])
print(x[0][1],y[0][1])
print(y)
print(z)
plot(x[0],y[0])
show()