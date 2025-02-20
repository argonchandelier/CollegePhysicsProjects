# Logan Richan
# ph385

from matplotlib import pyplot as plt

class BoundaryValueProblem:
    # Initialize N and grid space
    def __init__(self, a, b, N, omega=400):
        from numpy import linspace
        self.N = N
        # Get the cell edge grid to plot g(x)
        self.x,self.dx = linspace(a,b,N,retstep=True)
        
        # given constants
        self.mu = 0.003
        self.T = 127.
        self.L = b
        self.omega = omega
    
    # Create the matrices
    def loadMatrices(self, omega=-1):
        from numpy import zeros
        # get T and h
        h=float(self.dx)
        T=self.T
        
        # get omega default or new omega
        if omega == -1:
            omega = self.omega

        self.A = zeros([self.N,self.N]) # Initialize A in Ay=b
        # Find first 2 rows of A
        self.A[0,0] = 1
        self.A[-1,-1] = 1
        self.f = zeros([self.N])
        
        # Find the rest of A
        for i in range(1, self.N - 1):
            # Get diagonal A values
            self.A[i,i+1] = T/h**2
            self.A[i,i]   = self.mu*omega**2 - 2*T/h**2
            self.A[i,i-1] = T/h**2
            
            # Get all non-zero f values
            if self.x[i] >= 0.8 and self.x[i] <= 1:
                self.f[i] = -0.73
        
        #boundary conditions
        self.f[0] = 0
        self.f[-1] = 0
    
    def omegaShift(self, omegaA = 400, omegaB = 1200):
        from numpy import linspace
        N=100
        self.omegaValues = linspace(omegaA,omegaB,N) # Get range of omega values
        self.maxAValues = [] # Initialize max amplitude values
        
        # Find the maximum amplitude for each omega value
        for i in self.omegaValues:
            self.loadMatrices(i)
            self.maxAValues.append(self.solveProblems())
            self.plotSolution()
        plt.figure(2)
        plt.plot(self.omegaValues, self.maxAValues)
        #plt.show()
        
    
    # Do a linear algebra solver for y in Ay = b
    def solveProblems(self):
        from numpy.linalg import solve
        self.solution = solve(self.A, self.f)
        
        return max(abs(self.solution))
    
    # Plot the solution obtained by the approximation
    def plotSolution(self, figure=1):
        plt.figure(figure)
        #plt.clf()
        plt.plot(self.x,self.solution,'r')
        plt.pause(.01)
        #plt.show()


# Initialize grid
a=0
b=1.2 # L value
N=100
myBVP = BoundaryValueProblem(a,b,N)

# Get and solve Matrices
myBVP.loadMatrices()
myBVP.solveProblems()

# Plot solution estimated with the actual solution
myBVP.plotSolution()

# Find maximum amplitude values for varying omega
myBVP.omegaShift()

# As omega varies, g(x) gets bigger or smaller, and it spikes at certain omega values. As omega gets bigger,
# another mode begins to appear


# P11.2 part f:
myBVP2 = BoundaryValueProblem(a,b,N,omega=2690.4455791038208)
myBVP2.loadMatrices()
myBVP2.solveProblems()
myBVP2.plotSolution(3)

plt.show()

'''
μω2g(x)=Tg′′(x)+f(x)
'''
