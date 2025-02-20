# Logan Richan
# ph295

from numpy import sin, e, zeros, sqrt
from random import random
from datetime import datetime

start = datetime.now()

# rectangle x edge values (x goes from a-b)
a = -2. 
b = 2.
# rectangle y edge values (y goes from c-d)
c = 0.  
d = 10.
# Area of the rectangle
A = (d-c)*(b-a) # Area = length * width

N=1000000

def f(x): # Function to integrate
    return x**3 - sin(x) + e**(-x) 

def Icalc(): # Calculate the Integral
    count=0
    for i in range(N):
        x = 4*random()-2 # random number from -2 to 2
        y = 10*random()  # random number from  0 to 10
        Y = f(x) # actual y value evaluated at x
        if (y<=Y and Y>0) or (y>=Y and Y<0):
            count+=1
   
    I = count/float(N) * A
    return I

M = 10 # Number of times I is computed
Ivalues=zeros(M,float)
for i in range(M): # Get 10 values for I
    Ivalues[i]=Icalc()

Imean = sum(Ivalues)/float(M)
sd = sqrt(Imean*(A-Imean)) / sqrt(N) #standard deviation of I values; equation from book

print(Imean,"+/-",sd)
print(datetime.now()-start)
