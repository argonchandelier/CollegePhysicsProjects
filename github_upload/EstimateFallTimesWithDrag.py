# Logan Richan
# ph150 lab

from numpy import sqrt,cos,sin,pi
from matplotlib import pyplot as plt

#m=.415kg, A=0.392m^2, large ball
#Large, small, blue, 
mv=[0.415,0.08,0.0117,.0451]
Av=[0.392,0.096,2.11e-5,2.87e-5]
tv=[0,0,0,0]
for i in range(0,4):
    m=mv[i]#.415 #kg
    A=Av[i]#0.392 # Cross sectional area
    
    p=.7364 # density 1.29 kg/m^3 #.7364 at 5000ft elevation
    C=.5 # Drag coefficient, depends on the geometry of the object
    
    v=0 # velocity
    th=90
    vx=cos(th*pi/180)*v
    vy=sin(th*pi/180)*v
    
    x=0
    y=16.9
    ax=0
    ay=0
    
    t=0
    dt=.05
    
    # x.append(x[-1]+vx[-1]*dt)
        
    def FD(v,vn):
        return .5*p*A*C*v*vn
    
    while y>=0:
        t+=dt
        x+=vx*dt
        y+=vy*dt
        vy+=ay*dt
        vx+=ax*dt
        v=sqrt(vx**2+vy**2)
        ax=FD(v,vx)/m
        ay=-9.8 - FD(v,vy)/m
        '''
        if y>=0:
            plt.plot(x+i,y,'.')
        else:
            plt.plot(x+i,0,'.')
    plt.show()
    '''
    tv[i]=t
print('Big Beach Ball Time: {:8.3f}'.format(tv[0]))
print('Small Beach Ball Time: {:8.3f}'.format(tv[1]))
print('Blue Ball Time: {:8.3f}'.format(tv[2]))
print('Styrofoam Time: {:8.3f}'.format(tv[3]))
