##############
# PH385 Test 1
# Problem # 3
# Logan Richan
################

from numpy import pi, array, arange
from matplotlib import pyplot as plt
from numpy.linalg import norm


class orbit():
    # Initialize values
    alpha = 1.10e-8
    GM = 4*pi**2
    def __init__(self, r, v, dt=1e-5, tMax=0.24356):
        # Initialize position and velocities
        self.r = r # position vector in AU
        self.v = v # velocity vector in AU/year
        
        # Start lists
        self.x = [r[0]]
        self.y = [r[1]]
        self.vx = [v[0]]
        self.vy = [v[1]]
        
        # Initialize dt and time values
        self.dt = dt
        self.tValues = arange(0, tMax, dt)
    
    # Get the derivatives
    def f(self, r):
        # Position derivatives are velocities
        xDeriv = r[2]
        yDeriv = r[3]
        
        # find velocity by the acceleration due to the force of gravity
        vxDeriv = -self.GM*r[0]/norm(r[:2])**3 * (1+self.alpha/norm(r[:2])**2)
        vyDeriv = -self.GM*r[1]/norm(r[:2])**3 * (1+self.alpha/norm(r[:2])**2)
        
        return array([xDeriv, yDeriv, vxDeriv, vyDeriv]) # return the derivatives
    
    # Use the leapfrog method to conserve energy
    def leapfrog(self):
        r = [self.r[0],self.r[1],self.v[0],self.v[1]] # Put positions and velocities all together
        # Start k1 and values after half a time step
        k1 = self.dt * self.f(r)
        rHalf = r + 0.5*k1
        
        # Go through time
        for t in self.tValues:
            # Finish leapfrog method
            k2 = self.dt*self.f(rHalf)
            r += k2
            rHalf += self.dt*self.f(r)
            
            # Append positon and velocity values
            self.x.append(r[0])
            self.y.append(r[1])
            self.vx.append(r[2])
            self.vy.append(r[3])
    
    # Plot orbit of Mercury to see if it looks correct
    def plot(self):
        plt.plot(self.x, self.y)
        plt.show()
    
    # Find the smallest and largest distance from the sun and the velocities at those points
    def DistancesAndVelocities(self):
        distances = (array(self.x)**2 + array(self.y)**2)**(0.5) # Get all distances from the sun at each calculated point
        #Initialize index values for the largest and smallest point
        smallestIndex = 0
        largestIndex = 0
        
        # Loop through all distance values to see which is the largest and which is the smallest (by recording the index number)
        for i in range(len(distances)):
            if distances[i] > distances[largestIndex]:
                largestIndex = i
            if distances[i] < distances[smallestIndex]:
                smallestIndex = i
        
        # Keep largest and smallest distance values and indexes within the class (to help calculate the period)
        self.apoapsis = distances[largestIndex]
        self.periapsis = distances[smallestIndex]
        self.smallestIndex = smallestIndex
        self.largestIndex = largestIndex
        
        # Return smallest distance, largest distance, and each of their velocities at those points
        return array([distances[smallestIndex], distances[largestIndex], norm([self.vx[smallestIndex], self.vy[smallestIndex]]), norm([self.vx[largestIndex], self.vy[largestIndex]])])
    
    # Find the eccentricity of the orbit
    def eccentricity(self):
        return (self.apoapsis + self.periapsis) / (self.apoapsis - self.periapsis)
    
    # Find the period of the orbit
    def period(self):
        return 2.*abs(self.tValues[self.largestIndex] - self.tValues[self.smallestIndex])

# Initial position and velocity values
r = [0.47034,0.]
v = [0.,8.16365]

mercury = orbit(r, v) # Initialize orbit for Mercury
mercury.leapfrog() # perform the leapfrog method
mercury.plot() # plot the orbit
Vars = mercury.DistancesAndVelocities() # Get the smallest and largest distance values of Mercury from the sun, as well as the velocities at those points
e = mercury.eccentricity() # Find the eccentricity
period = mercury.period() # Find the period

print("Closest Mercury gets to the Sun: ", Vars[0], " in AU")
print("Speed at closest distance: ", Vars[2], "in AU/year")
print("Eccentricity: ", e)
print("Period: ", period)