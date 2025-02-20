# Logan Richan
# ph385

from numpy import pi

class BoundaryValueProblem:
    # Initialize N and grid space
    def __init__(self, a, b, N):
        from numpy import linspace
        
        # Given constants
        self.L = b
        self.mu = 0.003
        self.T = 127.
        
        # Grid creation
        self.N = N
        self.dx = (b-a)/float(N)
        self.x,self.dx = linspace(a,b,N,retstep=True)
    
    # Create the matrices
    def loadMatrices(self):
        from numpy import zeros, eye
        h=float(self.dx)
        self.A = zeros([self.N,self.N]) # Initialize A in Ay=b
        self.B = eye(self.N,self.N)
        
        # Find first and last rows of A
        self.A[0,0] = 1
        self.A[-1,-3] =  1/(2.*h)
        self.A[-1,-2] = -2/h
        self.A[-1,-1] =  3/(2.*h) - 2
        # Set endpoints of B
        self.B[0,0] = 0
        self.B[-1,-1] = 0
      
        # Find the rest of A
        for i in range(1, self.N - 1):
            # Get diagonal A values
            self.A[i,i-1] =  1/h**2
            self.A[i,i]   = -2/h**2
            self.A[i,i+1] =  1/h**2
        #print(self.B)
    
    # Do a linear algebra solver for y in A*g = lambda*B*g
    def solveProblems(self):
        from scipy.linalg import eig
        self.eValue, self.eVec = eig(self.A, self.B)
        
        self.omega = (-self.T * self.eValue / float(self.mu))**(0.5) # omega values
        self.key = sorted(range(self.N), key = lambda k: self.omega[k]) # omega sorter
        
    
    # Plot the solution obtained by the approximation
    def plotSolution(self,mode):
        from matplotlib import pyplot
        pyplot.plot(self.x,self.eVec[:,self.key[mode]])
        pyplot.title("Frequency: " + str(self.omega[self.key[mode]].real))
        pyplot.show()
        
        # Compare g'(L) and 2*g(L) to check that they are the same
        gPrimeL = self.A[-1,-3]*self.eVec[:,self.key[mode]][-3] +\
                  self.A[-1,-2]*self.eVec[:,self.key[mode]][-2] +\
                  (self.A[-1,-1]+2)*self.eVec[:,self.key[mode]][-1]
        gL = self.eVec[:,self.key[mode]][-1]
        print("g'(L) = " + str(gPrimeL) + ", and 2*g(L) = " + str(2*gL.real) + ", which should be the same.")
        
        return self.omega[self.key[mode]].real
    
    # Find the actual resonant frequency at a given mode
    def realFreq(self, mode):
        return mode * pi / float(self.L) * (self.T/float(self.mu))**(0.5)

# Initialize
a=0
b=1.2
N=100
myBVP = BoundaryValueProblem(a,b,N)

# Get and solve Matrices
myBVP.loadMatrices()
myBVP.solveProblems()

# Find the frequency at the resonant modes and compare to the actual frequencies
mode = 3
freq = myBVP.plotSolution(mode)

# Part a: The resonant frequencies change because the boundary condition on the left of the string 
# was set to be at a derivative of 0, which is at a peak or trough