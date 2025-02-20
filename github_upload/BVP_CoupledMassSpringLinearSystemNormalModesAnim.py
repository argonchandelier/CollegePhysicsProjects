#######################
# PH385
# H13.2
# Logan Richan
#######################

from numpy import pi, exp

class BoundaryValueProblem:
    # Initialize N and grid space
    def __init__(self, a, b, N=6, k=[1000., 1000., 1000., 1000., 1000., 1000., 1000.], m=[3., 3., 3., 3., 3., 3.]):
        from numpy import linspace
        # define k and m
        self.k = k
        self.m = m
        
        # Get point of masses
        Da=0
        self.Db=10*N
        dD=(self.Db-Da)/float(N)
        self.D = linspace(0.+dD,self.Db-dD,N)
        
        #get cell edge grid
        self.N = N
        self.dx = (b-a)/float(N)
        self.x,self.dx = linspace(a-self.dx/2.,b+self.dx/2.,N+2,retstep=True)
        
    
    # Create the matrices
    def loadMatrices(self):
        from numpy import zeros, eye
        #get m and k
        m=self.m
        k=self.k
        
        self.A = zeros([self.N,self.N]) # Initialize A in Ax=lambda*B*x
        self.B = eye(self.N,self.N) # B is the Identity matrix
        
        # Find first 2 rows of A and initial B
        self.A[0,0] = (k[0] + k[1])/m[0]
        self.A[0,1] = -k[1]/m[0]
        self.A[-1,-2] = -k[-2]/m[-1]
        self.A[-1,-1] = (k[-1] + k[-2])/m[-1]
        
      
        # Find the rest of A and B
        for i in range(1, self.N -1):
            self.A[i,i] = (k[i] + k[i+1])/m[i]
            self.A[i,i+1] = -k[i+1]/m[i]
            self.A[i,i-1] = -k[i]/m[i]
    
    # Solve A*f = eig*B*f for eigs
    def solveProblems(self):
        from scipy.linalg import eig
        # Find eigenvalues and eigenvectors
        self.eValue, self.eVec = eig(self.A, self.B)
        
        # Use omega equation from eValue
        self.omega = (self.eValue)**(0.5)
        
        # make the key to sort the omega values in order of the modes
        self.key = sorted(range(self.N), key = lambda k: self.omega[k])
        
        print(self.eVec[2])
        
    
    # Plot the solution obtained by the approximation
    def plotSolution(self,mode,plotType='.'):
        from matplotlib import pyplot as plt
        from numpy import zeros,cos,linspace
        self.tRange = linspace(0,4*pi/self.omega[self.key[mode]],20) # range of t (2 periods)
        # Do animation
        for t in self.tRange:
            plt.clf() # Clear plot
            
            # Plot the masses with their positon
            plt.plot(self.D+self.eVec[:,self.key[mode]]*cos(self.omega[self.key[mode]]*t), zeros(self.N), plotType)
            plt.xlim(0,self.Db)
            plt.ylim(-2,2)
            plt.xlabel("distance in m")
            plt.draw()
            plt.pause(0.008)
    


# Initialize
a=0
b=2
k = [1000., 1200., 1400., 1600., 1800., 2000., 2200.]
m = [3., 8., 3., 3., 8., 3.]

# Make sure there is 1 more spring than there are masses 
if len(m) == len(k)-1:
    myBVP = BoundaryValueProblem(a,b,N=len(m),k=k,m=m) # Initialize
    
    # Get and solve Matrices
    myBVP.loadMatrices()
    myBVP.solveProblems()
        
    # Plot the animation with the given mode
    myBVP.plotSolution(3) # Plot 3rd normal mode
    myBVP.plotSolution(5,plotType='.r') # Plot 5th normal mode
