# Logan Richan
# ph385

from numpy import sin, pi

class pendulum:
    #Initialize data
    def __init__(self, l, theta, omega, tMax=30, dt=0.1, g=9.8):
        self.g = g
        self.l = l
        self.theta = [theta]
        self.omega = [omega]
        self.dt = dt
        self.tMax = tMax
    
    # Use the 2nd order Runge-Kutta method to step through theta over time
    def RK2(self):
        from numpy import arange
        
        self.time = arange(0,self.tMax,self.dt)
        
        for t in self.time: # Use the 2nd order Runge-Kutta Method
            thetaHalf = self.theta[-1] + self.dt/2 * self.omega[-1]
            omegaHalf = self.omega[-1] - self.dt/2 * self.g/self.l * sin(self.theta[-1])
            self.theta.append(self.theta[-1] + self.dt * omegaHalf)
            self.omega.append(self.omega[-1] - self.dt * self.g/self.l * sin(thetaHalf))
    
    # Plot theta over time
    def Plot(self):
        from matplotlib import pyplot as plt
        
        plt.plot(self.time, self.theta[:-1])
        plt.show()
    
l = 1
theta = pi/4
omega = 0
Pend = pendulum(l,theta,omega)
Pend.RK2()
Pend.Plot()

# The 2nd Order Runge-Kutta Method does not conserve energy
# as the plot clearly shows increasing energy over time