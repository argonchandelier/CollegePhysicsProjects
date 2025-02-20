#############################
# Program
#   Assignment #4
# Author:
#   PH295 Logan Richan
# Summary:
#   Bessel Functions
#   Gives a program for Excercise 5.4 on pg148
# Date:
#   February 7, 2019
#############################

from numpy import cos, sin, pi, arange, zeros
from matplotlib import pyplot as plt

N=1000

def f(th,m,x): #the function being integrated within the Bessel function
    fth=cos(m*th-x*sin(th))
    
    return fth

def J(m,x): #the given definition of the Bessel function
    Jmx=(1/pi)*definiteInt(0,pi,m,x)
    
    return Jmx
    
def definiteInt(a,b,m,x): #calculates a definite integral for the function called (which is f(th,m,x)) from a to b
    h=((b-a)/N) #using the formula for h
    
    area=(1./3.)*h*(f(a,m,x)+f(b,m,x)) #Using the extended Simpson's rule

    for i in range(1,N,2):
        area+= (1./3.)*h*4*f(a+i*h,m,x) #sum kodd
    for i in range(2,N,2):
        area+= (1./3.)*h*2*f(a+i*h,m,x) #sum keven

    return area

xmax=20
h2=.01

def BesselGraph(m): #Plots the Bessel function for a range of x
    yvalues=zeros(xmax*int(1/h2)+2,float) #arrays for the x and y values in the Bessel function
    xvalues=zeros(xmax*int(1/h2)+2,float)
    
    i=0
    for x in arange(0,xmax+h2,h2): #gives the range for x from 0 to xmax (which is set to be 20)
        y=J(m,x) #y uses the Bessel function
        xvalues[i]=x
        yvalues[i]=y
        i+=1
    plt.plot(xvalues,yvalues) #plots the Bessel function each time the function is called

for m in range(0,2+1): #calls J(m,x) for m values of 0-2
    BesselGraph(m)

plt.show()