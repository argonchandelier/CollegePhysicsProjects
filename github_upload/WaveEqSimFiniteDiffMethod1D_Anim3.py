# Logan Richan
# ph385

import numpy as np

class animatedWave:
    
    def __init__(self,a,b,c,N,tau,tMax):        
        # Define member variables
        self.a = a
        self.L = b
        self.c = c
        self.N = N
        self.tau = tau
        self.tMax = tMax
        
        # Build cell-centered grid with ghost points
        self.dx = (b-a)/float(N)
        self.x = np.linspace(a-self.dx/2., b+self.dx/2., self.N+2)
        
    def initializeWave(self):        
        # Initialize y which holds initial disturbance
        self.yInit = self.x * 0
        
        # Initialize v to hold initial velocity
        self.vInit = np.exp(-160*(self.x - self.L/2.)**2 / float(self.L**2))
        
    def animate(self):
        from matplotlib import pyplot as plt
        
        # Define the constant and y from initial y
        constant = self.c**2 * self.tau**2/(2*self.dx**2)
        y=self.yInit
        
        # Define variable to store wave at prev. time step
        yOld = y[1:-1] - self.vInit[1:-1]*self.tau + constant*(y[2:] - 2*y[1:-1] + y[:-2])
        # Enforce boundary conditions to set values for ghost points in yOld
        yOld = np.append(0,np.append(yOld,0))
        
        # Initialize time and counter
        t=0
        counter=0
        
        #Loop over time
        while t < self.tMax:
            #Calculate yNew
            yNew = 2*y[1:-1] - yOld[1:-1] + 2*constant*(y[2:] - 2*y[1:-1] + y[:-2])
            
            #Enforce boundary conditions to set values for ghost points.
            yNew = np.append(0,np.append(yNew,0))
            
            if counter % 20 == 0:
                #Animate the wave periodically
                plt.clf()
                plt.plot(self.x, y)
                plt.xlim(0,1)
                plt.ylim(-.1,.1)
                plt.draw()
                plt.pause(0.002)
            
            # Let yOld be equal to y
            yOld = np.copy(y)
            
            # Let y be yNew
            y = np.copy(yNew)
            
            t += self.tau
            counter += 1

# Get initial components
a=0
b=1.
c=2.
N=200
tau=0.0008

# Calculate h
h = (b-a)/float(N)

# Get the h/c to tau ratio, which should be no less than 1.
tauRel = h/c/tau
print(tauRel)

# Initialize the wave
wave = animatedWave(a,b,c,N,tau,1.1)
wave.initializeWave()
# Animate the wave over time
wave.animate()