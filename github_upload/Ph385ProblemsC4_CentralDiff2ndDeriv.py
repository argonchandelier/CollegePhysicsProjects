# Logan Richan
# ph385

from numpy import sin, cos, cosh, linspace, array, append, exp, log
from matplotlib import pyplot as plt

### P4.1 ###
def P4_1():
    h=10**(-2) # using a small h
    diffSin_fdf=(sin(1+h)-sin(1))/h # Find derivative using forward difference formula
    diffSin_cdf=(sin(1+h)-sin(1-h))/(2*h) # Find derivative using central difference formula
    print(diffSin_fdf)
    print(diffSin_cdf)
    
    # Compare the two methods against each other and the actual value
    print(cos(1), diffSin_fdf/cos(1), diffSin_cdf/cos(1))
    
    # The central difference method is clearly better

### P4.2-3 ###
def P4_2_3():
    ### 4.2 ###
    plt.figure(1) # start figure
    # Create a cell-edge grid from a-b using 100 points
    a=0 
    b=5
    N=100
    x,dx=linspace(a,b,N,retstep=True)
    
    # Using this function...
    y = sin(x) * cosh(x)
    # ...find the first two derivatives by using the central difference method
    yPrime = (y[2:] - y[:-2])/(2*dx)
    yDoublePrime = (yPrime[2:] - yPrime[:-2])/(2*dx)
    
    # Plot y, y', and y''
    plt.plot(x,y)
    plt.plot(x[1:-1],yPrime)
    plt.plot(x[2:-2],yDoublePrime)
    
    ### 4.3 ###
    plt.figure(2) #start a new figure
    
    # Using the extrapolation formula, append points to the first and second derivatives, so they match the full length of the original function
    yPrime=append(array( [yPrime[1]*(2)-(1)*yPrime[0]] ),append(yPrime,array( [yPrime[-1]*(2)-(1)*yPrime[-2]] )))
    yDoublePrime=append(array( [yDoublePrime[1]*(3)-(2)*yDoublePrime[0], yDoublePrime[1]*(2)-(1)*yDoublePrime[0]] ),append(yDoublePrime,array( [yDoublePrime[-1]*(2)-(1)*yDoublePrime[-2], yDoublePrime[-1]*(3)-(2)*yDoublePrime[-2]] )))
    
    # Plot y, y', and y'' again with the appended values
    plt.plot(x,y)
    plt.plot(x,yPrime)
    plt.plot(x,yDoublePrime)
    
    print(yPrime)
    
### P4.4 is in Mathematica ###

### P4.5 ###
def P4_5():
    plt.figure(3) #start a new figure
    # initialize arrays and start h at 1
    h=1.
    ffdErr=[]
    cfdErr=[]
    csdErr=[]
    H=[]
    while h > 10**(-5):
        # Find the derivative value given by the given method
        ffd=(exp(0+h)-exp(0))/h # forward difference derivative
        cfd=(exp(0+h)-exp(0-h))/(2*h) # central difference first derivative
        csd=(exp(0+h)-2*exp(0)+exp(0-h))/(h**2) # central difference second derivative
        
        # Find the error and add to the list
        ffdErr.append(ffd-1)
        cfdErr.append(cfd-1)
        csdErr.append(csd-1)
        H.append(h)
        
        h/=2. # decrease h by a power of 2 each iteration
    #Plot log graphs of h vs. error
    plt.loglog(H,ffdErr,'.')
    plt.loglog(H,cfdErr,'.') # the Error here is about the error of the previous plot squared
    plt.loglog(H,csdErr,'.')
    # Label plots
    plt.xlabel("h")
    plt.ylabel("Error")

#P4_1()
P4_2_3()
#P4_5()
plt.show()
    