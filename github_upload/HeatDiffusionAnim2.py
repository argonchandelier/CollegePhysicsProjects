# Logan Richan
# ph385

import numpy as np

class animatedWave:
    
    def __init__(self,L,D,N,tau,tMax):
        from numpy import linspace
        
        # Define member variables
        self.L = L
        self.N = N
        self.tau = tau
        self.tMax = tMax
        
        self.D = 7.
        self.L = 3.
        
        self.A=self.L/np.pi
        
        # Build cell-centered grid with ghost points
        self.dx = (L)/float(N)
        #self.x = linspace(self.dx/2., L-self.dx/2., self.N)
        self.x = linspace(0., L, self.N)
        
    def initializeWave(self):
        #define num waves
        self.n=3.
        
        # Initialize y which holds initial disturbance
        self.TInit = np.sin(self.n*np.pi*self.x/float(self.L))
        
    def animate(self):
        from numpy import zeros_like,copy
        from matplotlib import pyplot as plt
        T=self.TInit
        
        # Initialize time and counter
        t=0
        counter=0
        
        #Loop over time
        while t < self.tMax:
            #Calculate yNew
            TNew = T[1:-1] + self.D*self.tau/(self.dx**2) * (T[2:] - 2*T[1:-1] + T[:-2])
            
            #Enforce boundary conditions to set values for ghost points.
            TNew = np.append(0,np.append(TNew,0))
            
            TExact = self.TInit*self.A*np.exp((-self.D * self.n**2*np.pi**2/float(self.L**2))*t)
            
            if counter % 20 == 0:
                #Animate the wave periodically
                plt.clf()
                plt.plot(self.x, TNew)
                plt.plot(self.x, TExact)
                plt.xlim(0,3)
                plt.ylim(-1.2,1.2)
                plt.draw()
                plt.pause(0.002)
                
            
            # Let yOld be equal to y
            T = TNew
            
            t += self.tau
            counter += 1
            
        error = np.mean(abs(TExact - T))
        print("Error: " + str(error))

# Get initial components
L=3.
N=80
D=2.
tau=0.0001
tmax = 0.04

# Calculate h
h = (L)/float(N)

# Find C
C = tau*D/float(h**2)
#print(C)
# C is about 0.5


# Initialize the wave
wave = animatedWave(L,D,N,tau,tmax)
wave.initializeWave()
# Animate the wave over time
wave.animate()

# part b: D seems to be the related to the speed that heat diffuses through the material

# part c: sure enough, shorter wavelengths decay faster, as seen by increasing self.n