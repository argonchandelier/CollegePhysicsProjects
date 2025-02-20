# Logan Richan
# ph385 assignment

import numpy as np
from matplotlib import pyplot as plt

class Schrodinger:
    # Initialize class
    def __init__(self,b,N,tau,V0):
        # Initialize constants
        self.L = b
        self.N = N
        self.tau = float(tau)
        self.V0 = float(V0)
        
        # Create grid
        self.dx = 2 * b/N
        self.x,self.dx = np.linspace(-2*self.L,2*self.L,N,retstep=True)
        
        self.Vx = np.array([self.V(i) for i in self.x],float)
    
    # Define potential
    def V(self,x):
        # (part c) Extra increase of the width of the barrier (toward the right; from a width of 0.02L)
        extraWidth = 0.04
        
        # Potential at each region
        if (-2*self.L < x and x < 0.98*self.L) or ((1.+extraWidth)*self.L < x and x < 2*self.L):
            return 0
        elif -2*self.L >= x or x >= 2*self.L:
            return 1e10 # Infinite barrier
        else:
            return self.V0 # square barrier
    
    # Initial wave packet
    def initializeWaveFunction(self,sigma):
        self.psi = 1./np.sqrt(sigma * np.sqrt(np.pi)) * np.exp(2j * np.pi * self.x) * np.exp(-self.x**2/float(2*sigma**2))
    
    # Use an integration function to find probability and expectation value
    def Integrate(self, f):
        return sum((f[1:] + f[:-1])/2.* self.dx)
    
    # Find H*Psi for a given psi
    def HPsi(self, psi):
        return np.append(0,np.append(-self.hbar**2/(self.m*2.) * \
                ((psi[2:] - 2*psi[1:-1] + psi[:-2]))/float(self.dx**2) + self.Vx[1:-1]*psi[1:-1],0))
    
    # Find the matrices of the problem
    def loadMatrices(self):
        # Initialize matrices
        A = np.zeros([self.N,self.N],dtype=complex)
        self.B = np.zeros([self.N,self.N],dtype=complex)
        
        # Set hbar and m to be 1 in this probleem
        hbar = self.hbar = 1.
        m = self.m = 1.
        
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
        
        # Get ab matrix from banded matrix A
        ud = np.insert(np.diag(A,1),0,0)
        d = np.diag(A)
        ld = np.insert(np.diag(A,-1),-1,0)
        self.ab = np.matrix([ud,d,ld])
    
    # animate the wave equation through time
    def animate(self,tMax):
        from scipy.linalg import solve_banded

        
        # Initialize t and counter
        t = 0
        counter = 0
        
        # Get and print the pulse energy
        expEnergy = np.real(self.Integrate(np.conjugate(self.psi) * self.HPsi(self.psi)))
        print(expEnergy)
        
        # Find equation over timee
        plt.figure(1)
        VdivV0 = self.Vx/V0
        while t < tMax:
            # Plot every 5 iterations
            if counter % 5 == 0:
                plt.clf()
                psisq = np.conjugate(self.psi) * self.psi
                plt.plot(self.x, psisq, 'r.-')
                plt.plot(self.x, VdivV0, 'b-')
                plt.ylim(-0.1,1.1)
                plt.draw()
                plt.pause(1e-4)
            
            # Solve for psi at next time step
            b = np.dot(self.B,self.psi)
            self.psi = solve_banded((1,1),self.ab,b)
            
            # Increment counters
            counter += 1
            t += self.tau
        
        
# Define constants
b=10. # given L
N=200 # amount of points shown
tau=5e-2 # time step
sigma=2. # width
tMax=12.0 # maximum time

V0 = 20 # Potential barrier energy of square hill

# Initialize and animate the wave equation
sch = Schrodinger(b,N,tau,V0)
sch.initializeWaveFunction(sigma)
sch.loadMatrices()
sch.animate(tMax)

# part a: switching the sign on p causes the wave packet to move in the other direction

# part b: The wave generally gets transmitted at V0 values lower than the pulse energy and
# generally gets reflected for V0 higher than the pulse energy

# part c: the greater the width, the more of the wave gets reflected