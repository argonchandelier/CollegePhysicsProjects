# Logan Richan
# ph385

class trajectory():
    def __init__(self, g=9.8):
        self.g = g
    
    # Set the initial conditions of the projectile
    def setConditions(self,x0=None,y0=None,v0=None,th=None):
        from numpy import pi, cos, sin
        self.x0 = float(x0)
        self.y0 = float(abs(y0)) # abs() used as failsafe
        self.v0 = float(v0)
        self.th = th/180.*pi
        
        self.vx0 = self.v0 * cos(self.th)
        self.vy0 = self.v0 * sin(self.th)
    
    # Calculate x(t)
    def calcXLoc(self, t):
        return self.x0 + self.vx0*t
    
    # Calculate y(t)
    def calcYLoc(self, t):
        return self.y0 + self.vy0*t - 0.5*self.g*t**2
    
    # Calculate x(y=0, t>=0)
    def calcLandLoc(self):
        return self.x0 + self.vx0/self.g * (self.vy0 + ((self.vy0)**2 + 2*self.g*self.y0)**(0.5))
    
    # Plot the trajectory of the projectile until it hits the ground
    def plotTraj(self):
        from matplotlib import pyplot as plt
        from numpy import zeros, linspace
        
        tf = (self.calcLandLoc() - self.x0) / self.vx0 # Calculate the final time
        
        N = 500 # points plotted
        X = zeros(N, float) # initialize x values at 0
        Y = zeros(N, float) # initialize y values at 0
        T = linspace(0,tf,N) # Use times from the initial to final with N points

        for i in range(N): # Get points
            X[i] = self.calcXLoc(T[i])
            Y[i] = self.calcYLoc(T[i])
        
        plt.plot(X,Y) # Plot
        plt.show()



Traj1 = trajectory()

Traj1.setConditions(x0 = 5, y0 = 400, v0 = 10, th = 45)
xf = Traj1.calcLandLoc()
print(xf)
Traj1.plotTraj()