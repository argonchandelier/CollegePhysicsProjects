# Logan Richan
# ph336

from matplotlib import pyplot as plt
from numpy import zeros

X=range(0,13)
data = [5, 2, 3, 4, 3, 4, 4, 6, 10, 4, 3, 8, 4, 12, 8, 6, 6, 8, 4, 6, 
   7, 4, 9, 3, 5, 5, 9, 3, 8, 0, 7, 3, 10, 4, 6, 1, 2, 3, 2, 3, 3, 2, 
   5, 2, 6, 7, 4, 4, 4, 6, 10, 4, 5, 10, 2, 6, 4, 5, 4, 5, 5, 4, 4, 6,
    6, 11, 6, 4, 5, 1, 4, 5, 1, 6, 2, 5, 7, 3, 4, 9, 5, 2, 7, 3, 2, 
   10, 4, 1, 2, 3, 6, 2, 4, 5, 6, 5, 2, 6, 1, 9, 5, 3, 5, 4, 6, 7, 4, 
   7, 10, 1, 3, 2, 5, 7, 3, 5, 5, 5, 4, 2]
N=zeros(len(X))
for n in data:
    N[n]+=1
print(len(data))
plt.plot(X,N)
plt.show()