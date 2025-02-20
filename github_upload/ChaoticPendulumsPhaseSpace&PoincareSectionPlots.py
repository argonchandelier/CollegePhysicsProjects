# Logan Richan
# ph385

from numpy import array, sin, arange, pi
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
        self.theta2 = [theta]
        self.omega = [omega]
    
    # take the derivatives
    def f(self, varsVec, t):
        thetaDeriv = varsVec[1]
        omegaDeriv = -self.g/self.l*sin(varsVec[0]) - self.q*varsVec[1] + self.Fd*sin(self.omegaD * t)
        
        return array([thetaDeriv, omegaDeriv])
    
    # implement 4th order Runge-Kutta method
    def RK4(self, goBack=False):
        r = array([self.theta[0], self.omega[0]])
        self.time = arange(0,self.tMax,self.dt)
        for t in self.time:
            k1 = self.dt * self.f(r, t)
            k2 = self.dt * self.f(r+k1/2., t+self.dt/2.)
            k3 = self.dt * self.f(r+k2/2., t+self.dt/2.)
            k4 = self.dt * self.f(r+k3, t+self.dt)
            
            r += (1./6.) * (k1 + 2*k2 + 2*k3 + k4)
            
            # loop theta back
            if r[0] > pi:
                r[0] -= 2*pi
            if r[0] < -pi:
                r[0] += 2*pi
            self.theta.append(r[0])
            self.omega.append(r[1])
        
        return array(self.theta)
            
    # Plot pendulum angle over time
    def plot(self):
        p.plot(self.time,self.theta[:-1])
        #p.show()
    
    # Compare the theta of a pendulum and a similar one with a slightly higher initial theta
    def Compare(self, theta, omega):
        self.setInitialConditions(theta,omega)
        TH1 = self.RK4()
        self.setInitialConditions(theta+0.001,omega)
        TH2 = self.RK4()
        
        dTH = TH1 - TH2
        p.plot(self.time, dTH[:-1])
        p.yscale("log")
        #p.show()
    
    def PhaseSpacePlot(self):
        p.plot(self.theta, self.omega,'.')
        p.xlim(-pi,pi)
        #p.show()
    
    # Only plot phase space plots in phase with the driving frequency
    def PhaseSpacePlotLimited(self):
        i=0
        t=0.
        for k in self.theta:
            s = self.omegaD*t*200./(2.*pi)
            if int(s) % 200 == 0:
                p.plot(self.theta[i],self.omega[i],'.')
            t+=self.dt
            i+=1
        p.xlim(-pi,pi)
        #p.show()
        
        

theta = 0.2
omega = 0

p.figure(1)
pend = chaosPendulum(tMax = 60, Fd = 0.5, q = 0.5, dt = 0.04)
pend.setInitialConditions(theta,omega)
pend.RK4()
pend.PhaseSpacePlot()

p.figure(2)
pend2 = chaosPendulum(tMax = 300, Fd = 1.2, q = 0.5, dt = 3*pi/200.)
pend2.setInitialConditions(theta,omega)
pend2.RK4()
pend2.PhaseSpacePlot()

p.figure(3)
pend3 = chaosPendulum(tMax = 15000, Fd = 1.2, q = 0.5, dt = 3*pi/200.)
pend3.setInitialConditions(theta,omega)
pend3.RK4()
pend3.PhaseSpacePlotLimited()

p.show()
