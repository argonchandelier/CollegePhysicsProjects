# Logan Richan
# ph385

from matplotlib import pyplot as plt


class bounce():
    
    # Initialize variables
    def __init__(self,v,r):
        self.vx = v[0]
        self.vy = v[1]
        self.x = r[0]
        self.y = r[1]
        
        self.tau = 0.001
        self.g = 9.8
                
    def BetterEuler(self):
        counter = 0
        tau0 = self.tau
        while self.x < 20:
            if self.y + self.vy * self.tau < 0: # make a new tau to scale so that y ends at 0
                tau0 = -self.y/(self.vy)
            
            # Do the Euler method as before
            self.x += self.vx * tau0
            self.y += self.vy * tau0
            self.vy += -self.g * tau0
            
            if tau0 != self.tau: # Then move with an Euler step to catch up to the regular time step interval after tau was modified
                print(self.y) # Check to see y is in fact at 0
                self.vy = 0.95*abs(self.vy) # Do the bounce... with dampening
                tau0 = self.tau - tau0 # Catch up tau
                
                self.x += self.vx * tau0
                self.y += self.vy * tau0
                self.vy += -self.g * tau0
                
                tau0 = self.tau # Put tau back to normal
                
            if counter %30 == 0: # Only use once every 10 iterations for faster performance
                # Make a movie of the points
                plt.plot(self.x,self.y,'k.')
                plt.xlim(0,20)
                plt.ylim(0,1.2)
                plt.draw()
                plt.pause(0.01)
            counter+=1
    
    def Euler(self):
        counter = 0
        while self.x < 10:
            # Use Euler steps
            self.x += self.vx * self.tau
            self.y += self.vy * self.tau
            self.vy += -self.g * self.tau
            
            if self.y < 0:
                self.vy = abs(self.vy) # Do the bounce
            if counter %20 == 0: # Only use once every 10 iterations for faster performance
                # Make a movie of the points
                plt.plot(self.x,self.y,'k.')
                plt.xlim(0,10)
                plt.ylim(0,1.2)
                plt.draw()
                plt.pause(0.01)
            counter+=1
    
    
    
bouncing = bounce([1,0],[0,1])
bouncing.BetterEuler()