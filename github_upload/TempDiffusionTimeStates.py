# Logan Richan
# ph385

import numpy as np
from scipy.linalg import solve_banded, inv
from matplotlib import pyplot as plt

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
        if x < self.L/2.:
            return 1.
        else:
            return 5.
    
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

        T=self.TInit
        
        # Initialize time and counter
        t=0
        counter=0
        
        #Loop over time
        qq=1
        while t < self.tMax:
            # Get TNew
            AinvB = np.dot(inv(self.A), self.B)
            TNew = np.dot(AinvB, T)
            #TNew = solve_banded((1,1), self.ab, T)
            '''
            if counter % 100 == 0:
                #Animate the wave periodically
                plt.clf()
                plt.plot(self.x, TNew)
                plt.title("a")
                plt.xlim(0,L)
                plt.ylim(-0.1,1.2)
                plt.draw()
                plt.pause(0.2)
            '''
            
            if qq == 1:
                #plt.figure(1)
                plt.subplot(231)
                plt.plot(self.x, T)
                plt.title("t = 0.0")
                plt.xlim(0,L)
                plt.ylim(-0.1,1.2)
                plt.ylabel("Temperature")
                #plt.show()
                qq+=1
            if t > 0.05 and qq == 2:
                #plt.figure(qq)
                plt.subplot(232)
                plt.plot(self.x, TNew)
                plt.title("t = 0.05")
                plt.xlim(0,L)
                plt.ylim(-0.1,1.2)
                #plt.show()
                qq+=1
            if t > 0.2 and qq == 3:
                #plt.figure(qq)
                plt.subplot(233)
                plt.plot(self.x, TNew)
                plt.title("t = 0.2")
                plt.xlim(0,L)
                plt.ylim(-0.1,1.2)
                #plt.show()
                qq+=1
            if t > 0.5 and qq == 4:
                #plt.figure(qq)
                plt.subplot(234)
                plt.plot(self.x, TNew)
                plt.title("t = 0.5")
                plt.xlim(0,L)
                plt.ylim(-0.1,1.2)
                plt.ylabel("Temperature")
                plt.xlabel("Position")
                #plt.show()
                qq+=1
            if t > 1.5 and qq == 5:
                #plt.figure(qq)
                plt.subplot(235)
                plt.plot(self.x, TNew)
                plt.title("t = 1.5")
                plt.xlim(0,L)
                plt.ylim(-0.1,1.2)
                plt.xlabel("Position")
                #plt.show()
                qq+=1
            if t > 3.0 and qq == 6:
                #plt.figure(qq)
                plt.subplot(236)
                plt.plot(self.x, TNew)
                plt.title("t = 3.0")
                plt.xlim(0,L)
                plt.ylim(-0.1,1.2)
                plt.xlabel("Position")
                #plt.show()
                qq+=1
                
            
            # Let TOld be equal to T
            T = TNew
            
            # Increment counters
            t += self.tau
            counter += 1

# Get initial components
L=3.
N=40
tau=0.0008
tmax = 3.2#1.99

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

plt.show()

# part b: the final temperature is the same because the rod starts off at the same temperature in
# both cases. Since the boundary condition implies that no temperature is exchanged with the surroundings,
# so the total energy of the system remains constant. When the heat dissipates, it spreads so that the
# entire rod has the same temperature everywhere, so the rod will have the average temperature everywhere.
# Since the initial temperatures are the same, so is the average temperature, so T does not change.
# The different D only affects how fast the temperature dissapates, but it will end up in the same final state.