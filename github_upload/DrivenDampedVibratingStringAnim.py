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
    
    # Find discrete fourier transform coefficients
    def DFT(self, samples):
        from numpy import exp, pi
        # Initial number of points and coefficients
        N = len(samples)
        gamma = []
        
        # Find coefficients
        for k in range(N//2 + 1): #N//2
            gammaK=0
            for n, yn in enumerate(samples):
                gammaK += yn * exp(-2j * pi * k * n/N) # Coefficient formula
            gamma.append(gammaK/N)
        return gamma
    
    # Animate the wave and take the Fourier transform over time
    def overTime(self, doAnimation=True):
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
        ts=[]
        counter=0
        f=[]
        ysamps = []
        
        for x in self.x:
            if x >= 0.8 and x <= 1:
                f.append(0.73)
            else:
                f.append(0)
        f = np.array(f)
        
        every = 100
        #Loop over time
        while t < self.tMax:
            #Calculate yNew
            yNew = (4*y[1:-1] + (self.g*self.tau-2)*yOld[1:-1] +\
                   4*constant*(y[2:] - 2*y[1:-1] + y[:-2])) / float(2 + self.g*self.tau) +\
                   f[1:-1]*np.cos(self.omega*t)*2*self.tau**2 / float(self.mu * (2+self.g*self.tau))
            
            #Enforce boundary conditions to set values for ghost points.
            yNew = np.append(0,np.append(yNew,0))
            
            if counter % every == 0:
                #Animate the wave periodically
                if doAnimation:
                    plt.clf() # Clear previous plot
                    plt.plot(self.x, yNew) # Plot the x vs. y of the string points for every 20 time steps
                    # Set reasonable limits to see the string propogating over time
                    plt.xlim(0,self.L)
                    plt.ylim(-.002,.002)
                    plt.draw()
                    plt.pause(0.00002)
                
                sampleAt = 0.5 # Point to sample y at for different times
                ysampindex=min(range(len(self.x)), key=lambda i: abs(self.x[i]-sampleAt))
                ysamps.append(yNew[ysampindex])
                ts.append(t)
            
            # Let yOld be equal to y
            yOld = np.copy(y)
            
            # Let y be yNew
            y = np.copy(yNew)
            
            # Increment values
            t += self.tau
            counter += 1
        
        
        plt.figure(2)
        
        # Take the Fourier transform by using the built in or user defined function:
        gamma = np.fft.rfft(ysamps) # 5s for tmax=1.5s
        #gamma = self.DFT(ysamps)   # 9s for tmax=1.5s
        
        sampFreq = 1./float(every*self.tau) # get the sample frequencies
        k = np.linspace(0,sampFreq//2,len(ysamps)//2 + 1) # make the length in Hz
        plt.plot(k,np.abs(gamma),'.') # plot frequencies
        plt.show()
        # peaked around 172 Hz

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
    wave = animatedWave(a,b,g,N,tau,0.5)
    wave.initializeWave()
    # Animate the wave over time
    wave.overTime(doAnimation=True)

# part e: the wave was also sampled at x=0.3 and was found to have the same frequency components
#         as x=0.5. This makes sense, as the frequency is of the entire string, of which all points
#         are a part of.
