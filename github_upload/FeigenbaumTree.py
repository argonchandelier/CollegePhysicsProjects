#############################
# Program
#   PH295 Assignment #3
# Author:
#   Logan Richan
# Summary:
#   Gives a program for Excercise 3.6  on pg120
# Date:
#   January 31, 2019
#############################
from numpy import zeros
from pylab import plot, show
from datetime import datetime

#CONSTANTS
rmin=1 #r will be shown between these two values
rmax=4
h=.01 #step size
b=1000 #number of times the chaos equation iterates for a value of r after the first 1000 iterations
startx=0.5 #the starting value of x before iterations of the equation occurs

start=datetime.now() #start the program timer before calculations begin

a=int(float(rmax-rmin)*int((1/h))) #setting end of range of r equal to rmax

r=zeros(a,float) #array for the values of r (from rmin to rmax in steps of the step size h)
x2=zeros([a,b],float) #multi-dimensional array for the values of r for each iteration of the equation (after the first 1000 iterations)

for i in range(0,a): #iterating r until it equals rmax
    r[i]=rmin+h*i #starting r at 1 and increasing by the step size each iteration
    x=startx #x is set to the starting value every time the iteration process is restarted
    for j in range(0,1000): #iteration for the first 1000 times
        newx=x*r[i]*(1-x)
        x=newx
    x2[i][0]=x #begin listing in the array starting at the thousandth iteration
    for j in range(0,b-1): #list of x values from the 1000th iteration to the (b+1000)th iteration for an r value
        x2[i][j+1]=x2[i][j]*r[i]*(1-x2[i][j])

plot(r,x2,'ro', markersize=2) #plot and show the graph

runtime=datetime.now()-start #get and print the runtime
print("Runtime:", runtime)

show()

