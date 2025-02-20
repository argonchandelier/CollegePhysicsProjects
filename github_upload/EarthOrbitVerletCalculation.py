from numpy import array, sqrt, arange, zeros, pi, sin, cos
from matplotlib import pylab as plt

### CONSTANTS ###
#################
G=6.6738e-11 #in m^3/(kg*s^2); Newton's gravitational constant
M=1.9891e30 #mass of sun in kg
m=5.9722e24 #mass of Earth in kg

### RANGE ###
#############
numRev=5 #Plot of 5 revolutions
h=dt=3600. # 1 hr step size
a=0
b=dt*24*365.25*numRev
N=int((b-a)/h)

### POINTS ###
##############
tPoints=arange(a,b,h)
xPoints=zeros(N,float)
yPoints=zeros(N,float)

KEpoints=zeros(N,float)
Upoints=zeros(N,float)
TEpoints=zeros(N,float)

### POSITION AND VELOCITY VECTORS ###
#####################################
r0=1.4710e11 #perihelion distance in meters
v0=3.0287e4 #perihelion velocity in m/s
r=array([r0,0],float)
v=array([0,v0],float)

### FUNCTIONS ###
#################
def mag(r): # magnitude of the given vector; used for both r and v vectors
    return sqrt(r[0]**2 + r[1]**2)

def f(r,t): #d^2/dt^2 *r
    return -G*M*r/(mag(r))**3

def U(r): #Potential Energy Function
    return -G*M*m/mag(r)

def KE(v): #Kinetic Energy Function
    return 0.5*m*(mag(v)**2)

def plotCircle(rad): # Used in verification
    N=1000
    thPoints=arange(0,2*pi,2*pi/N)
    xPts=zeros(N,float)
    yPts=zeros(N,float)
    i=0
    for th in thPoints:
        xPts[i]=rad*cos(th)
        yPts[i]=rad*sin(th)
        i+=1
    plt.plot(xPts,yPts,'--')
    plt.show()

### VERLET METHOD ###
#####################
vHalf = v + 0.5*h*f(r,tPoints[0])
i=0
for t in tPoints:
    xPoints[i] = r[0]
    yPoints[i] = r[1]
    KEpoints[i] = KE(v)
    Upoints[i] = U(r)
    TEpoints[i] = KEpoints[i]+Upoints[i]
    r += h*vHalf
    k = h*f(r,t+h)
    v = vHalf + 0.5*k
    vHalf += k
    i += 1

### PLOTS ###
#############
tPoints /= 3600*24 #make time in units of days from seconds

plt.subplot(131)
plt.plot(xPoints,yPoints) # Earth's orbit
plt.plot(0,0,'.') # The Sun
plt.xlabel("x (m)")
plt.ylabel("y (m)")
plt.title("Earth's Orbit")
#plotCircle(r0)

plt.subplot(132)
plt.plot(tPoints,KEpoints,label='Kinetic Energy')
plt.plot(tPoints,Upoints,label='Potential Energy')
plt.plot(tPoints,TEpoints,label='Total Energy')
plt.xlabel("time (days)")
plt.ylabel("Energy (J)")
plt.legend(loc='center left')
plt.title('Energies')

plt.subplot(133)
plt.plot(tPoints,TEpoints)
plt.xlabel("time (days)")
plt.ylabel("Energy (J)")
plt.title('Total Energy')

plt.show()
