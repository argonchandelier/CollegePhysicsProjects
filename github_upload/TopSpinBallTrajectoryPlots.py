# Logan Richan
# ph385

from matplotlib import pyplot as plt
from numpy import array, pi, sin, cos, cross
from numpy.linalg import norm


class trajectory:
    # Initialize values
    g=9.8
    def __init__(self, r = [0,1,0], v = 40.2, th = 0, omega = array([30,0,0]), dt = 0.01, S0 = 6.11e-5, p = 1.29):
        # Original postion and velocity
        self.r = array(r)
        self.v = v
        
        self.th = th*pi/180. # theta in radians
        self.omega = omega*2*pi # angular velocity in radians/second
        
        # Start list of position and velocity vectors
        self.x = [r[0]]
        self.y = [r[1]]
        self.z = [r[2]]
        self.vx = [v*cos(self.th)]
        self.vy = [v*sin(self.th)]
        self.vz = [0]
        
        self.dt = dt # Time step
        self.S0 = S0 # Magnus Force coefficient
        self.m = 0.145 # in kg
        diam = 0.074 # diameter of the baseball in m
        self.A = pi * diam**2 / 4. # Area of the baseball
        self.C = 0.5 # Drag coefficient
        self.p = p # Air density
        
        self.range = 18.39 # Distance from mound to plate in meters
    
    # Calculate acceleration due to drag
    def Drag(self, v, vD):
        return -0.5*self.p*self.A*self.C*v*vD
    
    # Calculate the acceleration due to the Magnus Force
    def MagnusA(self, v):
        return self.S0 * cross(self.omega, v) / self.m
        
    def f(self, Vars):
        # Derivatives of the positions
        xD = Vars[3]
        yD = Vars[4]
        zD = Vars[5]
        
        v = norm(Vars[3:]) # velocity magnitude
        
        # Derivatives of the velocities
        vD = array([self.Drag(v, Vars[3]), self.Drag(v, Vars[4]) - self.g, self.Drag(v, Vars[5])]) # Accelertion due to drag and gravity
        vD += self.MagnusA(Vars[3:]) # Acceleration due to the Magnus force
        
        return array([xD, yD, zD, vD[0], vD[1], vD[2]]) # Return all derivatives in place of their original values
    
    # Calculate the trajectory using the Second-order Runge-Kutta method
    def RK2(self):
        # Set array of all values to step through
        r = array([self.x[0], self.y[0], self.z[0], self.vx[0], self.vy[0], self.vz[0]])
        while r[0] < self.range and r[1] > 0:
            # Get k1 and k2
            k1 = self.dt * self.f(r)
            k2 = self.dt * self.f(r + k1/2.)
            
            r += k2
            
            # Append x, y, and z values
            self.x.append(r[0])
            self.y.append(r[1])
            self.z.append(r[2])
    
    # Plot given axes
    def Plot(self, plotAxes):
        # Make list of possible axes and their names to be used
        axes = [self.x, self.y, self.z]
        axesNames = ["x axis", "y axis", "z axis"]
        
        # Plot 2 axes relative to each other
        plt.plot(axes[plotAxes[0]], axes[plotAxes[1]])
        
        # Label and show graph
        plt.xlabel(axesNames[plotAxes[0]])
        plt.ylabel(axesNames[plotAxes[1]])
        #plt.show()

omega = 30. # intitial angular velocity in revolutions per second

# Plot the x vs. z for a ball with side spin
plt.figure(1)
sideSpinBall = trajectory()
sideSpinBall.RK2()
sideSpinBall.Plot([0,2])

# Plot the x vs. y for a ball with top spin
plt.figure(2)
topSpinBall = trajectory(omega = array([0.,omega,0.]))
topSpinBall.RK2()
topSpinBall.Plot([0,1])

plt.show()
