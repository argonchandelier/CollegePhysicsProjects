# Logan Richan
# ph385

from matplotlib import pyplot as plt
from numpy import pi, cos, sin, exp, linspace, zeros


class trajectory:
    # Initialize variables
    def __init__(self,v,th,r):
        self.th = th*pi/180.
        self.vx = v*cos(self.th)
        self.vy = v*sin(self.th)
        self.x = r[0]
        self.y = r[1]
        
        self.tau = 0.001
        self.g = 9.8
        self.C = 0.5
        
        self.m = 0.145 # in kg
        diam = 0.074 # in m
        self.A = pi * diam**2 / 4.
        
        self.T0 = 293 # in K
    
    # Set variables directly
    def SetVars(self,C,A,p,m):
        self.C = C
        self.A = A
        self.p = p
        self.m = m
    
    # Drag equation
    def Drag(self, p, v, vD):
        return -0.5*p*self.A*self.C*v*vD
                
    # Plot trajectory
    def plot(self):
        counter = 0
        X=[]
        Y=[]
        while self.y > 0: # Until ground is hit
            # Use Euler steps
            self.x += self.vx * self.tau
            self.y += self.vy * self.tau
            v = (self.vx**2 + self.vy**2)**(0.5)
            self.vx += (self.Drag(self.p,self.vx,v)/self.m) * self.tau
            self.vy += (-self.g + self.Drag(self.p,self.vy,v)/self.m) * self.tau
            
            
            if counter %20 == 0: # Plot only 1/20 of the points
                X.append(self.x)
                Y.append(self.y)
            
            counter+=1
   
        plt.plot(X,Y)
        plt.show()
    
    # Density change function (in part b)
    def density(self, y):
        a = 6.5e-3
        b = 2.5
        return self.p*(1-a*y/self.T0)**b
    
    # Verify equation given in part b
    def plotDensityTest(self):
        N = 100
        Y = linspace(0,10000,N)
        P = zeros(N, float)
        for i in range(N):
            P[i] = self.density(Y[i])
        
        plt.plot(Y,P)
        plt.show()
    
    # Plot with modified density function
    def plot2(self):
        counter = 0
        X=[]
        Y=[]
        while self.y > 0: # Until ground is hit
            # Use Euler steps
            self.x += self.vx * self.tau
            self.y += self.vy * self.tau
            v = (self.vx**2 + self.vy**2)**(0.5)
            self.vx += (self.Drag(self.density(self.y),self.vx,v)/self.m) * self.tau
            self.vy += (-self.g + self.Drag(self.density(self.y),self.vy,v)/self.m) * self.tau
            
            
            if counter %20 == 0: # Plot only 1/20 of the points
                X.append(self.x)
                Y.append(self.y)
            
            counter+=1
   
        plt.plot(X,Y)
        #plt.show()

# a
traj = trajectory(750,45,[0,1])
traj.SetVars(0.5,0.007,1.29,50)
traj.plot()

# b
plt.figure(2)
traj.plotDensityTest()

# c/d
traj2 = trajectory(750,45,[0,1])
traj2.SetVars(0.5,0.007,1.29,50)
plt.figure(1)
traj2.plot2()

plt.show()

# The cannon shell range is about 3000 m more with the corrected air density
