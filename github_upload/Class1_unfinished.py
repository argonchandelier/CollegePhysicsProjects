from numpy import e

y = (R * ((1/(m**2)) - (1/(n**2))))**(-1)
R = 1.097*(e**-2)
for m in [1,2,3]:
    print("series of m = ", m)
for k in [1,2,3,4,5]:
    n = m + k
print ("wavelength = ", y)