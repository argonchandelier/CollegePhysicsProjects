# Logan Richan
# ph336

from matplotlib import pyplot as plt


class bounce():
    
    def __init__(self,v,r):
        self.vx = v[0]
        self.vy = v[1]
        self.x = r[0]
        self.y = r[1]
        
        self.tau = 0.001
        self.g = 9.8
                
    def Euler(self):
        
        counter = 0
        while self.x < 10:
            self.x += self.vx * self.tau
            self.y += self.vy * self.tau
            self.vy += -self.g * self.tau
            
            if self.y < 0:
                self.vy = abs(self.vy)
            if counter %10 == 0:
                plt.plot(self.x,self.y,'k.')
                plt.xlim(0,10)
                plt.ylim(0,1.2)
                plt.draw()
                plt.pause(0.01)
            counter+=1
    
    
    
bouncing = bounce([1,0],[0,1])
bouncing.Euler()

# Note that the bounces get higher due to propagating errors using Euler's method
