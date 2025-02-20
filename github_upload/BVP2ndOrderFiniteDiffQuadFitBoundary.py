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
        self.A[-1,-1] = 3
        self.A[-1,-2] = -4 #-1
        self.A[-1,-3] = 1#
        
        # Find the rest of A
        for i in range(1, self.N - 1):
            self.A[i,i] = -2/self.dx**2 + 9
            self.A[i,i+1] = 1/self.dx**2
            self.A[i,i-1] = 1/self.dx**2
        
        # use the right hand side of the equation for b, with initial conditions as well
        self.b = self.x+0
        self.b[0] = 0
        self.b[-1] = 0
    
    # Do a linear algebra solver for y in Ay = b
    def solveProblems(self):
        from numpy.linalg import solve
        self.solution = solve(self.A, self.b)
    
    #Fit parabola to end
    def parabolaFit(self):
        from matplotlib import pyplot
        from numpy import arange
        h=self.dx
        x1,y1,y2,y3=self.x[-3],self.solution[-3],self.solution[-2],self.solution[-1]
        
        #parabola fit parameters
        a=(2*h**2*y1 + h*x1*(3*y1-4*y2+y3) + x1**2*(y1-2*y2+y3)) / (2.*h**2)
        b=-(h*(3*y1-4*y2+y3) + 2*x1*(y1-2*y2+y3)) / (2.*h**2)
        c=(y1-2*y2+y3) / (2.*h**2)
        print(a,b,c)
        xs=arange(x1,self.x[-1]+h/10.,h/10.) # points between 3 endpoints
        endPoints = a + b*xs + c*xs**2 # parabola equation
        pyplot.plot(xs,endPoints) # plot parabola on end points
        #pyplot.show()
    
    # Plot the solution obtained by the approximation
    def plotSolution(self):
        from matplotlib import pyplot
        pyplot.plot(self.x,self.solution,'r.')
        #pyplot.show()
    
    # Plot the exact solution
    def plotExactSolution(self):
        from numpy import sin, cos
        from matplotlib import pyplot
        
        # Exact solution:
        self.yExact =  self.x/9. - sin(3*self.x)/(27.*cos(6.))
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
myBVP.parabolaFit()

pyplot.show()
