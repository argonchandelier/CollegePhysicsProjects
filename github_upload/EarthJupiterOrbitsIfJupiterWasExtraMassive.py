# Logan Richan
# ph385

from numpy import array, pi
from numpy.linalg import norm
from matplotlib import pyplot

class orbit:
    # Initial, unchanging values
    mEarth = 5.98e24
    mJup = 1.90e27 * 1000 # ...except this one for testing and comparison purposes in a what-if scenario
    mSun = 1.99e30
    G = 6.67e-11
    GM = 4 * pi**2
    
    # Initialize
    def __init__(self, tMax = 1, dt = 0.01):
        self.dt = dt
        self.tMax = tMax
    
    # Set initial conditions
    def setInitialConditions(self,r,v,r2,v2):
        # Earth positions and velocities over time
        self.r = [r]
        self.v = [v]
        
        # Jupiter positions and velocities over time
        self.r2 = [r2]
        self.v2 = [v2]
    
    # Get derivatives function
    def getDerivs(self, varsVec):
        # Get the x and y derivatives of the Earth and Jupiter respectively
        xDeriv1 = varsVec[2]
        yDeriv1 = varsVec[3]
        xDeriv2 = varsVec[6]
        yDeriv2 = varsVec[7]
        
        # Get an array of the positions of Earth and Jupiter
        r1 = array(varsVec[:2])
        r2 = array(varsVec[4:6])
        
        # Use the gravity equation to get velocity derivatives of Earth and Jupiter, considering forces from the sun and the other planet
        vxDeriv1 = -self.G * self.mSun * varsVec[0]/norm(r1)**3 - self.G * self.mJup * varsVec[0]/norm(r1-r2)**3
        vyDeriv1 = -self.G * self.mSun * varsVec[1]/norm(r1)**3 - self.G * self.mJup * varsVec[1]/norm(r1-r2)**3
        vxDeriv2 = -self.G * self.mSun * varsVec[4]/norm(r2)**3 - self.G * self.mEarth * varsVec[4]/norm(r2-r1)**3
        vyDeriv2 = -self.G * self.mSun * varsVec[5]/norm(r2)**3 - self.G * self.mEarth * varsVec[5]/norm(r2-r1)**3
        
        # Return the derivatives
        return array([xDeriv1,yDeriv1,vxDeriv1,vyDeriv1,xDeriv2,yDeriv2,vxDeriv2,vyDeriv2])
    
    # Potential energy formula
    def PE(self,r):
        return -4*pi**2 /norm(r)
    
    # Kinetic energy formula
    def KE(self,v):
        return 0.5 * self.mEarth * norm(v)**2
    
    # leapfrog method
    def leapfrog(self):
        # Make an array of the initial values
        r = array([self.r[0][0],self.r[0][1],self.v[0][0],self.v[0][1],self.r2[0][0],self.r2[0][1],self.v2[0][0],self.v2[0][1]])
        # Get the k1 value
        k1 = self.dt * self.getDerivs(r)
        midPointVars = r + 0.5*k1
        
        # Get initial time and energy values
        self.t = [0]
        Un=self.PE(self.r[0]) # Potential energy
        Kn=self.KE(self.v[0]) # Kinetic energy
        U = [Un]
        K = [Kn]
        self.T = [Un+Kn] # Total energy
        
        # Step through time
        while self.t[-1] < self.tMax:
            # Get k2 and add to the values
            k2 = self.dt * self.getDerivs(midPointVars)
            r += k2
            midPointVars += self.dt * self.getDerivs(r)
            
            # append position and velocity values of Earth and Jupiter, as well as time
            self.r.append([ r[0], r[1] ])
            self.v.append([ r[2], r[3] ])
            self.r2.append([ r[4], r[5] ])
            self.v2.append([ r[6], r[7] ])
            self.t.append(self.t[-1] + self.dt)
            
            # Obtain and append energy values
            Un=self.PE(r[-1])
            Kn=self.KE(v[-1])
            U.append(Un)
            K.append(Kn)
            self.T.append(Un+Kn)
    
    # Plot the orbit
    def plot(self):
        # Extract and plot x and y values for Earth and Jupiter
        x = [ var[0] for var in self.r ]
        y = [ var[1] for var in self.r ]
        pyplot.plot(x,y) # Earth orbit plot
        x2 = [ var[0] for var in self.r2 ]
        y2 = [ var[1] for var in self.r2 ]
        pyplot.plot(x2,y2) # Jupiter orbit plot
        
        # Show the plots
        pyplot.show()
    
    # Plot the total energy
    def plotTE(self):
        # Plot and show total energy over time
        pyplot.plot(self.t,self.T)
        pyplot.show()

# Initial position and velocity of Earth
r=[1.47e11,0]
v=[0,30280]

# Initial position and velocity of Jupiter
r2=[1e11*5.2,0]
v2=[0,13720]

# Use leapfrog method and plot the orbits of Earth and Jupiter simultaneously
myOrbit = orbit(tMax = 3.154e7*12, dt = 1e4)
myOrbit.setInitialConditions(r,v,r2,v2)
myOrbit.leapfrog()
myOrbit.plot()