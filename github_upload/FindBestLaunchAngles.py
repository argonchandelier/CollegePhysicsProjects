##############
# PH385 Test 1
# Problem # 2
# Logan Richan
################

from matplotlib import pyplot as plt
from numpy.linalg import norm
from numpy import array, cos, sin, pi

class trajectory():
    # Initialize given constants
    g = 9.8 # m/s^2
    def __init__(self, T0=320, m=50, alpha=2.5, C=0.5, p0=1.29, A=0.007, a = 6.5e-3, targetPos = [10000.,1000.], vehicleXSpeed = -30., dt = 0.02):
        self.T0 = float(T0) # sea level temperature in K
        self.m = m # mass in kg
        self.alpha = alpha
        self.C = C # 0.5
        self.p0 = p0 # air density in kg/m^3
        self.A = A # area in m^2
        self.a = a # in K/m
        self.targetPos = targetPos # Position of the target
        self.vehicleXSpeed = vehicleXSpeed # initial horizontal speed of the vehicle (assuming vehicle is not traveling on an incline)
        
        self.dt = dt # time step in seconds
    
    # Initialize position and velocity
    def Initialize(self, v, r=[0,0]):
        self.r = r
        self.v = v
    
    # Reset position and velocity arrays over time to be back at just t=0
    def reset(self, th):
        self.x = [self.r[0]]
        self.y = [self.r[1]]
        # Turn velocity into its components
        self.vx = [self.v*cos(th) + self.vehicleXSpeed]
        self.vy = [self.v*sin(th)]
    
    # Density as a function of height, y in m
    def density(self, y):
        return self.p0 * (1. - self.a*y/self.T0)**self.alpha
    
    # Acceleration due to drag at a specific speed and height
    def DragA(self, v, vn, y):
        return -0.5*self.density(y)*self.A*self.C*v*vn / self.m
    
    # Get the derivatives of the variables
    def f(self, Vars):
        # Position derivatives are just the velocities
        xDeriv = Vars[2]
        yDeriv = Vars[3]
        
        v = norm(Vars[2:])
        
        # Take the velocity derivatives by considering the forces
        vxDeriv = self.DragA(v,Vars[2],Vars[1])
        vyDeriv = -self.g + self.DragA(v,Vars[3],Vars[1])
        
        # Return derivatives
        return array([xDeriv, yDeriv, vxDeriv, vyDeriv])
    
    def RK4(self, th):
        th *= pi/180. # convert theta into radians
        self.reset(th) # Reset position and initial velocity with a certain angle
        
        # Initialize start position, velocity, and time
        values = [self.x[0], self.y[0], self.vx[0], self.vy[0]]
        self.t=[0]
        while values[1] >= 0 and values[0] <= self.targetPos[0]:
            # Use 4th order Runge-Kutta method
            k1 = self.dt * self.f(values)
            k2 = self.dt * self.f(values + 0.5*k1)
            k3 = self.dt * self.f(values + 0.5*k2)
            k4 = self.dt * self.f(values + k3)
            
            values += (1./6.) * (k1 + 2*k2 + 2*k3 + k4)
            
            # Add to list
            self.x.append(values[0])
            self.y.append(values[1])
            self.t.append(self.t[-1]+self.dt)
    
    # Plot trajectory
    def Plot(self):
        plt.plot(self.x, self.y,'.')

    # Determine the launch angle so that the shell strikes within 10m of the target
    def determineAngleFrom0(self, within):
        # initialize variables
        theta = 10
        counter = 10.
        self.RK4(theta-counter) # Get y values
        
        # While not within range (in y values)
        while self.y[-1] > self.targetPos[1] + within or self.y[-1] < self.targetPos[1] - within:
            # After loop, go back to previous theta that was under, and start counting in smaller increments now, until over
            theta -= counter
            counter /= 10.
            self.RK4(theta)
            
            # While under range
            while self.y[-1] < self.targetPos[1] - within:
                theta += counter
                self.RK4(theta)  # Check y value after 10km for each theta
        
        return [theta, self.y[-1]] # Return the desired theta, along with the y value it is actually at 10km away
    
    def determineAngleFrom90(self, within):
        # initialize variables
        theta = 80
        counter = 10.
        self.RK4(theta+counter) # Get y values
        
        # While not within range (in y values)
        while self.y[-1] > self.targetPos[1] + within or self.y[-1] < self.targetPos[1] - within:
            # After loop, go back to previous theta that was under, and start counting in smaller increments now, until over
            theta += counter
            counter /= 10.
            self.RK4(theta)
            
            # While under range
            while self.y[-1] < self.targetPos[1] - within:
                theta -= counter
                self.RK4(theta)  # Check y value after 10km for each theta
        
        return [theta, self.y[-1]] # Return the desired theta, along with the y value it is actually at 10km away

# Initialize cannon values and perform a 4th order Runge-Kutta method
cannon = trajectory()
cannon.Initialize(700.)
cannon.RK4(25.)

# Get the angles within the desired range in m
Angle1 = cannon.determineAngleFrom0(10)
Angle2 = cannon.determineAngleFrom90(10)
print(Angle1)
print(Angle2)

print("The cannon can be shot at with an angle of ", Angle1[0], " or ", Angle2[0], " degrees to be within 10 m of the target")


###########
cannon.RK4(Angle1[0])
cannon.Plot()
cannon.RK4(Angle2[0])
cannon.Plot()

plt.show()
