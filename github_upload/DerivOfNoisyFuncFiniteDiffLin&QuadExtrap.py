# Logan Richan
# ph385

from numpy import cos, linspace, append, array, sin
from numpy.random import uniform
from matplotlib import pyplot as plt


class CellEdgeGrid:
    # Create the cell edge grid
    def __init__(self,a,b,N):
        self.x,self.dx=linspace(a,b,N,retstep=True)
        self.yPs()
    
    # cos function with noise
    def f(self):
        return cos(self.x)+0.001*uniform(0,1,len(self.x))
    
    # Put the grid into a function and differentiate the function twice
    def yPs(self):
        y = self.f()
        
        #Differentiate using the central difference method
        yPL = (y[2:] - y[:-2])/(2*self.dx)
        yPPL = (yPL[2:] - yPL[:-2])/(2*self.dx)
        
        #Use linear extrapolation to finish the derivatives
        yPL=append(array( [yPL[1]*(-1)+(2)*yPL[0]] ),
            append(yPL,array( [yPL[-1]*(2)-(1)*yPL[-2]] )))
        yPPL=append(array( [yPPL[1]*(-2)+(3)*yPPL[0], yPPL[1]*(-1)+(2)*yPPL[0]] ),
             append(yPPL,array( [yPPL[-1]*(2)-(1)*yPPL[-2], yPPL[-1]*(3)-(2)*yPPL[-2]] )))
        
        #Use quadratic extrapolation to finish the derivatives
        yPQ=list(yPL)
        yPPQ=list(yPPL)
        yPQ[0]= 3*yPQ[1] - 3*yPQ[2] + yPQ[3]
        yPQ[-1]= yPQ[-4] - 3*yPQ[-3] + 3*yPQ[-2]
        yPPQ[0],yPPQ[1]= 6*yPPQ[2] - 8*yPPQ[3] + 3*yPPQ[4], 3*yPPQ[2] - 3*yPPQ[3] + yPPQ[4]
        yPPQ[-2],yPPQ[-1]= yPPQ[-5] - 3*yPPQ[-4] + 3*yPPQ[-3], 3*yPPQ[-5] - 8*yPPQ[-4] + 6*yPPQ[-3]
        
        # Actual Derivative values
        self.yPTrue = -sin(self.x)
        self.yPPTrue = -cos(self.x)

        self.y, self.yPL, self.yPPL, self.yPQ, self.yPPQ = y,yPL,yPPL,yPQ,yPPQ
        
    # Plot functions and derivatives (but not double derivatives, as that is too noisy
    def Plot(self):

        plt.plot(self.x,self.y)
        plt.plot(self.x,self.yPL)
        #plt.plot(self.x,self.yPPL)
        
        plt.plot(self.x,self.yPQ)  
        #plt.plot(self.x,self.yPPQ)      
        
        plt.plot(self.x,self.yPTrue)
        #plt.plot(self.x,self.yPPTrue)
        plt.show()


# Make a cell edge grid with 1000 points and plot the functions with the derivatives
grid = CellEdgeGrid(0,5,1000)
grid.Plot()

plt.figure(2)

# Do the same but only with 100 points
grid2 = CellEdgeGrid(0,5,100)

grid2.Plot()

# It looks less noisy with less points