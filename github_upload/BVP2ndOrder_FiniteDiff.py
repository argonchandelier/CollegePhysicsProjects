# Logan Richan
# ph385

class BoundaryValueProblem:
    # Initialize N and grid space
    def __init__(self, a, b, N):
        from numpy import linspace
        self.N = N
        self.x,self.dx = linspace(a,b,N,retstep=True)
    
    # Create the matrices
    def loadMatrices(self):
        from numpy import zeros, sin, exp
        self.A = zeros([self.N,self.N]) # Initialize A in Ay=b
        # Find first 2 rows of A
        self.A[0,0] = 1
        self.A[-1,-1] = 1
        
        # Find the rest of A
        for i in range(1, self.N - 1):
            self.A[i,i] = -2/self.dx**2 + exp(self.x[i])
            self.A[i,i+1] = 1/self.dx**2 + sin(self.x[i])/(2.*self.dx)
            self.A[i,i-1] = 1/self.dx**2 - sin(self.x[i])/(2.*self.dx)
        
        # use the right hand side of the equation for b, with initial conditions as well
        self.b = self.x**2
        self.b[0] = 0
        self.b[-1] = 3
    
    # Do a linear algebra solver for y in Ay = b
    def solveProblems(self):
        from numpy.linalg import solve
        self.solution = solve(self.A, self.b)
    
    # Plot the solution obtained by the approximation
    def plotSolution(self):
        from matplotlib import pyplot
        pyplot.plot(self.x,self.solution,'r')
        pyplot.show()


# Initialize
a=0
b=5
N=200
myBVP = BoundaryValueProblem(a,b,N)

# Get and solve Matrices
myBVP.loadMatrices()
myBVP.solveProblems()

# Plot solution estimated with the actual solution
myBVP.plotSolution()

# GPT summary:
# This script solves a second-order boundary value problem (BVP) numerically using finite difference methods. It constructs and solves a linear system of equations, approximating the solution to a differential equation with given boundary conditions.
#
# The problem being solved follows the form:
# y′′+f(x)y′+g(x)y=h(x)
# y′′+f(x)y′+g(x)y=h(x)
