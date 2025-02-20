##############
# PH385 Test # 3
# Problem # 2
# Logan Richan
################

import numpy as np
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

plt.close('all') # close all existing plots

class membrane():
    # Set initial values
    def __init__(self,a,b,c,d,Nx,Ny,sig,tau,tmax):
        # x boundaries
        self.a = a
        self.b = b
        # y boundaries
        self.c = c
        self.d = d
        
        # number of points in x and y
        self.Nx = Nx
        self.Ny = Ny
        
        # Surface tension
        self.sig = sig
        
        # time step and max
        self.tau = tau
        self.tmax = tmax
        
        # Get values for X and Y
        self.x,self.dx = np.linspace(a,b,Nx,retstep=True)
        self.y,self.dy = np.linspace(c,d,Ny,retstep=True)
        self.X,self.Y=np.meshgrid(self.x,self.y)
        
        # Find the surface mass density
        self.mu = 1. + 2. * (np.sin((self.X-5.)/4.))**2 * (np.sin(self.Y/10.))**2
        
    # initialize the membrane plane and velocity
    def initialize(self):
        # Start with a Gaussian
        self.Zinit = np.exp(-5*(self.X**2 + self.Y**2))
        # Set boundary conditions at 0 for all edges
        self.Zinit[0,:] = 0
        self.Zinit[-1,:] = 0
        self.Zinit[:,0] = 0
        self.Zinit[:,-1] = 0
        
        # No initial velocity
        self.Vinit = self.X*0
    
    # Animate the membrane
    def animate(self):
        fig = plt.figure() # Set the figure for plotting
        
        # Get initial z and zold
        z = self.Zinit
        zold = z[1:-1,1:-1] - self.Vinit[1:-1,1:-1]*self.tau + self.sig*self.tau**2/(2.*self.mu[1:-1,1:-1]) *\
               ((z[2:,1:-1]+z[:-2,1:-1])/self.dx**2 + (z[1:-1,2:]+z[1:-1,:-2])/self.dy**2 +\
                -2*z[1:-1,1:-1]*(self.dx**(-2) + self.dy**(-2)))
        # set boundary conditions at 0
        zold = np.append(np.zeros((1,len(self.x)-2)),np.append(zold,np.zeros((1,len(self.x)-2)),axis=0),axis=0)
        zold = np.append(np.zeros((len(self.y),1)),np.append(zold,np.zeros((len(self.y),1)),axis=1),axis=1)
        
        # Initialize time and counter
        t=0
        counter=0
        
        # Loop through time steps
        while t<=self.tmax:
            # Get znew
            znew = 2*z[1:-1,1:-1] - zold[1:-1,1:-1] + self.sig*self.tau**2/(self.mu[1:-1,1:-1]) *\
            ((z[2:,1:-1]+z[:-2,1:-1])/self.dx**2 + (z[1:-1,2:]+z[1:-1,:-2])/self.dy**2 +\
             -2*z[1:-1,1:-1]*(self.dx**(-2) + self.dy**(-2)))
            # Keep boundaries at 0
            znew = np.append(np.zeros((1,len(self.x)-2)),np.append(znew,np.zeros((1,len(self.x)-2)),axis=0),axis=0)
            znew = np.append(np.zeros((len(self.y),1)),np.append(znew,np.zeros((len(self.y),1)),axis=1),axis=1)
            
            # Plot every 100 iterations
            if counter % 100 == 0:
                plt.clf() # Clear previous plot
                ax=fig.gca(projection='3d') # Make a 3d plot
                # Set labels and limits
                plt.xlabel("x")
                plt.ylabel("y")
                plt.xlim(c,d)
                
                # Plot
                ax.plot_surface(self.X,self.Y,znew)
                plt.draw()
                plt.pause(0.0001)
            
            # Make everything older for the new time step
            zold = np.copy(z)
            z = np.copy(znew)
            
            # Increment values
            t+=self.tau
            counter+=1
                   
# Given initial conditions
a=-5.
b=5.
c=-10.
d=10.
Nx=20
Ny=40
sig=2.
tau=0.005
tmax=15.

# Initialize and animate the membrane
mem = membrane(a,b,c,d,Nx,Ny,sig,tau,tmax)
mem.initialize()
mem.animate()

# part b: These wave make sense because they propogate symmetrically and get reflected from the edges