# Logan Richan
# PH295

from numpy import cos, sin, pi, zeros, sqrt
from pylab import show, imshow, jet

N=1000

def f(th,m,x):
    fth=cos(m*th-x*sin(th))
    
    return fth

# Bessel Function
def J(m,x):
    Jmx=(1/pi)*definiteInt(0,pi,m,x)
    
    return Jmx
    
def definiteInt(a,b,m,x):
    h=((b-a)/N)

    area=(1./3.)*h*(f(a,m,x)+f(b,m,x))

    for i in range(1,N,2):
        area+= (1./3.)*h*4*f(a+i*h,m,x) #sum kodd
    for i in range(2,N,2):
        area+= (1./3.)*h*2*f(a+i*h,m,x) #sum keven
        
    return area

###functions above are the same as the other program

w=500 #wavelength in nm
k=2*pi/w

def computeI(r): #the given intensity function
    if r==0:
        r=0.0001
    I=(J(1,k*r)/(k*r))**2
    return I

M=zeros([201,201],float) #matrix of x and y values from negative to positive 1 micrometer

for i in range(-100,101):
    for j in range(-100,101): 
        r=sqrt(((i*10)**2)+((j*10)**2)) #the values of i*10 and j*10 are in nm (because w is in nm) and goes 10 at a time as i and j jump up 1 value at a time
        I=computeI(r) #uses the given intensity function I(r)
        M[i+100,j+100]=I
        
imshow(M,origin="lower",vmax=0.01,) #graphs the matrix of intensity values
jet()
show()
