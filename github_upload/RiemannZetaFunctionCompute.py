##############
# PH385 Test 1
# Problem # 1
# Logan Richan
################


from numpy import linspace
from matplotlib import pyplot as plt


class RiemannZetaClass():
    # Riemann Zeta function
    def RiemannZeta(self, p):
        S = 0 # Start sum at 0
        Tprev = 100 # Initialize term of a sum
        err = 10**(-9) # closeness of terms before accepted convergence
        maxIterations = 100000 # to keep from an infinite loop
        for n in range(1, maxIterations+1): # loop until going too long
            T = n**(-p) # Utilizing given equation
            S += T # Sum term by term
            if abs(T-Tprev) < err: # break the loop at accepted convergence
                break
            Tprev = T
        
        return S # Return the function
    
    # Find the RiemannZeta function output with given p
    def FindPs(self):
        Z1 = self.RiemannZeta(0.5) # p = 0.5
        Z2 = self.RiemannZeta(1.5) # p = 1.5
        
        # Print Riemann Zeta values
        print("Function at p=0.5 for 100 thousand iterations instead of infinity:", Z1)
        print("Function at p=1.5:", Z2)
        print("p=1.5 converges, but p=0.5 diverges, as it always goes to the maximum number of iterations")
        
    def Plot(self):
        # Make a grid of points from a to b with n points
        a = 1
        b = 10
        n = 1000
        x = linspace(a,b,n)
        
        y = [] # initialize y values
        for i in x:
            y.append(self.RiemannZeta(i)) # Use the Riemann Zeta function for each p
        
        # Plot p values with the Riemann Zeta output for the p
        plt.plot(x,y)
        plt.show()

RZ = RiemannZetaClass() # Initialize Riemann Zeta class
RZ.FindPs() # part a
RZ.Plot() # part b