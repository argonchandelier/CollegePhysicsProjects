# Logan Richan
# ph385

import numpy as np

class animatedWave:
    # Initialize the wave components
    def __init__(self,a,b,g,N,tau,tMax):        
        # Define member variables
        self.a = a # start of grid
        self.L = b # length of the string in m
        self.T = 127. # in N
        self.g = g # damping constant
        self.N = N # number of grid points
        self.tau = tau # time step
        self.tMax = tMax # final time
        
        self.omega = 1080. #400. #2*np.pi/0.5
        self.mu = 0.003
        self.c = (self.T/float(self.mu))**(0.5) # speed
        
        # Build cell-centered grid with ghost points
        self.dx = (b-a)/float(N)
        self.x = np.linspace(a-self.dx/2., b+self.dx/2., self.N+2)
        
    # Initialize the initial y positions and velocities of the wave  
    def initializeWave(self):        
        # Initialize y which holds initial disturbance
        self.yInit = self.x * 0
        
        # Initialize v to hold initial velocity
        self.vInit = self.x * 0
     
    # Animate the wave
    def animate(self):
        from matplotlib import pyplot as plt
        
        # Define the constant and y from initial y
        constant = self.c**2 * self.tau**2/(2*self.dx**2)
        y=self.yInit
        
        # Define variable to store wave at prev. time step
        yOld = -self.vInit[1:-1]*(self.tau*(2+self.g*self.tau))/2. + y[1:-1] + \
                constant*(y[2:] - 2*y[1:-1] + y[:-2])
        # Enforce boundary conditions to set values for ghost points in yOld
        yOld = np.append(0,np.append(yOld,0))
        
        # Initialize variables
        t=0
        #ts=[]
        #fit=[]
        counter=0
        #yMax = []
        f=[]
        
        for x in self.x:
            if x >= 0.8 and x <= 1:
                f.append(0.73)
            else:
                f.append(0)
        f = np.array(f)
        print(f)
        
        #Loop over time
        while t < self.tMax:
            #Calculate yNew
            yNew = (4*y[1:-1] + (self.g*self.tau-2)*yOld[1:-1] +\
                   4*constant*(y[2:] - 2*y[1:-1] + y[:-2])) / float(2 + self.g*self.tau) +\
                   f[1:-1]*np.cos(self.omega*t)*2*self.tau**2 / float(self.mu * (2+self.g*self.tau))
            
            #Enforce boundary conditions to set values for ghost points.
            yNew = np.append(0,np.append(yNew,0))
            
            # Append values for max amplitude over time graph
            #ts.append(t)
            #fit.append(0.035*np.exp(-self.g*t/2.))
            #yMax.append(max(abs(yNew)))
            
            if counter % 100 == 0:
                #Animate the wave periodically
                plt.clf() # Clear previous plot
                plt.plot(self.x, yNew) # Plot the x vs. y of the string points for every 20 time steps
                # Set reasonable limits to see the string propogating over time
                plt.xlim(0,self.L)
                plt.ylim(-.001,.001)
                plt.draw()
                plt.pause(0.00002)
            
            # Let yOld be equal to y
            yOld = np.copy(y)
            
            # Let y be yNew
            y = np.copy(yNew)
            
            # Increment values
            t += self.tau
            counter += 1
        
        
        #plt.figure(2)
        #plt.plot(ts, fit)
        #plt.plot(ts, yMax)
        #plt.show()

# Get initial components
a=0
b=1.2
c=2.
g=20
N=200
tau=0.00001

# Calculate h
h = (b-a)/float(N)

# Get the h/c to tau ratio, which should be no less than 1.
tauRel = h/c/tau
print(tauRel)

# Only animate the wave if the CFL condition is met
if tauRel >= 1:
    # Initialize the wave
    wave = animatedWave(a,b,g,N,tau,.25)
    wave.initializeWave()
    # Animate the wave over time
    wave.animate()

# part e: This fit works well because the solution to this problem will have the form of some exponential
# decay function multiplied by a periodic function. The exponential decay function would probably
# then be the e^(-gt/2) function, so that at the maximum of the periodic function, the exponential
# function can be seen