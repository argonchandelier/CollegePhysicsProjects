#######################
# In class assignment ph385
# Logan Richan
#######################
import numpy as np

class animatedWave:
    # Initialize the wave components
    def __init__(self,a,b,c,N,tau,tMax):        
        # Define member variables
        self.a = a # start of grid
        self.L = b # length of the string in m
        self.T = 1. # in N
        self.N = N # number of grid points
        self.tau = tau # time step
        self.tMax = tMax # final time
        
        # Build cell-centered grid with ghost points
        self.dx = (b-a)/float(N)
        self.x = np.linspace(a-self.dx/2., b+self.dx/2., self.N+2)
        
    # Initialize the initial y positions and velocities of the wave  
    def initializeWave(self):        
        # Initialize y which holds initial disturbance
        self.yInit = self.x * 0 # Initial y position is at 0 for all x.
        
        # Initialize v to hold initial velocity
        self.vInit = np.exp(-160*(self.x - self.L/2.)**2 / float(self.L**2))
    
    # Find c**2 as a function of x
    def cSqu(self):
        cS=[] # Initialize c**2
        for i in range(len(self.x)):
            # Get c**2 for all x using given equations for c(x) (and mu(x))
            cS.append((self.T / float(0.1 + self.x[i]/float(self.L)))**(0.5))
        return np.array(cS) # Return as an array so math can be done with it
    
    # Animate the wave
    def animate(self):
        from matplotlib import pyplot as plt
        
        # Define the constant and y from initial y
        constant = self.cSqu() * self.tau**2/(2*self.dx**2)
        y=self.yInit
        
        # Define variable to store wave at prev. time step
        yOld = y[1:-1] - self.vInit[1:-1]*self.tau + constant[1:-1]*(y[2:] - 2*y[1:-1] + y[:-2])
        # Enforce boundary conditions to set values for ghost points in yOld
        yOld = np.append(0,np.append(yOld,0))
        
        # Initialize time and counter
        t=0
        counter=0
        
        #Loop over time
        while t < self.tMax:
            #Calculate yNew
            yNew = 2*y[1:-1] - yOld[1:-1] + 2*constant[1:-1]*(y[2:] - 2*y[1:-1] + y[:-2])
            
            #Enforce boundary conditions to set values for ghost points.
            yNew = np.append(0,np.append(yNew,0))
            
            if counter % 20 == 0:
                #Animate the wave periodically
                plt.clf() # Clear previous plot
                plt.plot(self.x, yNew) # Plot the x vs. y of the string points for every 20 time steps
                # Set reasonable limits to see the string propogating over time
                plt.xlim(0,1)
                plt.ylim(-.1,.1)
                plt.draw()
                plt.pause(0.002)
            
            # Let yOld be equal to y
            yOld = np.copy(y)
            
            # Let y be yNew
            y = np.copy(yNew)
            
            # Increment values
            t += self.tau
            counter += 1

# Get initial components
a=0
b=1.
c=2.
N=200
tau=0.001

# Calculate h
h = (b-a)/float(N)

# Get the h/c to tau ratio, which should be no less than 1.
tauRel = h/c/tau
print(tauRel)

# Only animate the wave if the CFL condition is met
if tauRel >= 1:
    # Initialize the wave
    wave = animatedWave(a,b,c,N,tau,1.8)
    wave.initializeWave()
    # Animate the wave over time
    wave.animate()

# The pulses propagate through the wave faster on the left side of the string because there is
# a lower linear mass density the farther left on the wave you go, so there is a higher speed
# and meets up with the pulse going toward the right faster, so they meet toward the right side of the string.
# The pulse on the left then still moves faster, but has more distance to move, so when they meet again,
# they meet at the middle again.
