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
        from numpy import zeros
        self.A = zeros([self.N,self.N]) # Initialize A in Ay=b
        # Find first 2 rows of A
        self.A[0,0] = 1
        self.A[-1,-1] = 1/self.dx
        self.A[-1,-2] = -1/self.dx
        
        # Find the rest of A
        for i in range(1, self.N - 1):
            self.A[i,i] = -2/self.dx**2 + 9
            self.A[i,i+1] = 1/self.dx**2
            self.A[i,i-1] = 1/self.dx**2
        
        print(self.A)
        
        # use the right hand side of the equation for b, with initial conditions as well
        self.b = self.x+0
        self.b[0] = 0
        self.b[-1] = 0
    
    # Do a linear algebra solver for y in Ay = b
    def solveProblems(self):
        from numpy.linalg import solve
        self.solution = solve(self.A, self.b)
    
    # Plot the solution obtained by the approximation
    def plotSolution(self):
        pyplot.plot(self.x,self.solution,'r.')

    # Plot the exact solution
    def plotExactSolution(self):
        from numpy import sin, cos

        # Exact solution:
        self.yExact =  self.x/9. - sin(3*self.x)/(27.*cos(6.))
        pyplot.plot(self.x,self.yExact)


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

'''
The equation being solved:
y′′(x)+9y(x)=x

with boundary conditions:
y(0)=0,y′(2)=0
'''
