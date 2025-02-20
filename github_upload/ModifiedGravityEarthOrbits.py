# Logan Richan
# ph385

from numpy import array, pi
from numpy.linalg import norm
from matplotlib import pyplot

class orbit:
    mEarth = 5.98e24
    mSun = 1.99e30
    G = 6.67e-11
    GM = 4 * pi**2
    
    # Initialize
    def __init__(self, tMax = 1, dt = 0.01):
        self.dt = dt
        self.tMax = tMax
    
    # Set initial conditions
    def setInitialConditions(self,r,v):
        self.r = [r]
        self.v = [v]
    
    # Get derivatives function
    def getDerivs(self, varsVec, n):
        # first 2 pos; last 2 velocities in vV
        if n==1: # Normal law of gravity
            xDeriv = varsVec[2]
            yDeriv = varsVec[3]
            
            r = array(varsVec[:2])
            vxDeriv = -self.G * self.mSun * varsVec[0]/norm(r)**3
            vyDeriv = -self.G * self.mSun * varsVec[1]/norm(r)**3
            

            a = array([xDeriv,yDeriv,vxDeriv,vyDeriv])
            return a
        elif n==2: # Part e: modified gravity law
            xDeriv = varsVec[2]
            yDeriv = varsVec[3]
            
            r = array(varsVec[:2])
            vxDeriv = -self.G * self.mSun * varsVec[0]/norm(r)**(3.5)
            vyDeriv = -self.G * self.mSun * varsVec[1]/norm(r)**(3.5)
            
            return array([xDeriv,yDeriv,vxDeriv,vyDeriv])
        elif n==3: # part f: Inverse cube law
            xDeriv = varsVec[2]
            yDeriv = varsVec[3]
            
            r = array(varsVec[:2])
            vxDeriv = -self.G * self.mSun * varsVec[0]/norm(r)**(4)
            vyDeriv = -self.G * self.mSun * varsVec[1]/norm(r)**(4)
            
            return array([xDeriv,yDeriv,vxDeriv,vyDeriv])
        else:
            return 0
    
    # Potential energy formula
    def PE(self,r):
        return -4*pi**2 /norm(r)
    
    # Kinetic energy formula
    def KE(self,v):
        return 0.5 * self.mEarth * norm(v)**2
    
    # leapfrog method
    def leapfrog(self,n):
        r = array([self.r[0][0],self.r[0][1],self.v[0][0],self.v[0][1] ])
        k1 = self.dt * self.getDerivs(r,n)
        midPointVars = r + 0.5*k1
        
        self.t = [0]
        Un=self.PE(self.r[0])
        Kn=self.KE(self.v[0])
        U = [Un]
        K = [Kn]
        self.T = [Un+Kn]
        while self.t[-1] < self.tMax:
            k2 = self.dt * self.getDerivs(midPointVars,n)
            r += k2
            midPointVars += self.dt * self.getDerivs(r,n)
            self.r.append([ r[0], r[1] ])
            self.v.append([ r[2], r[3] ])
            self.t.append(self.t[-1] + self.dt)
            Un=self.PE(r[-1])
            Kn=self.KE(v[-1])
            U.append(Un)
            K.append(Kn)
            self.T.append(Un+Kn)
    
    # Plot the orbit
    def plot(self):
        x = [ var[0] for var in self.r ]
        y = [ var[1] for var in self.r ]
        pyplot.plot(x,y)
        pyplot.show()
    
    # Plot the total energy
    def plotTE(self):
        pyplot.plot(self.t,self.T)
        pyplot.show()

r=[1.47e11,0]
v=[0,30280]

# part a-c
pyplot.figure(1)
myOrbit = orbit(tMax = 9.1e7, dt=1e4) # 3.1e7
myOrbit.setInitialConditions(r,v)
myOrbit.leapfrog(1)
myOrbit.plot()

# part d
pyplot.figure(2)
pyplot.title("Total Energy vs. Time")
myOrbit.plotTE()

# part e
pyplot.figure(3)
myOrbit2 = orbit(tMax = 5.1e8, dt=1e5)
myOrbit2.setInitialConditions([4e10,0],[0,10.3])
myOrbit2.leapfrog(2)
myOrbit2.plot()

# part f
pyplot.figure(4)
myOrbit2 = orbit(tMax = 5.1e8, dt=1e5)
myOrbit2.setInitialConditions([4e9,0],[0,1.03])
myOrbit2.leapfrog(3)
myOrbit2.plot()
