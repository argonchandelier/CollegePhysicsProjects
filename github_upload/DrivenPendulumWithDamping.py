# Logan Richan
# ph385
import matplotlib.pyplot as plt
from numpy import array, sin, arange
from matplotlib import pyplot as p


class chaosPendulum:
    g=9.8
    # Initialize variables
    def __init__(self, tMax=60.,dt=0.01,q=1/2.,Fd=1.2,omegaD=2/3.,l=9.8):
        self.dt = dt
        self.tMax = tMax
        self.l = l
        self.q = q
        self.Fd = Fd
        self.omegaD = omegaD
    
    # set initial conditions
    def setInitialConditions(self,theta,omega):
        self.theta = [theta]
        self.omega = [omega]
    
    # take the derivatives
    def f(self, varsVec, t):
        thetaDeriv = varsVec[1]
        omegaDeriv = -self.g/self.l*sin(varsVec[0]) - self.q*varsVec[1] + self.Fd*sin(self.omegaD * t)
        
        return array([thetaDeriv, omegaDeriv])
    
    # implement 4th order Runge-Kutta method
    def RK4(self):
        r = array([self.theta[0], self.omega[0]])
        self.time = arange(0,self.tMax,self.dt)
        for t in self.time:
            k1 = self.dt * self.f(r, t)
            k2 = self.dt * self.f(r+k1/2., t+self.dt/2.)
            k3 = self.dt * self.f(r+k2/2., t+self.dt/2.)
            k4 = self.dt * self.f(r+k3, t+self.dt)
            
            r += (1./6.) * (k1 + 2*k2 + 2*k3 + k4)
            self.theta.append(r[0])
            self.omega.append(r[1])
            
    # Plot pendulum angle over time
    def plot(self):
        p.plot(self.time,self.theta[:-1])
        #p.show()

theta = 0.2
omega = 0

# a/b
pend = chaosPendulum(tMax = 60, Fd = 0.0, q = 0.5, dt = 0.04)
pend.setInitialConditions(theta,omega)
pend.RK4()
plt.title("Driving Force: 0N")
pend.plot()

# c
p.figure(2)
pend2 = chaosPendulum(tMax = 60, Fd = 0.5, q = 0.5, dt = 0.04)
pend2.setInitialConditions(theta,omega)
pend2.RK4()
plt.title("Driving Force: 0.5N")
pend2.plot()

newMax = 600 # f
newDt = 0.004 # g

# d
p.figure(3)
pend3 = chaosPendulum(tMax = newMax, Fd = 1.2, q = 0.5, dt = 0.04)
pend3.setInitialConditions(theta,omega)
pend3.RK4()
plt.title("Driving Force: 1.2N; Sensitivity to small change in initial angle")
pend3.plot()

# e/f/g
pend4 = chaosPendulum(tMax = newMax, Fd = 1.2, q = 0.5, dt = 0.04)
pend4.setInitialConditions(0.201,omega)
pend4.RK4()
pend4.plot()

p.show()
