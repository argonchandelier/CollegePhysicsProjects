### PH336 Test 3
### Problem 3
###
### Logan Richan

from matplotlib import pyplot as plt
import numpy as np
#from math import factorial
from scipy.optimize import curve_fit

nheads = np.array([0, 1, 2, 3, 4], dtype=int)
noutcomes = np.array([81, 173, 138, 49, 10], int)

totaloutcomes = sum(noutcomes)
probs = noutcomes/float(totaloutcomes)

flips=np.array([4,4,4,4,4], int)

# Take a factorial of an array
def fact(x):
    xfact = []
    for i in range(len(x)):
        if x[i] == 0:
            xfact.append(1)
        else:
            p=1
            for j in range(1,int(x[i]+1)):
                p *= j
            xfact.append(p)
    return np.array(xfact)

def f(n,Ph):
    return fact(flips)/(fact(n)*fact(flips-n)).astype(float) * Ph**n * (1-Ph)**(flips-n)
guess=[0.2]

fit,error=curve_fit(f,nheads,probs,p0=guess) # get parameters of fit model

# Show parameters with their errors
print("Probability of heads: ", fit[0])
print("With error:", np.sqrt(error)[0][0])

# Plot the fit with the points of data
plt.plot(nheads,f(nheads,*fit),'--k')
plt.plot(nheads,probs,'.b')
plt.title('Coin Tosses')
plt.xlabel('Number of heads')
plt.ylabel('Probability')
plt.show()

print("The probability of getting a head on a single coin is about 34.8% +/- 0.2%")