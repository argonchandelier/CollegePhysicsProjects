# Logan Richan
# ph336

import numpy as np
from matplotlib import pyplot as plt


nDice=4
sides=6
tosses=100000

spots=[]
outcomes=[]

for i in range(0,(sides-1)*nDice+1):
    spots.append(i+nDice)
    outcomes.append(0)

for j in range(tosses):
    n=0
    for k in range(nDice):
        n+=np.random.randint(1,sides+1)
    outcomes[n-nDice]+=(1.0/tosses)

mu=(1+sides)*nDice/2.0
sigma=np.sqrt(mu)/1.2
gauss=[1/(sigma*np.sqrt(2*np.pi))*np.exp(-(i-mu)**2/(2*sigma)**2) for i in spots]

plt.plot(spots,gauss,'-r')
plt.bar(spots,outcomes)
plt.show()

if nDice==2:
    parta = outcomes[4] + outcomes[5] + outcomes[6]
    print(parta)
elif nDice==4:
    partb = outcomes[8] + outcomes[9] + outcomes[10] + outcomes[11] + outcomes[12]
    print(partb)