# Logan Richan
# ph385

from numpy import array, pi

class orbit:
    mEarth = 5.98e24
    def __init__(self, tMax = 1, dt = 0.01):
        self.dt = dt
        self.tMax = tMax
    
    def setInitialConditions(self,r,v):
        self.r = [r]
        self.v = [v]
    
    def getDerivs(self, varsVec):
        # first 2 pos; last 2 velocities in vV
        from numpy.linalg import norm
        
        xDeriv = varsVec[2]
        yDeriv = varsVec[3]
        
        r = array(varsVec[:2])
        vxDeriv = -4 * pi**2 * varsVec[0]/norm(r)**3
        vyDeriv = -4 * pi**2 * varsVec[1]/norm(r)**3
        
        return array([xDeriv,yDeriv,vxDeriv,vyDeriv])
    
    def leapfrog(self):
        r = array([self.r[0][0],self.r[0][1],self.v[0][0],self.v[0][1] ])
        k1 = self.dt * self.getDerivs(r)
        midPointVars = r + 0.5*k1
        
        self.t = [0]
        while self.t[-1] < self.tMax:
            k2 = self.dt * self.getDerivs(midPointVars)
            r += k2
            midPointVars += self.dt * self.getDerivs(r)
            self.r.append([ r[0], r[1] ])
            self.v.append([ r[2], r[3] ])
            self.t.append(self.t[-1] + self.dt)
    
    def plot(self):
        from matplotlib import pyplot
        x = [ var[0] for var in self.r ]
        y = [ var[1] for var in self.r ]
        pyplot.plot(x,y)
        pyplot.show()

r=[1,0]
v=[0,2*pi]

myOrbit = orbit(dt=0.001)
myOrbit.setInitialConditions(r,v)
myOrbit.leapfrog()
myOrbit.plot()
