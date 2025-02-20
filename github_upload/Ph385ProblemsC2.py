# Logan Richan
# ph385

from numpy import arange, sin, log, sum, loadtxt, size, array, exp, cos
from matplotlib import pyplot

### P2.1 ###
def P2_1():
    x = arange(3,2001,3) # Take all multiples up 3 up to 2000...
    y = 3*x**2*sin(x) + log(x) # ...put each of them through this function...
    z = sum(y) # ...and sum them all up to get -736905.545292
    print(z) # show answer
    print("End of problem 2.1.\n")

### P2.2 ###
def P2_2():
    #retrieve data
    data = loadtxt('massdata.txt')
    
    #initialize CM coordinates and the total mass M
    xCM=0
    yCM=0
    zCM=0
    M=0
    
    # Take the sum of each coordinate multiplied by its mass...
    for i in data: 
        xCM += i[0]*i[3]
        yCM += i[1]*i[3]
        zCM += i[2]*i[3]
        M+=i[3] # (Find the total mass of the system)
    #... and divide by the total mass to get the CM coordinates
    xCM = xCM/M
    yCM = yCM/M
    zCM = zCM/M
    print(xCM,yCM,zCM) # Show CM coordinates
    
    #Alternate method...
    #Get all x, y, z, and m values...
    x=data[:,0]
    y=data[:,1]
    z=data[:,2]
    m=data[:,3]
    
    # ...and use the CM coordinate equation on all arrays simultaneously
    Pt = array([sum(m*x)/sum(m), sum(m*y)/sum(m), sum(m*z)/sum(m)], float)
    print(Pt) # Show CM coordinates (again; should be the same as above)
    print("End of problem 2.2.\n")

### P2.3 ###
def P2_3():
    # initialize variables
    n = 0 # Starting at n=0...
    ep=10**(-8) #Stop computing when terms fall below this numbere
    s = 0 # sum of terms
    q = 1 # term
    x = 1.01 # ... with an x between -1 and 1 (non-inclusive) ...
    while q > ep:
        n = n + 1 #...keep raising n...
        q = n * x**n #...perform this operation for each term...
        s += q #...and take the sum of those terms...
        if n == 10000: # If x is not within the specified range, the loop will go forever, so it will need to be broken
            break
    conv = x / (1-x)**2 #...the sum should equal this value...
    print(s, conv) #...and this will tell if they are about equal (or that the sum does not converge if x is not in the specified range)
    print("End of problem 2.3.\n")

### P2.4 ###

# Show that the sum of n integers from 1 through n...
def summ(n):
    S = 0
    for i in range(0,n+1):
        S += i
    return S

# ...is equal to this equation...
def form(n):
    return n*(n+1)/2.

#...by comparing a few values and showing that they are equal
def P2_4():
    for k in [24,429,34,904,2300]:
        print(summ(k), form(k)) # (Should be equal)
    print("End of problem 2.4.\n")

### P2.5 ###
def P2_5():
    x = arange(0,10,0.02) # Plot from 0 to 10...
    y = exp(-0.25*x)*cos(x) # ...this function
    # Plotting commands:
    pyplot.figure()
    pyplot.plot(x,y)
    pyplot.show()
    print("---See plot---")
    print("End of problem 2.5.\n")
    

P2_1()
P2_2()
P2_3()
P2_4()
P2_5()