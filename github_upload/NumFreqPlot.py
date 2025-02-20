# Logan Richan
# ph336

from matplotlib import pyplot as plt
from numpy import zeros

X=range(0,6)
N=zeros(len(X))
for n in [0, 2, 1, 1, 1, 0, 1, 1, 1, 0, 0, 5, 2, 2, 3, 0, 1, 0, 1, 3, 2, 1, 1, 0, 0, 0, 1, 4, 0, 2]:
    N[n]+=1

plt.plot(X,N)
plt.show()