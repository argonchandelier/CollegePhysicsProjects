##############
# PH385 Test # 3
# Problem # 1
# Logan Richan
################

import numpy as np
from matplotlib import pyplot as plt

plt.close('all')

class diffusion():
    # Initialize the class
    def __init__(self,A,B,L,D,P,Tf,N,tau,tmax):
        # Variables of the function of T_0(t)
        self.A = A
        self.B = B
        
        self.L = L # Depth of the Earth plotted
        self.D = D # Diffusion constant
        self.P = float(P) # The period of the Earth (365 days)
        self.Tf = Tf # Temperature at the final depth
                        
        self.N = N # number of points used in plotting and calculations
        self.tau = tau # Time steps
        self.tmax = tmax # End time
        
        self.x,self.h=np.linspace(0,L,N,retstep=True) # Cell edge grid
    
    # Function for the temperature at the surface
    def surfaceT(self,t):
        return self.A + self.B*np.sin(2.*np.pi*t/P)
    
    # Initial distribution of temperature
    def initializeWave(self):
        self.Tinit = self.x*0 + 10.
        self.Tinit[0] = self.surfaceT(0)
        self.Tinit[-1] = self.Tf
    
    # Create the matrices used in calculations
    def loadMatrices(self):
        # Initialize matrices
        self.F = np.zeros((self.N,self.N))
        self.G = np.zeros((self.N,self.N))
        
        # Get first and last row components
        self.F[0,0] = 1
        self.F[-1,-1] = 1
        self.G[-1,-1] = 1
        
        # Find components for the other rows
        for i in range(1,self.N-1):
            self.F[i,i-1] = -self.D
            self.F[i,i] =   2*self.h**2/self.tau + 2*D
            self.F[i,i+1] = -self.D
            self.G[i,i-1] = self.D
            self.G[i,i] =   2*self.h**2/self.tau - 2*D
            self.G[i,i+1] = self.D
        
    def diffuse(self):
        # Set the temperature      
        T = self.Tinit
        
        # Initialize time and counter
        ts = np.arange(0,self.tmax+self.tau,self.tau)
        counter = 0
        
        # Loop through time in steps
        for t in ts:
            # Find T for the next time step
            GT = np.dot(self.G, T)
            GT[0] = self.surfaceT(t)
            Tnew = np.dot(np.linalg.inv(self.F), GT)
            
            # Plot T vs. depth every 50 iterations
            if counter % 100 == 0:
                plt.clf()
                plt.plot(self.x,Tnew)
                plt.ylim(-2,22)
                plt.xlabel("Depth in m")
                plt.ylabel("Temperature in Celsius")
                plt.draw()
                plt.pause(0.0002)
            
            # make Tnew older
            T = np.copy(Tnew)
            
            # Increment counter
            counter += 1

# Set constants
A=10. # C
B=12. # C
L=20. # m
D=0.1 # m^2/day
P=365. # days
Tf=11. # C

N=200 # Number of points
tau=0.1 # days
tmax=P*10. # 10 years

# Initialize and find the Temperature over time across the first 20m of the Earth's crust's depth
earth = diffusion(A,B,L,D,P,Tf,N,tau,tmax)
earth.initializeWave()
earth.loadMatrices()
earth.diffuse()