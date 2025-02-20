# Logan Richan
# ph385

from scipy.special import jv
from numpy import linspace,array,append,cos
from matplotlib import pyplot as plt

class CellEdgeGrid():
    
    # Create the cell edge grid
    def __init__(self,a,b,N):
        self.x,self.dx=linspace(a,b,N,retstep=True)
        self.yPs()
   
    # Put the grid into a function and differentiate the function twice
    def yPs(self):
        y = jv(0,self.x)
        
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
        self.yPTrue = -jv(1,self.x)
        self.yPPTrue = 0.5*(-jv(0,self.x) + jv(2,self.x))
        
        self.y, self.yPL, self.yPPL, self.yPQ, self.yPPQ = y,yPL,yPPL,yPQ,yPPQ
    
    # Compare extrapolated values to actual values
    def Compare(self):
        print("f'(x) at the start point by linear & quadratic extrapolation and the true value",self.yPL[0], self.yPQ[0], self.yPTrue[0],)
        print("\n")
        print("f'(x) at the end point by linear & quadratic extrapolation and the true value",self.yPL[-1], self.yPQ[-1], self.yPTrue[-1],"\n")
        print("\n")
        print("f''(x) at start points by linear & quadratic extrapolation and the true values",[self.yPL[0],self.yPL[1]],[self.yPQ[0],self.yPQ[1]],[self.yPTrue[0],self.yPTrue[1]],"\n")
        print("\n")
        print("f''(x) at end points by linear & quadratic extrapolation and the true values",[self.yPL[-2],self.yPL[-1]],[self.yPQ[-2],self.yPQ[-1]],[self.yPTrue[-2],self.yPTrue[-1]],"\n")
      
    # Plot functions and derivatives and double derivatives
    def Plot(self):

        plt.plot(self.x,self.y)
        plt.plot(self.x,self.yPL)
        plt.plot(self.x,self.yPPL)
        
        plt.plot(self.x,self.yPQ)
        plt.plot(self.x,self.yPPQ)
        
        plt.plot(self.x,self.yPTrue)
        plt.plot(self.x,self.yPPTrue)
        plt.show()

grid = CellEdgeGrid(0,5,100) # Create the cell edge grid
grid.Compare() # Compare extrapolated values with actual
grid.Plot() # Plot
