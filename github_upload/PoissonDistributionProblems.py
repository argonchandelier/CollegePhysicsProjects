# Logan Richan
# ph336
# Finds N times '1' appears in Poisson distribution
# Finds how often 5 consecutive 0s occur

import numpy as np
from scipy import stats
from matplotlib import pyplot as plt
from math import factorial

mu=1
nmax=1000
modelTimes=range(10000)

ones = []
fivePlus0Count = []
for i in modelTimes:
    r=np.ndarray.tolist(stats.poisson.rvs(mu, size=1000))
    ones.append(r.count(1))
    
    consecutive0s=0
    streakCount=0
    for k in range(nmax):
        if r[k] == 0:
            consecutive0s+=1
        else:
            consecutive0s=0
        if consecutive0s==5:
            streakCount+=1
    fivePlus0Count.append(streakCount)

streakSpots=range(max(fivePlus0Count))
streakOutcomes=[]
for l in streakSpots:
    streakOutcomes.append(fivePlus0Count.count(l))
    
plt.figure(1)
plt.bar(streakSpots,streakOutcomes)
print("Expected # of at least 5 consecutive 0s: ", np.mean(fivePlus0Count))

spots=[]
outcomes=[]
for j in range(min(ones),max(ones)+1):
    spots.append(j)
    outcomes.append(ones.count(j))

plt.figure(2)
plt.bar(spots,outcomes)
plt.show()

expectedOnes = mu**1 * np.exp(-mu) / factorial(1) * nmax
print(expectedOnes)

actualOnes = np.mean(ones)
print(actualOnes)
