# Logan Richan
# ph385

from matplotlib import pyplot as plt
import numpy as np
from mpl_toolkits.mplot3d import Axes3D

class wave3d:
    # Initialize N and grid space
    def __init__(self, a, b, c, d, Nx, Ny, dt, tMax):
        # Get the cell edge grid to plot g(x)
        self.x,self.dx = np.linspace(a,b,Nx,retstep=True)
        self.y,self.dy = np.linspace(c,d,Ny,retstep=True)
        
        # Get the meshgrid of X and Y
        self.X,self.Y=np.meshgrid(self.x,self.y)
        
        # Num points
        self.Nx=Nx
        self.Ny=Ny
        
        # given constants
        self.sigma = 2 # N/m
        self.mu = 0.3 # kg/m^2
        
        # Time values
        self.tau = dt
        self.tMax = tMax
        
        # lengths
        self.Lx = b-a
        self.Ly = d-c
    
    # Initialize the initial y positions and velocities of the wave  
    def initializeWave(self):        
        # Initialize y which holds initial disturbance
        self.zInit = self.X * 0 #np.exp(-5*(self.X**2 + self.Y**2))
        
        # Initialize v to hold initial velocity
        self.vInit = np.exp(-5*(self.X**2 + self.Y**2)) #self.X * 0
     
    # Animate the wave
    def animate(self):
        
        fig = plt.figure()
        
        # Define the constant and y from initial y
        const = self.sigma * self.tau**2 / float(self.mu*self.dx**2)
        z=self.zInit
        
        # Define variable to store wave at prev. time step
        zOld = z[1:-1,1:-1] - self.tau*self.vInit[1:-1,1:-1] + \
               const/2.*(z[2:,1:-1] + z[:-2,1:-1] + z[1:-1,2:] + z[1:-1,:-2] - 4*z[1:-1,1:-1])
            
        # Enforce boundary conditions to set values for ghost points in zOld
        zerosRow,zerosCol=np.zeros((1,self.Nx)),np.zeros((self.Ny-2,1))
        zOld = np.append(zerosCol,np.append(zOld,zerosCol,axis=1),axis=1)
        zOld = np.append(zerosRow,np.append(zOld,zerosRow,axis=0),axis=0)

        # Initialize variables
        t=0
        counter=0
        zCenters = []
        ts = []
        
        #Loop over time
        while t < self.tMax:
            #Calculate yNew
            zNew = 2*z[1:-1,1:-1] - zOld[1:-1,1:-1] + \
                   const*(z[2:,1:-1] + z[:-2,1:-1] + z[1:-1,2:] + z[1:-1,:-2] - 4*z[1:-1,1:-1])
            
            #Enforce boundary conditions to set values for ghost points.
            zNew = np.append(zerosCol,np.append(zNew,zerosCol,axis=1),axis=1)
            zNew = np.append(zerosRow,np.append(zNew,zerosRow,axis=0),axis=0)
            
            zCenters.append(zNew[self.Nx//2,self.Ny//2])
            ts.append(t)
            
            if counter % 50 == 0:
                #'''
                #Animate the wave periodically
                plt.clf() # Clear previous plot
                plt.plot(self.x, zNew) # Plot the x vs. y vs. z of the string points for every 20 time steps
                ax = fig.gca(projection='3d')
                ax.plot_surface(self.X,self.Y,z)
                plt.xlabel('x')
                plt.ylabel('y')
                plt.draw()
                plt.pause(0.00002)
                #'''
                
            
            # Let zOld be equal to z
            zOld = np.copy(z)
            
            # Let z be zNew
            z = np.copy(zNew)
            
            # Increment values
            t += self.tau
            counter += 1
            
            '''
            plt.figure(2)
            plt.plot(ts, zCenters)
            plt.show()
            '''

a=-5.
b=5.
c=-5.
d=5.
Nx=50
Ny=50
dt=0.005
tMax=5.

# f ~ 0.6 in the eCourant condition

wave = wave3d(a,b,c,d,Nx,Ny,dt,tMax)
wave.initializeWave()
# Animate the wave over time
wave.animate()

#part f: the initial pulse does not behave the same way in 2 dimensions, as the center eventually flattens