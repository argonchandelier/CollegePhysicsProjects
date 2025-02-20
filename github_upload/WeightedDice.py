# Logan Richan
# ph336

import numpy as np
from matplotlib import pyplot as plt


nDice=2
tosses=1000000

pSides=[4,3,2,1,1,1]

nSides=len(pSides)

spots=[]
outcomes=[]
Plist=[]

for i in range(0,nSides):
    for j in range(pSides[i]):
        Plist.append(i+1) # makes a list of 4 1s, 3 2s, 2 3s, and 1 of 4, 5, and 6

N=len(Plist)

for k in range(0,(nSides-1)*nDice+1):
    spots.append(k+nDice)
    outcomes.append(0)

for m in range(tosses):
    # add 1 for each time the outcome is observed
    total=0
    for p in range(nDice):
        rand = np.random.randint(0,N)
        total += Plist[rand]
    outcomes[total-nDice] += (1./float(tosses))

mu=(1+nSides)*nDice/2.0
sigma=np.sqrt(mu)

gauss=[1/(sigma*np.sqrt(2*np.pi))*np.exp(-(i-mu)**2/(2*sigma)**2) for i in spots]

plt.plot(spots,gauss,'-r')
plt.bar(spots,outcomes)
plt.show()

