# Logan Richan
# ph295

from pylab import linspace,plot,show,ylabel,xlabel
from numpy import sin,cos,pi

h=27.4 #given initial height
v=52.4 #given velocity
g=-9.81 #Earth's gravitational constant

for ang in range(0,90,10): #graphs each angle from 0 to 80 degrees in increments of 10 degrees

    vx=v*cos(ang*pi/180) #velocity in the x direction
    vy=v*sin(ang*pi/180) #velocity in the y direction

    tfinal=(-vy-(((vy**2)-4*0.5*g*h)**(0.5)))/(g) #calculates the time when the ground is hit
    xfinal=vx*tfinal #calculates the distance when the ground is hit (and when the graph stops plotting)
    
    x=linspace(0,xfinal,100) #calculation of x until the ground is hit (when y==0)
    t=x/vx  #used to calculate y
    y=h+vy*t+0.5*g*t**2
    
    plot(x,y) #plots each trajectory for each angle

xlabel("Ground distance (m)")
ylabel("Height (m)") #labels

show()