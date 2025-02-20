##############
# PH385 Test 2
# Problem # 1
# Logan Richan
################

import numpy as np
from matplotlib import pyplot as plt

class string:
    # Initialize variables
    def __init__(self,L,N):
        self.L=L # Length of the string in m
        self.N=int(N) # Number of points on the string
        self.T=10. # Tension of the string in Newtons
        
        self.x,self.dx = np.linspace(0,self.L,self.N,retstep=True) # Cell edge grid for string points' x postions
        self.mu = 0.003 + 0.1*self.x # given mu(x) function for linear mass density (made to be kg/m)
    
    # Find the A and B matrices
    def loadMatrices(self):
        # Initialize A and B matrices as a 0 matrix and identity matrix, respectively
        self.A = np.zeros([self.N,self.N])
        self.B = np.eye(self.N,self.N)
        
        # Set first and last rows of A and B matrices
        self.A[0,0]   = 1
        self.A[-1,-1] = 1
        self.B[0,0]   = 0
        self.B[-1,-1] = 0
        
        # Get all other components of A
        for i in range(1, self.N-1):
            self.A[i,i-1] =  1./float(self.mu[i]*self.dx**2)
            self.A[i,i]   = -2./float(self.mu[i]*self.dx**2)
            self.A[i,i+1] =  1./float(self.mu[i]*self.dx**2)
    
    # Solve for the eigenvalues and eigenvectors in A*y = lambda*B*f
    def solveMatrices(self):
        from scipy.linalg import eig
        
        # Solve for the eigenvalues and their eigen vectors
        self.eVals, self.eVecs = eig(self.A, self.B)
        
        # Get the omega values for the eigenvalues
        self.omega = (-self.T*self.eVals)**(0.5)
        
        # Get the key to sort the omega values
        self.key = sorted(range(self.N), key = lambda k: self.omega[k])
    
    # Plot the string for a given mode
    def plot(self, mode):
        plt.plot(self.x, self.eVecs[:,self.key[mode]])
        plt.show()

# Initialize variables and string
L=3.
N=100
myString = string(L,N)

# Get and solve the matrices to obtain the frequencies for the normal modes
myString.loadMatrices()
myString.solveMatrices()

# Plot the first four normal modes
for i in range(4):
    plt.figure(i+1)
    myString.plot(i)

# This is an eigenvalue problem because when solving the matrices for their eigenvalues,
# those eigenvalues can then be used to solve for the resonant frequencies, which would
# give the normal modes
    