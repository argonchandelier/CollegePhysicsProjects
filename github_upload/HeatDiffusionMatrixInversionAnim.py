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
        #self.x = linspace(self.dx/2., L-self.dx/2., self.N)
        self.x = linspace(0.-self.dx/2., self.L+self.dx/2., self.N+2)
        
    def D(self, x):
        return 2.
        
    def initialize(self):
        # Initialize y which holds initial disturbance
        self.TInit = np.sin(np.pi*self.x/float(self.L))
        
    def loadMatrices(self):
        self.A = np.zeros([self.N+2,self.N+2])
        self.B = np.zeros([self.N+2,self.N+2])
        
        self.A[0,0]=-1./self.dx
        self.A[0,1]=1./self.dx
        self.A[-1,-1]=-1./self.dx
        self.A[-1,-2]=1./self.dx
        '''
        self.B[0,0]=1./2.
        self.B[0,1]=1./2.
        self.B[-1,-1]=1./2.
        self.B[-1,-2]=1./2.
        '''
        
        for i in range(1,self.N+1):
            self.A[i,i-1] = -self.D(self.x[i]-self.dx/2.)
            self.A[i,i] = 2*self.dx**2 / self.tau + 4.#(self.D(self.x[i]+self.dx/2.) + self.D(self.x[i]-self.dx/2.))
            self.A[i,i+1] = -self.D(self.x[i]+self.dx/2.)
            self.B[i,i-1] = self.D(self.x[i]-self.dx/2.)
            self.B[i,i] = 2*self.dx**2 / self.tau - 4.#(self.D(self.x[i]+self.dx/2.) + self.D(self.x[i]-self.dx/2.))
            self.B[i,i+1] = self.D(self.x[i]+self.dx/2.)
        
        print(self.A)
        '''
        ud = np.insert(np.diag(self.A,1),0,0)
        d = np.diag(self.A)
        ld = np.insert(np.diag(self.A,-1),-1,0)
        self.ab = np.matrix([ud,d,ld])
        '''
        
    def animate(self):
        from numpy import zeros_like,copy
        from matplotlib import pyplot as plt
        T=self.TInit
        
        # Initialize time and counter
        t=0
        counter=0
        
        #Loop over time
        while t < self.tMax:
            '''
            #Calculate TNew
            Ainv = inv(self.A)
            #Binv = inv(self.B)
            print(Ainv)
            bandedM = inv(np.dot(Ainv,self.B))
            print(bandedM)
            TNew = solve_banded((1,1), bandedM, T)
            '''
            
            #TNew = solve_banded((1,1), self.ab, T)
            
            AinvB = np.dot(inv(self.A), self.B)
            #AinvB[0] = -AinvB[1]
            #AinvB[-1] = -AinvB[-2]
            TNew = np.dot(AinvB, T)
            
            #Enforce boundary conditions to set values for ghost points.
            #TNew = np.append(0,np.append(TNew,0))
            
            TExact = self.TInit*self.a*np.exp((-self.D(self.x) * np.pi**2/float(self.L**2))*t)
            
            if counter % 20 == 0:
                #Animate the wave periodically
                plt.clf()
                plt.plot(self.x, TNew)
                plt.plot(self.x, self.TInit)#TExact)
                plt.xlim(0,L)
                plt.ylim(-0.1,1.2)
                plt.draw()
                plt.pause(0.2)
                
            
            # Let yOld be equal to y
            T = TNew
            
            t += self.tau
            counter += 1
            
        error = np.mean(abs(TExact - T))
        print("Error: " + str(error))

# Get initial components
L=3.
N=40
tau=0.004
tmax = 0.99

# Calculate h
h = (L)/float(N)

# Find C
C = tau/float(h**2)
#print(C)
# C is about 0.5


# Initialize the wave
wave = animatedWave(L,N,tau,tmax)
wave.initialize()
wave.loadMatrices()
# Animate the wave over time
wave.animate()

# part d: the derivative boundary conditions means that the system is insulated