# Logan Richan
# ph385

from matplotlib import pyplot as plt
from numpy import pi, cos, sin, exp


class trajectory():
    
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
    def Euler2(self, p):
        counter = 0
        X=[]
        Y=[]
        while self.y > 0: # Until ground is hit
            # Use Euler steps
            self.x += self.vx * self.tau
            self.y += self.vy * self.tau
            v = (self.vx**2 + self.vy**2)**(0.5)
            self.vx += (self.Drag2(p,self.vx,v)/self.m) * self.tau
            self.vy += (-self.g + self.Drag2(p,self.vy,v)/self.m) * self.tau
                   
            if counter %20 == 0: # Plot only 1/20 of the points
                X.append(self.x)
                Y.append(self.y)
            
            counter+=1

        plt.plot(X,Y)
        #plt.show()
    
# b
traj = trajectory(49,35,[0,1])
traj.Euler(1.29)
# c
trajD = trajectory(49,35,[0,1]) # Denver trajectory
trajA = trajectory(49,35,[0,1]) # Atlanta trajectory
trajD.Euler(0.96)
trajA.Euler(1.22)
# Denver would be best

# d
plt.figure(2)
trajD2 = trajectory(49,35,[0,1]) # Denver trajectory
trajA2 = trajectory(49,35,[0,1]) # Atlanta trajectory
trajD2.Euler2(0.96)
trajA2.Euler2(1.22)
# With this drag, the balls fly a bit farther

plt.show()
