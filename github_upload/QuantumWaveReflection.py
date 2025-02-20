# Logan Richan
# ph385

import numpy as np
from matplotlib import pyplot as plt

class Schrodinger:
    # Initialize class
    def __init__(self,b,N,tau):
        # Initialize constants
        self.L = b
        self.N = N
        self.tau = float(tau)
        
        # Create grid
        self.dx = 2 * b/N
        self.x,self.dx = np.linspace(-self.L,self.L,N,retstep=True)
    
    # Define potential
    def V(self,x):
        if -self.L <= x <= self.L:
            return 0
        else:
            return 1e10 # Infinite barrier
    
    # Initial wave packet
    def initializeWaveFunction(self,sigma):
        self.psi = 1./np.sqrt(sigma * np.sqrt(np.pi)) * np.exp(2j * np.pi * self.x) * np.exp(-self.x**2/float(2*sigma**2))
        
        # Find normalization constant (should already be =1)
        print(self.Integrate(np.conjugate(self.psi) * self.psi))
    
    # Use an integration function to find probability and expectation value
    def Integrate(self, f):
        return sum((f[1:] + f[:-1])/2.* self.dx)
    
    # Find the matrices of the problem
    def loadMatrices(self):
        # Initialize matrices
        A = np.zeros([self.N,self.N],dtype=complex)
        self.B = np.zeros([self.N,self.N],dtype=complex)
        
        # Set hbar and m to be 1 in this probleem
        hbar = 1.
        m = 1.
        
        # Set diagonal eleement in matrices
        for i in range(1,self.N-1):
            A[i,i-1] = hbar**2/float(4*m*self.dx**2)
            A[i,i] = 1j*hbar/self.tau - hbar**2/float(2*m*self.dx**2) - self.V(self.x[i])/2.
            A[i,i+1] = hbar**2/float(4*m*self.dx**2)
            self.B[i,i-1] = -hbar**2/float(4*m*self.dx**2)
            self.B[i,i] = 1j*hbar/self.tau + hbar**2/float(2*m*self.dx**2) + self.V(self.x[i])/2.
            self.B[i,i+1] = -hbar**2/float(4*m*self.dx**2)
        
        # Set first and last rows in matrices
        A[0,0] = 1
        A[-1,-1] = 1
        
        # Get ab matrix from bandeed matrix A
        ud = np.insert(np.diag(A,1),0,0)
        d = np.diag(A)
        ld = np.insert(np.diag(A,-1),-1,0)
        self.ab = np.matrix([ud,d,ld])
    
    # animate the wave equation through time
    def animate(self,tMax):
        from scipy.linalg import solve_banded
        
        # Initialize normalization constnts and expeectation values over time
        Ints = []
        expVals = [self.Integrate(np.conjugate(self.psi)*self.psi*self.x)]
        
        # Initialize t and counter
        t = 0
        ts = [t]
        counter = 0
        
        # Find equation over timee
        plt.figure(1)
        while t < tMax:
            if counter % 5 == 0:
                plt.clf()
                psisq = np.conjugate(self.psi) * self.psi
                Ints.append(self.Integrate(psisq))
                expVals.append(self.Integrate(psisq*self.x))
                ts.append(t)
                plt.plot(self.x,psisq, 'r.-')
                plt.ylim(-0.1,1.)
                plt.draw()
                plt.pause(1e-4)
            
            b = np.dot(self.B,self.psi)
            
            self.psi = solve_banded((1,1),self.ab,b)
            counter += 1
            t += self.tau
        
        print(Ints)
        
        plt.figure(2)
        plt.plot(ts,expVals)
        plt.show()
        
        
# Define constants
b=10.
N=200
tau=5e-3
sigma=.8
tMax=3.0

# Initialize and animate the wave equation
sch = Schrodinger(b,N,tau)
sch.initializeWaveFunction(sigma)
sch.loadMatrices()
sch.animate(tMax)

# part a: switching the sign on p causes the wave packet to move in the other direction

