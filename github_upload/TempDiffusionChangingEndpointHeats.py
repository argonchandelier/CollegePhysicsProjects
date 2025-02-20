# Logan Richan
# ph385

import numpy as np
from scipy.linalg import solve_banded, inv

class animatedWave:
    # Initialize the variables
    def __init__(self,L,N,tau,tMax):
        from numpy import linspace
        
        # Define member variables
        self.L = L
        self.N = N
        self.tau = float(tau)
        self.tMax = tMax
        
        self.a=self.L/np.pi
        
        # Build cell-centered grid with ghost points
        self.dx = (L)/float(N)
        self.x = linspace(0.-self.dx/2., self.L+self.dx/2., self.N+2)
   
    # Define D(x) 
    def D(self, x):
        return 2.
    
    # Get the initial wave function
    def initialize(self):
        # Initialize y which holds initial disturbance
        self.TInit = np.sin(np.pi*self.x/float(self.L))
    
    # Create the matrices    
    def loadMatrices(self):
        # Initialize the matrices
        self.A = np.zeros([self.N+2,self.N+2])
        self.B = np.zeros([self.N+2,self.N+2])
        
        # Get the first and last rows
        self.A[0,0]=-1./self.dx
        self.A[0,1]=1./self.dx
        self.A[-1,-1]=1./self.dx
        self.A[-1,-2]=-1./self.dx
        
        # Get the elements in the other rows
        for i in range(1,self.N+1):
            self.A[i,i-1] = -self.D(self.x[i]-self.dx/2.)
            self.A[i,i] = 2*self.dx**2 / self.tau + (self.D(self.x[i]+self.dx/2.) + self.D(self.x[i]-self.dx/2.))
            self.A[i,i+1] = -self.D(self.x[i]+self.dx/2.)
            self.B[i,i-1] = self.D(self.x[i]-self.dx/2.)
            self.B[i,i] = 2*self.dx**2 / self.tau - (self.D(self.x[i]+self.dx/2.) + self.D(self.x[i]-self.dx/2.))
            self.B[i,i+1] = self.D(self.x[i]+self.dx/2.)

        ud = np.insert(np.diag(self.A,1),0,0)
        d = np.diag(self.A)
        ld = np.insert(np.diag(self.A,-1),-1,0)
        self.ab = np.matrix([ud,d,ld])
        
    def animate(self):
        from matplotlib import pyplot as plt
        T=self.TInit
        
        # Initialize time and counter
        t=0
        counter=0
        
        #Loop over time
        while t < self.tMax:
            # Get TNew:
            BTn = np.dot(self.B, T)
            BTn[0] = -1. # Derivative boundary condition at x = 0
            BTn[-1] = 2. # Derivative boundary condition at x = L
            TNew = np.dot(inv(self.A), BTn)
            
            if counter % 20 == 0:
                #Animate the wave periodically
                plt.clf()
                plt.plot(self.x, TNew)
                plt.xlim(0,L)
                plt.ylim(-5.1,6.2)
                plt.draw()
                plt.pause(0.2)
                
            
            # Let TOld be equal to T
            T = TNew
            
            # Increment counters
            t += self.tau
            counter += 1

# Get initial components
L=3.
N=40
tau=0.004
tmax = 1.5

# Calculate h
h = (L)/float(N)

# Find C through testing trials and seeing what seems to pass the CFL condition
C = tau/float(h**2)
#print(C)
# C is about 0.5


# Initialize the wave
wave = animatedWave(L,N,tau,tmax)
wave.initialize()
wave.loadMatrices()

# Animate the wave over time
wave.animate()

# This animation makes sense, and is showing the rate of temperature change by -1 on the left end
# and 2 on the right end (per dx). The full curve moves upward because the net change in temperature is
# positive. When the derivative boundary conditions are equal but opposite values, there is no change
# in the total curve's position
