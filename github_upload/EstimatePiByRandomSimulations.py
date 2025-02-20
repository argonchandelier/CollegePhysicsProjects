# Calculate I: pi/4; true value: 0.7853981634...
# Calculate using randomness


from numpy import zeros, sqrt
from random import random

Atotal=1
N=1000000
X=10
Is=zeros(X,float)

for j in range(X):
    count=0
    for i in range(N):
        x=random()-0.5
        y=random()-0.5
        r=sqrt((x**2)+(y**2))
        if r<0.5:
            count+=1
    I=count/float(N)*Atotal
    print(I*4)
    Is[j]=I

avgI=sum(Is)/float(X)
sigma=sqrt(sum((avgI-Is)**2)/float(X))

print("pi est:", avgI*4, "+/-", sigma*4)
