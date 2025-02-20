# Logan Richan
# ph385

from numpy import pi
from matplotlib import pyplot


class BoundaryValueProblem:
    # Initialize N and grid space
    def __init__(self, a, b, N):
        from numpy import linspace
        
        # Given constants
        self.w = 20.
        self.g = 9.8
        self.L = b
        
        # Grid creation
        self.N = N
        self.dx = (b-a)/float(N)
        self.x,self.dx = linspace(a-self.dx/2.,b+self.dx/2.,N+2,retstep=True)
    
    # Create the matrices
    def loadMatrices(self):
        from numpy import zeros
        h=float(self.dx)
        self.A = zeros([self.N+2,self.N+2]) # Initialize A in Ay=b
        self.B = zeros([self.N+2,self.N+2])
        
        # Find first and last rows of A and B
        self.A[0,0] = -1/h
        self.A[0,1] = 1/h
        self.A[-1,-2] = 0.5
        self.A[-1,-1] = 0.5
        self.B[0,0] = 0.5
        self.B[0,1] = 0.5
      
        # Find the rest of A
        for i in range(1, self.N + 1):
            self.A[i,i] = -2*self.x[i]/h**2
            self.A[i,i+1] =  1/(2*h) + self.x[i]/h**2
            self.A[i,i-1] = -1/(2*h) + self.x[i]/h**2
            self.B[i,i] = 1
        #print(self.B)
    
    # Do a linear algebra solver for y in A*g = lambda*B*g
    def solveProblems(self):
        from scipy.linalg import eig
        self.eValue, self.eVec = eig(self.A, self.B)
        #print(self.eVec)
        #print(self.eValue)
        
        self.omega = (-self.eValue*self.g)**(0.5)/(2*pi)
        self.key = sorted(range(self.N + 2), key = lambda k: self.omega[k])
        
    
    # Plot the solution obtained by the approximation
    def plotSolution(self,mode):
        pyplot.plot(self.eVec[:,self.key[mode]],self.x)
        pyplot.axes().set_aspect('equal')

        
        print(self.omega[self.key[mode]])
    


# Initialize
a=0
b=2
N=50
myBVP = BoundaryValueProblem(a,b,N)

# Get and solve Matrices
myBVP.loadMatrices()
myBVP.solveProblems()

mode = 3
myBVP.plotSolution(mode)

pyplot.show()

