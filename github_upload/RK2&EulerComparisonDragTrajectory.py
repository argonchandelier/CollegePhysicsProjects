# Logan Richan
# ph385

from matplotlib import pyplot as plt
from numpy import pi, cos, sin, exp


class trajectory():
    
    # Initialize variables
    def __init__(self,v,th,r,p):
        self.th = th*pi/180.
        self.vx = v*cos(self.th)
        self.vy = v*sin(self.th)
        self.r = r
        self.v = [v*cos(self.th),v*sin(self.th)]
        self.x = r[0]
        self.y = r[1]
        
        self.tau = 0.01
        self.g = 9.8
        self.C = 0.5

        
        self.m = 0.145 # in kg
        diam = 0.074 # in m
        self.A = pi * diam**2 / 4.
        
        self.p = p
    
    # Drag
    def Drag(self, p, v, vD):
        return -0.5*p*self.A*self.C*v*vD
                
    # Plot trajectory
    def Euler(self, p):
        counter = 0
        X=[]
        Y=[]
        while self.y > 0: # Until ground is hit
            # Use Euler steps
            self.x += self.vx * self.tau
            self.y += self.vy * self.tau
            v = (self.vx**2 + self.vy**2)**(0.5)
            self.vx += (self.Drag(p,self.vx,v)/self.m) * self.tau
            self.vy += (-self.g + self.Drag(p,self.vy,v)/self.m) * self.tau
            
            
            if counter %20 == 0: # Plot only 1/20 of the points
                X.append(self.x)
                Y.append(self.y)
            
            counter+=1
   
        plt.plot(X,Y)
        #plt.show()
    
    # Drag with formula for non-constant C
    def Drag2(self, p, v, vD):
        C = .198 + .295 / (1+exp((v-35)/5.))
        return -0.5*p*self.A*C*v*vD
        
    
    # Plot trajectory with different C
    def Euler2(self,doPlot=True):
        counter = 0
        X=[]
        Y=[]
        while self.y > 0: # Until ground is hit
            # Use Euler steps
            self.x += self.vx * self.tau
            self.y += self.vy * self.tau
            v = (self.vx**2 + self.vy**2)**(0.5)
            self.vx += (self.Drag2(self.p,self.vx,v)/self.m) * self.tau
            self.vy += (-self.g + self.Drag2(self.p,self.vy,v)/self.m) * self.tau
                   
            if counter %20 == 0: # Plot only 1/20 of the points
                X.append(self.x)
                Y.append(self.y)
            
            counter+=1
        Range = self.x
        
        # Return values to normal
        self.x = self.r[0]
        self.y = self.r[1]
        self.vx = self.v[0]
        self.vy = self.v[1]
        
        if (doPlot):
            plt.plot(X,Y)
            #plt.show()
        
        return Range
    
    # Plot the trajectory using 2nd order Runge-Kutta
    def RK2(self, doPlot=True):
        counter = 0
        X=[]
        Y=[]
        while self.y > 0:
            #'''
            v = (self.vx**2 + self.vy**2)**(0.5)
            
            # Calculate k1
            k1_x = self.tau*self.vx
            k1_vx = self.tau*(self.Drag2(self.p,self.vx,v)/self.m)
            
            k1_y = self.tau*self.vy
            k1_vy = self.tau*(-self.g + self.Drag2(self.p,self.vy,v)/self.m)
            
            # Calculate k2
            vH = ((self.vx + 0.5*k1_vx)**2 + (self.vy + 0.5*k1_vy)**2)**(0.5)
            
            k2_x = self.tau*(self.vx + k1_vx/2.)#self.x + 0.5*k1_x
            k2_vx = self.tau*(self.Drag2(self.p,self.vx+0.5*k1_vx,vH)/self.m)
            
            k2_y = self.tau*(self.vy + k1_vy/2.)
            k2_vy = self.tau*(-self.g + self.Drag2(self.p,self.vy+0.5*k1_vy,vH)/self.m)
            
            
            
            self.x += k2_x
            self.vx += k2_vx
            self.y += k2_y
            self.vy += k2_vy
            #'''
            '''
            v = (self.vx**2 + self.vy**2)**(0.5)
            
            xH = self.x + self.tau/2 * self.vx
            vxH = self.vx + self.tau/2 * (self.Drag2(self.p,self.vx,v)/self.m)
            
            yH = self.y + self.tau/2 * self.vy
            vyH = self.vy + self.tau/2 * (-self.g + self.Drag2(self.p,self.vy,v)/self.m)
            
            vH = ((vxH)**2 + (vyH)**2)**(0.5)
            
            self.x += self.tau * vxH
            self.vx += self.tau * (self.Drag2(self.p,vxH,vH)/self.m)
            
            self.y += self.tau * vyH
            self.vy += self.tau * (-self.g + self.Drag2(self.p,vyH,vH)/self.m)
            
            '''
            if counter %20 == 0: # Plot only 1/20 of the points
                X.append(self.x)
                Y.append(self.y)
            
            
            counter+=1
            
            if counter > 100000:
                break
        
        if (doPlot):            
            plt.plot(X,Y)
            #plt.show()
        
        Range = self.x
        
        # Return values to normal
        self.x = self.r[0]
        self.y = self.r[1]
        self.vx = self.v[0]
        self.vy = self.v[1]
        
        return Range
    
    # Part c: Convergence of RK2
    def CompareRK2(self):
        tau = self.tau # Put a dummy variable to hold the old tau
        self.tau = 1.
        
        # Initialize taus and ranges
        Ranges = []
        Taus = []
        while self.tau > 10e-5: # Until tau is at the desired value
            Ranges.append(self.RK2(doPlot=False)) # Find the range at that tau
            Taus.append(self.tau)
            self.tau /= 2. # Divide tau by 2
        self.tau = tau
        
        plt.plot(Ranges,Taus,'.')
        plt.xscale("log")
        #plt.show()
    
    # Part d: Convergence of Euler's method
    def CompareEuler(self): # Similar to CompareRK2() except using Euler2() instead
        tau = self.tau
        self.tau = 1.
        
        Ranges = []
        Taus = []
        while self.tau > 10e-5:
            Ranges.append(self.Euler2(doPlot=False))
            Taus.append(self.tau)
            self.tau /= 2.
        self.tau = tau
        
        plt.plot(Ranges,Taus,'.')
        plt.xscale("log")
        #plt.show()
        
    

traj = trajectory(49,35,[0,1],1.29)
traj.RK2()
traj.Euler(1.29)

plt.figure(2)
newTraj = trajectory(49,35,[0,1],1.29)
newTraj.CompareRK2() # c
newTraj.CompareEuler() # d

plt.show()

# e
# The convergence for RK2 is much faster

