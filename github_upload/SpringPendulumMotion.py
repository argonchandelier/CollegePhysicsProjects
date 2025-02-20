# Logan Richan
# ph336

from matplotlib import pyplot as plt
from numpy import array, arange, sin, cos, pi


class pendulum:
    # Initialize values
    g = 9.8
    def __init__(self, L, T, R, phi0, phiPrime0, tMax, dt = 0.01):
        self.L = float(L) # Length in m
        self.omega = 2*pi/float(T) # constant angular velocity of the wheel in rads/s
        self.R = R # Radius of the wheel in m
        self.phi0 = phi0 # initial angle of the pendulum in rads
        self.phiPrime0 = phiPrime0 # initial anglular velocity of the pendulum in rads/s
        self.tMax = tMax # total time for the simulation in s
        self.dt = dt # time step in s
        
        self.phi = [phi0] # phi values to plot
        self.t = arange(0, tMax+dt, dt) # time values to plot
    
    
    def stepFunction(self):
        # Initialize phi and phi prime based on given starting values
        phi = self.phi0
        phiPrime = self.phiPrime0
        
        # Perform Euler's method to step through time to find phi over time
        for t in self.t:
            # Given equaation for phi double prime:
            phiPrime2 = -self.g/self.L*sin(phi) + self.omega**2*self.R/self.L*cos(phi - self.omega*t)
            
            phi += phiPrime*self.dt # Step through phi
            phiPrime += phiPrime2*self.dt # Step through phi prime
            self.phi.append(phi) # Append phi value to list of phis over time
            
    
    def Plot(self):
        plt.plot(self.t, array(self.phi)[:-1]) # Plot the values
        
        # Label graph and axes
        plt.xlabel("Time in seconds")
        plt.ylabel("Angle of the pendulum in radians")
        plt.title("Osciallations of the pendulum")
        
        plt.show() # Show the plot


pend = pendulum(0.45, 3, 0.15, pi/4., 0, 5.0) # Initialize the pendulum values
pend.stepFunction() # Find the angle over time of the pendulum
pend.Plot() # Plot the angle over time of the pendulum