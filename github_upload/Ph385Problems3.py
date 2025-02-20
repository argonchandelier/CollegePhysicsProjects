# Logan Richan
# ph385

from numpy import pi,arange,linspace,sin,sinh,cos
from matplotlib import pyplot as plt

def P3_1_a():
    ### a ###
    #initialize variables
    a=0
    b=pi
    N=500
    
    x=linspace(a,b,N) # create cell-edge grid from a-b
    y=sin(x)*sinh(x) # put x into a function
    print(len(x), ' ...there is one less cell than grid points, so there are ', len(x)-1, ' cells.')
    
    plt.plot(x,y) # plot the function
    
    print('graph plotted')
    print('End of Problem 3.1a\n')

def P3_1_b():
    ### b ###
    plt.figure(2) #start new figure
    
    #initialize variables
    a=0
    b=pi
    N=500
    dx=(b-a)/float(N)
    
    x2=linspace(a+dx/2.,b-dx/2.,N-1) # create a cell-center grid from a-b
    print(x2, len(x2))
    
    y2=sin(x2)*sinh(x2) # put x into the same function as above
    plt.plot(x2,y2) # plot
    
    print('graph plotted')
    print('End of Problem 3.1b\n')

def P3_1_c():
    ### c ###
    plt.figure(3) #start new figure
    
    # initialize variables
    a=0
    b=2
    N=5000
    dx=(b-a)/float(N)
    
    x3=linspace(a+dx/2.,b-dx/2.,N-1) # create a cell-center grid from a-b
    y3=cos(x3) # use a new function
    
    intEst=sum(y3)*dx # estimate integral based on the grid
    intAct=sin(2) # integral evaluated
    print(intEst, ' = ', intAct) # verify the estimate and actual integral are about equal
    
    plt.plot(x3,y3) # plot

    print('graph plotted')
    print('End of Problem 3.1c\n')



P3_1_a()
P3_1_b()
P3_1_c()

plt.show()