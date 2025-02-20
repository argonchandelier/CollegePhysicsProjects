# Logan Richan
# ph385

from numpy import sinh, pi, exp, cos, sin

def P2_6_SumFunc(x): # Performs the desired sum
    S=0 # start at 0
    for n in range(1,1001): # for n from 1-1000
        S+=n*x**n
    return S

def P2_6():
    for n in [-2,-0.99,-0.3,-0.1,0,0.01,0.2,0.5,0.8,0.99,1.2]: # Test a bunch of values
        S=P2_6_SumFunc(n) # Perform the desired sum
        
        if n < 1 and n > -1: # Convergence conditions
            F=n/(1-n)**2 # Function for convergence
            print("Convergence: ",S, " ~= ", F) # The sum should be about equal to the formula's output
        else:
            print("Divergence: ",S) # If the convergence conditions are not met, S should be fairly large
    
    print("End of problem H2.6\n")

def P2_7():
    P = 1. # Initialize a large product
    F = sinh(pi)/pi # Formula that the product should be equal to
    err=10**(-6) # "close enough" difference value
    
    for n in range(1,4000000): # Go for a while, but stop after too many times
        P *= 1 + n**(-2)
        if abs(P-F) < err: # If the Product and Function are close enough, we are done
            break
    print(P, " ~= ", F) # Show that they are approximate (with the loop broken when they are close enough)
    print("End of problem H2.7\n")


def P2_8_Funcs(x,n): # Desired functions to test convergence
    if n == 0:
        return exp(-x) # Should converge
    if n == 1:
        return cos(x) # Should converge
    if n == 2:
        return sin(2*x) # Should converge
    else:
        return sin(3*x) # Should NOT converge
    
def P2_8_main(n):
    
    err = 10**(-8) # Convergence level
    x = 0 # initialize x
    xnew = 0.4 # starting x (as x begins at xnew in the loop)
    i = 0    # initialize i
    while abs(xnew-x) > err: # stop iterating when they converge at the given level 
        x = xnew
        xnew = P2_8_Funcs(x,n) # The next step is the desired function with the value of the last step
        if i > 1000000: # The loop will never stop for diverging sums, so eventually the loop should be broken
            print("Does not converge")
            break
        if abs(xnew-x) > 10**2: # The sum is also clearly diverging if the terms keep getting farther apart
            print("Does not converge (", i, " iterations done)")
            break
        i+=1
    if abs(xnew-x) <= err: # Showing convergence after a certain amount of iterations
        print("Converged after ", i, " iterations")

def P2_8():
    # Go through each function to see if it converges
    for i in range(4): 
        P2_8_main(i)
    print("End of problem H2.8\n")



P2_6()
P2_7()
P2_8()