# Logan Richan
# ph385
# 3D Butterfly curve

from numpy import array, sin, arange, pi
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

# Lorenz's model of chaos:
class chaos:
    # Initialize class
    def __init__(self, tMax=60.,dt=0.01):    
        self.dt = dt
        self.tMax = tMax
    
    # Initialize variables and reset x, y, and z values
    def Initialize(self, sigma=10.,b=8./3.,r=10.,r0=[1.,0.,0.]): # Utilizing given values
        self.sigma = sigma
        self.b = b
        self.r = r
        self.r0 = r0
        self.Reset()
    
    # Reset x, y, and z lists back to just their first element
    def Reset(self):
        self.x = [self.r0[0]]
        self.y = [self.r0[1]]
        self.z = [self.r0[2]]
    
    # Take the derivatives with respect to time
    def f(self, varsVec):
        # Given derivatives for the Lorenz model
        xDeriv = self.sigma * (varsVec[1] - varsVec[0])
        yDeriv = -varsVec[0]*varsVec[2] + self.r*varsVec[0] - varsVec[1]
        zDeriv = varsVec[0]*varsVec[1] - self.b*varsVec[2]
        
        return array([xDeriv, yDeriv, zDeriv]) # Return the derivatives in the spots of the original values
    
    # Implement 4th order Runge-Kutta method
    def RK4(self):
        r = array([self.x[0], self.y[0], self.z[0]])
        self.time = arange(0,self.tMax,self.dt) # Creates a time array
        
        for t in self.time:
            # Utilize Runge-Kutta here
            k1 = self.dt * self.f(r)
            k2 = self.dt * self.f(r+k1/2.)
            k3 = self.dt * self.f(r+k2/2.)
            k4 = self.dt * self.f(r+k3)
            
            r += (1./6.) * (k1 + 2.*k2 + 2.*k3 + k4)
            
            # put the coordinate values into the started list
            self.x.append(r[0])
            self.y.append(r[1])
            self.z.append(r[2])
    
    # Plot t vs. z
    def PlotTZ(self):
        plt.plot(self.time, self.z[:-1])
        plt.show()
    
    # Plot z vs. x
    def PlotZX(self):
        plt.plot(self.z, self.x)
        plt.show()
    
    # Plot x vs. y vs. z in a 3D plot
    def Plot3D(self):
        fig = plt.figure() # automatically sets a new figure
        #fig.gca(projection='3d')
        #plt.plot(self.x,self.y,self.z)
        #plt.axis('equal')
        ax = fig.add_subplot(111, projection='3d')  # Define 3D axes
        ax.plot(self.x, self.y, self.z)  # Plot 3D trajectory
        ax.set_xlim(min(self.x), max(self.x))
        ax.set_ylim(min(self.y), max(self.y))
        ax.set_zlim(min(self.z), max(self.z))
        plt.show()

# Plot t vs. z of the Lorenz model with the given values
plt.figure(1)
model1 = chaos()
model1.Initialize(r=10)
model1.RK4()
model1.PlotTZ()

# Do the same but for r of 25
model1.Initialize(r=25)
model1.RK4()
model1.PlotTZ()

# Plot z vs. x now
plt.figure(2)
model1.PlotZX()

# And plot x vs. y vs. z
model1.Plot3D() # Note: 3d plot is automatically in new figure because of the function's code
