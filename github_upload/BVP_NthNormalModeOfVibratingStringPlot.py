# Logan Richan
# ph385

from numpy import pi

class BoundaryValueProblem:
    # Initialize N and grid space
    def __init__(self, a, b, N):
        from numpy import linspace
        
        # Given constants
        self.w = 20.
        self.T = 1.
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
            self.A[i,i] = -2*self.T / float(h**2*(0.1+self.x[i]/float(self.L)))
            self.A[i,i+1] = self.T / float(h**2*(0.1+self.x[i]/float(self.L)))
            self.A[i,i-1] = self.T / float(h**2*(0.1+self.x[i]/float(self.L)))
            self.B[i,i] = 1
        #print(self.B)
    
    # Do a linear algebra solver for y in A*g = lambda*B*g
    def solveProblems(self):
        from scipy.linalg import eig
        self.eValue, self.eVec = eig(self.A, self.B)
        #print(self.eVec)
        #print(self.eValue)
        
        self.omega = (-self.eValue)**(0.5)
        self.key = sorted(range(self.N + 2), key = lambda k: self.omega[k])
        
    
    # Plot the solution obtained by the approximation
    def plotSolution(self,mode):
        from matplotlib import pyplot
        pyplot.plot(self.eVec[:,self.key[mode]],self.x)
        pyplot.axes().set_aspect('equal')
        pyplot.show()
        
        print(self.omega[self.key[mode]])
    


# Initialize
a=0
b=2
N=100
myBVP = BoundaryValueProblem(a,b,N)

# Get and solve Matrices
myBVP.loadMatrices()
myBVP.solveProblems()

normalMode = 7
myBVP.plotSolution(normalMode)
