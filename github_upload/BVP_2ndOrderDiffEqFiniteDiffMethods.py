# Logan Richan
# ph385

from matplotlib import pyplot

class BoundaryValueProblem:
    # Initialize N and grid space
    def __init__(self, a, b, N):
        from numpy import linspace
        self.N = N
        self.x,self.dx = linspace(a,b,N,retstep=True)
    
    # Create the matrices
    def loadMatrices(self):
        from numpy import zeros, sin
        self.A = zeros([self.N,self.N]) # Initialize A in Ay=b
        # Find first 2 rows of A
        self.A[0,0] = 1
        self.A[-1,-1] = 1
        
        # Find the rest of A
        for i in range(1, self.N - 1):
            self.A[i,i] = -2/self.dx**2 + 9
            self.A[i,i+1] = 1/self.dx**2
            self.A[i,i-1] = 1/self.dx**2
        
        # use the right hand side of the equation for b, with initial conditions as well
        self.b = sin(self.x)
        self.b[0] = 0
        self.b[-1] = 1
    
    # Do a linear algebra solver for y in Ay = b
    def solveProblems(self):
        from numpy.linalg import solve
        self.solution = solve(self.A, self.b)
    
    # Plot the solution obtained by the approximation
    def plotSolution(self):
        pyplot.plot(self.x,self.solution,'r.')
        #pyplot.show()
    
    # Plot the exact solution
    def plotExactSolution(self):
        from numpy import sin, cos

        # Exact solution:
        self.yExact = -0.2236 * (cos(6-self.x) + cos(2+3*self.x) + 16*sin(3*self.x) - cos(2-3*self.x) - cos(6+self.x))
        pyplot.plot(self.x,self.yExact)
        #pyplot.show()


# Initialize
a=0
b=2
N=30
myBVP = BoundaryValueProblem(a,b,N)

# Get and solve Matrices
myBVP.loadMatrices()
myBVP.solveProblems()

# Plot solution estimated with the actual solution
myBVP.plotSolution()
myBVP.plotExactSolution()

pyplot.show()
