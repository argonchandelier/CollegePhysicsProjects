# Logan Richan
# ph385

import numpy as np

class animatedWave:
    # Initialize the wave components
    def __init__(self,a,b,gm,N,tau,tMax):        
        # Define member variables
        self.a = a # start of grid
        self.L = b # length of the string in m
        self.gm = gm # damping constant
        self.g = 10.
        self.N = N # number of grid points
        self.tau = tau # time step
        self.tMax = tMax # final time
        
        self.omega = 15. #400. #2*np.pi/0.5
        self.mu = 0.003
        
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
        y = np.copy(self.yInit)
        
        # Define variable to store wave at prev. time step
        yOld = np.copy(self.yInit)
                
        # Initialize variables
        t=0
        #ts=[]
        #fit=[]
        counter=0
        #yMax = []
        f=[]
        
        for x in self.x:
            if x >= 0 and x <= 0.2:
                f.append(0.73)
            else:
                f.append(0)
        f = np.array(f)
        print(f)
        
        #Loop over time
        while t < self.tMax:
            #Calculate yNew
            yNew = (2*self.tau**2 / float(2 + self.gm*self.tau)) * ( f[1:-1]*np.cos(self.omega*t)/self.mu +\
                    (self.g/float(2*self.dx))*(y[2:]-y[:-2]) + (self.g*self.x[1:-1]/float(self.dx**2)) * (y[2:]-2*y[1:-1]+y[:-2]) +\
                    (2*y[1:-1]-yOld[1:-1])/self.tau**2 + (self.gm/float(2.*self.tau))*yOld[1:-1] )
            
            #Enforce boundary conditions to set values for ghost points.
            yNew0 = (1 / float(2+self.gm*self.tau)) * ( 4*self.tau**2*f[1]*np.cos(self.omega*t)/self.mu - \
                    (2-self.gm*self.tau)*(yOld[1]+yOld[0]) + 4.*(y[1]+y[0]) + \
                    4*self.tau**2*self.g*(y[1]-y[0])/self.dx ) - yNew[0]
            yNew = np.append(yNew0,np.append(yNew,-yNew[-1]))
            
            # Append values for max amplitude over time graph
            #ts.append(t)
            #fit.append(0.035*np.exp(-self.g*t/2.))
            #yMax.append(max(abs(yNew)))
            
            if counter % 100 == 0:
                #Animate the wave periodically
                plt.clf() # Clear previous plot
                plt.plot(yNew, self.x) # Plot the x vs. y of the string points for every 20 time steps
                # Set reasonable limits to see the string propogating over time
                plt.ylim(0,self.L)
                plt.xlim(-1.,1.)
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
gm=20
N=200
tau=0.0001
tMax=1.5

# Calculate h
h = (b-a)/float(N)

# Get the h/c to tau ratio, which should be no less than 1.
tauRel = h/c/tau
print(tauRel)

# Only animate the wave if the CFL condition is met
if tauRel >= 1:
    # Initialize the wave
    wave = animatedWave(a,b,gm,N,tau,tMax)
    wave.initializeWave()
    # Animate the wave over time
    wave.animate()
