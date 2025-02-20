# Logan Richan
# ph336

from matplotlib import pyplot as plt
from numpy import arange, zeros


N=100
x=arange(0,12,1)
y=zeros(12,int)

D=[5 ,5 ,1 ,7 ,1,5,3,4,7,9,7,5,6,6,6,8,2,5,7,8,
   6 ,4 ,6 ,5 ,3,4,2,5,7,5,6,4,3,5,3,6,3,3,3,4,
   7 ,10,10,2 ,8,7,5,4,3,5,3,4,1,2,4,3,5,6,8,9,
   3 ,5 ,6 ,5 ,8,5,9,6,3,4,6,5,3,8,5,4,4,6,3,6,
   11,3 ,3 ,10,5,4,5,6,8,3,4,4,5,5,5,3,4,6,4,3]

for i in range(N):
    y[D[i]] += 1

plt.plot(x,y)
plt.show()