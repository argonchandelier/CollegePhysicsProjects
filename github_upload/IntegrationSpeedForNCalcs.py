#############################
# Program
#   PH295 In-class Assignment #7
# Author:
#   Logan Richan
# Summary:
#   Based on problem 4.4 on pg138 in the book.
# Date:
#   January 31, 2019
#############################
from math import sqrt,pi
from numpy import zeros,log10
from datetime import datetime
from pylab import plot,show,xlabel,ylabel

Iactual=pi/2. # the actual value that the given answers will be compared to

x=zeros(7,float) # 7 values will be plotted for x and y
y=zeros(7,int)

#I=int(sqrt(1-x^2) dx) from -1 to 1

def yk(h,k): # y_k calculation of y_k using the given definition of y_k
    xk=-1.+h*k #x_k calculated also using the given definition
    yk=sqrt(1-(xk**2))
    
    return yk

def Isum(N): # the sum of the given summation equation from k=1 to N
    sum=0
    for k in range (1,N+1):
        h=float(2./(float(N)))
        sum+=h*yk(h,k)
        
    return sum

n_exp_last = 7 #8
for i in range(2,n_exp_last+1): #iterating the exponent of 10 from 2 to 8
    N=int(10**i) #...which will give the values of N^i for every i between 2 to 8
    
    start=datetime.now()
    I=Isum(N) #inputting the current N value into the given summation function
    end=datetime.now()
    runtime=end-start #calculation of the runtime by subtracting the time before calculation from the time after
    
    x[i-2]=runtime.total_seconds() # conversion of runtime into seconds and putting to an array for plotting ...Note: is equal to 0 for x[0]
    y[i-2]=N # putting the N values used into an array for plotting
    
    percentError=((I-Iactual)/Iactual)*100 # calculation of percent error
    print("N = 10^", i, "I = ", I, "percent error: ", percentError,"%") # printing of the values of N, I, % error, and runtime for table input
    print(runtime)
    print(" ")


plot(log10(x),log10(y)) #plotting the log-log of the runtime vs. N values
xlabel("10^x = runtime in seconds")
ylabel("10^y = N")
show()
