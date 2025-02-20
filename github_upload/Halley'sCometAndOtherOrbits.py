# Logan Richan
# ph385 proj
# Shows orbits and shows that area/time is constant (using leapfrog method)

from numpy import array, copy, sqrt
from numpy.linalg import norm
from matplotlib import pyplot

class orbit:
    mSun = 1.99e30
    G = 6.67e-11
    
    # Initialize
    def __init__(self, tMax = 1, dt = 0.01):
        self.dt = float(dt)
        self.tMax = tMax
    
    # Set initial conditions
    def setInitialConditions(self,r,v):
        self.r = [r]
        self.v = [v]
    
    # Get derivatives function
    def getDerivs(self, varsVec):
        # varsVec: first 2 pos; last 2 velocities in vV
        
        # Get derivatives of x and y
        xDeriv = varsVec[2]
        yDeriv = varsVec[3]
        
        # Get derivatives of velocity components
        r = array(varsVec[:2]) # Use position vector
        vxDeriv = -self.G * self.mSun * varsVec[0]/norm(r)**3
        vyDeriv = -self.G * self.mSun * varsVec[1]/norm(r)**3
        
        # Return derivatives of varsVec
        return array([xDeriv,yDeriv,vxDeriv,vyDeriv])
    
    # Find the Area swept out from a planet between 2 points on its path
    def Area(self, rOldVec, rVec):
        # Get the vector difference of r and rOld
        drVec = rVec - rOldVec
        
        # Find the magnitude of these vectors to find the height and base of a triangle, where dr is the base
        dr = norm(drVec)
        rOld = norm(rOldVec)
        r = norm(rVec)
        
        # Find the height of the triangle
        h = sqrt(rOld**2 - (-(r**2 - rOld**2 - dr**2)/float(2.*dr))**2)
        
        # Return the area of the triangle, which is the area swept out from rOld to r
        return 0.5*h*dr
    
    # Leapfrog method
    def leapfrog(self):
        # Initial part of leapfrog
        r = array([self.r[0][0],self.r[0][1],self.v[0][0],self.v[0][1] ])
        k1 = self.dt * self.getDerivs(r)
        midPointVars = r + 0.5*k1
        
        # Define lists for t and dAdT values
        self.t = [0]
        self.dAdT = []
        
        # Loop for each dt from t=0 to t=tMax
        while self.t[-1] < self.tMax:
            # Repeating part of the leapfrog method
            rOld = copy(r)
            k2 = self.dt * self.getDerivs(midPointVars)
            r += k2
            midPointVars += self.dt * self.getDerivs(r)
            
            # Append values to lists
            self.r.append([ r[0], r[1] ])
            self.v.append([ r[2], r[3] ])
            
            self.t.append(self.t[-1] + self.dt)
            self.dAdT.append(self.Area(rOld,r)/self.dt) # in m^2 / s
    
    # Plot the orbits and dA/dt
    def plotAll(self,label):
        self.plot(label)
        self.plotdAdT(label)
    
    # Plot the orbit
    def plot(self,label):
        pyplot.figure(1)
        x = [ var[0] for var in self.r ]
        y = [ var[1] for var in self.r ]
        pyplot.plot(x,y,label=label)
        pyplot.axis('scaled')
        pyplot.xlabel("x position in m")
        pyplot.ylabel("y position in m")
        pyplot.legend()
    
    # Plot the area swept out by a planet in a time interval in meters^2 per second through time
    def plotdAdT(self,label):
        pyplot.figure(2)
        pyplot.plot(array(self.t[1:])/spy,self.dAdT,label=label)
        pyplot.ylim(0,6.0e15)
        pyplot.xlabel("time in years")
        pyplot.ylabel("dA/dt in m^2/s")
        pyplot.legend()

# seconds per year
spy = 31556952.

# Earth:
rE=array([1.47e11,0])
vE=array([0,30280])

EarthOrbit = orbit(tMax = 80*spy, dt=80*spy/10000.) # 9.1e7, 1e4
EarthOrbit.setInitialConditions(rE,vE)#*0.5)
EarthOrbit.leapfrog()
EarthOrbit.plotAll("Earth")

# Jupiter:
rJ=array([7.4052e11,0])
vJ=array([0,13720])

JupiterOrbit = orbit(tMax = 80*spy, dt=80*spy/10000.)
JupiterOrbit.setInitialConditions(rJ,vJ)
JupiterOrbit.leapfrog()
JupiterOrbit.plotAll("Jupiter")

# Mars:
rM=array([206.62e9,0])
vM=array([0,26500])

MarsOrbit = orbit(tMax = 80*spy, dt=80*spy/10000.)
MarsOrbit.setInitialConditions(rM,vM)
MarsOrbit.leapfrog()
MarsOrbit.plotAll("Mars")

# Halley's Comet :
rH=array([8.766e10,0])
vH=array([0,54580])

HalleyOrbit = orbit(tMax = 80*spy, dt=8*spy/10000.)
HalleyOrbit.setInitialConditions(rH,vH)
HalleyOrbit.leapfrog()
HalleyOrbit.plotAll("Halley's Comet")


# Show all plots
pyplot.show()
