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
        self.x = linspace(0.-self.dx/2., L+self.dx/2., self.N+2)
        
    def initializeWave(self):
        # Initialize y which holds initial disturbance
        self.TInit = np.exp(-40 * (self.x/float(self.L)-0.5)**2)
        
    def animate(self):
        from numpy import zeros_like,copy
        from matplotlib import pyplot as plt
        # Initial temperature
        T=self.TInit
        T2=self.TInit
        T3=self.TInit
        
        # Initialize time and counter
        t=0
        counter=0
        
        self.Dx = self.D * (self.x**2 + self.L/5.)/(self.L/5.)
        self.DxP = 2. * self.D * self.x / float(self.L/5.)
        
        #Loop over time
        while t < self.tMax:
            #Calculate TNew
            TNew = T[1:-1] + self.D*self.tau/(self.dx**2) * (T[2:] - 2*T[1:-1] + T[:-2])
            TNew2 = T2[1:-1] + self.D*self.tau/(self.dx**2) * (T2[2:] - 2*T2[1:-1] + T2[:-2])
            TNew3 = T3[1:-1] + self.Dx[1:-1]*self.tau/(self.dx**2) * (T3[2:] - 2*T3[1:-1] + T3[:-2]) + \
                   self.DxP[1:-1]*self.tau * (T3[2:] - T3[:-2])/float(2.*self.dx)
            
            #Enforce boundary conditions to set values for ghost points.
            TNew = np.append(0,np.append(TNew,0))
            TNew2 = np.append(TNew2[0],np.append(TNew2,TNew2[-1]))
            TNew3 = np.append(0,np.append(TNew3,0))
            
            #TExact = self.TInit*self.A*np.exp((-self.D * self.n**2*np.pi**2/float(self.L**2))*t)
            
            if counter % 20 == 0:
                #Animate the wave periodically
                plt.clf()
                plt.plot(self.x, TNew)
                plt.plot(self.x, TNew2)
                plt.plot(self.x, TNew3)
                plt.xlim(0,self.L)
                plt.ylim(-0.2,1.2)
                plt.draw()
                plt.pause(0.002)
                
            
            # Let T be equal to TNew
            T = TNew
            T2 = TNew2
            T3 = TNew3
            
            t += self.tau
            counter += 1

# Get initial components
L=3.
N=40
D=2.
tau=0.00001
tmax = 0.03

# Calculate h
h = (L)/float(N)

# Find C
C = tau*D/float(h**2)
print(C)
# C is about 0.5


# Initialize the wave
wave = animatedWave(L,D,N,tau,tmax)
wave.initializeWave()
# Animate the wave over time
wave.animate()

# part a: The boundary condition for part i is like a watermelon being connected at both ends to an
# insulated material that is at a constant temperature, and for the second, it is like the
# watermelon is in a vacuum where it cannot change heat with its surroundings

# part b: T(x,t) behaves in this way because the material is more conductive to heat the further right
# the material goes, so heat diffuses faster on the right side of the material
