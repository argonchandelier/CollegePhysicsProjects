# Logan Richan
# ph385

from numpy import pi, exp

class BoundaryValueProblem:
    # Initialize N and grid space
    def __init__(self, a, b, N):
        from numpy import linspace
        # define k and m
        self.k=1000.
        self.m=3.
        
        # Get point of masses
        Da=0
        self.Db=10*N
        dD=(self.Db-Da)/float(N)
        self.D = linspace(0.+dD,self.Db-dD,N)
        
        #get cell edge grid
        self.N = N
        self.dx = (b-a)/float(N)
        print(self.dx,'check')
        self.x,self.dx = linspace(a-self.dx/2.,b+self.dx/2.,N+2,retstep=True)
    
    # Create the matrices
    def loadMatrices(self):
        from numpy import zeros, sin
        h=float(self.dx)
        self.A = zeros([self.N,self.N]) # Initialize A in Ax=lambda*B*x
        self.B = zeros([self.N,self.N]) # B is the Identity matrix
        # Find first 2 rows of A and initial B
        self.A[0,0] = 2
        self.A[0,1] = -1
        self.A[-1,-2] = -1
        self.A[-1,-1] = 2
        self.B[0,0] = 1
        self.B[-1,-1] = 1
        
        # Find the rest of A and B
        for i in range(1, self.N -1):
            self.A[i,i] = 2
            self.A[i,i+1] = -1
            self.A[i,i-1] = -1
            self.B[i,i] = 1
        print(self.B)
    
    # Solve A*f = eig*B*f for eigs
    def solveProblems(self):
        from scipy.linalg import eig
        # Find eigenvalues and eigenvectors
        self.eValue, self.eVec = eig(self.A, self.B)
        
        # Use omega equation from eValue
        self.omega = (self.k*self.eValue/self.m)**(0.5)
        
        # make the key to sort the omega values in order of the modes
        self.key = sorted(range(self.N), key = lambda q: self.omega[q])
        
    
    # Plot the solution obtained by the approximation
    def plotSolution(self,mode):
        from matplotlib import pyplot as plt
        from numpy import zeros,cos,linspace
        self.tRange = linspace(0,4*pi/self.omega[self.key[mode]],20) # range of t (2 periods)
        # Do animation
        for t in self.tRange:
            plt.clf()
            plt.plot(self.D+self.eVec[:,self.key[mode]]*cos(self.omega[self.key[mode]]*t), zeros(self.N), '.')
            plt.xlim(0,self.Db)
            plt.ylim(-2,2)
            plt.draw()
            plt.pause(0.008)


# Initialize
a=0
b=2
Nm=10
myBVP = BoundaryValueProblem(a,b,Nm)

# Get and solve Matrices
myBVP.loadMatrices()
myBVP.solveProblems()

# Plot the animation with the given mode
mode = 2
myBVP.plotSolution(mode)
