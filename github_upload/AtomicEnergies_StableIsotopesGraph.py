#############################
# Program
#   PH295 Assignment #2
# Author:
#   Logan Richan
# Summary:
#   Based on excercise 2.10 on pg75 in the book.
#   Starts with a prompt for which part in the excercise to answer from a-d.
# Date:
#   January 24, 2019
#############################
from numpy import zeros
from pylab import imshow,show,xlabel,ylabel

#CONSTANTS
a1=15.8 #constants a1-a4 in MeV
a2=18.3
a3=0.714
a4=23.2

####################################
# Functions for each part
####################################
def original(x): #for parts a and b
    A=int(input("Enter A: ")) #input atomic mass
    Z=int(input("Enter Z: ")) #input atomic number
    
    B=Bcalc(A,Z) #calculates the binding energy
    
    if x==1: #part a   
        print(B, "MeV") #prints the total binding energy
    if x==2: #part b
        C=B/A #binding energy per nucleon
        print(C, "MeV/nucleon") #prints the binding energy per nucleon
        
def partc(): #part c
    Z=int(input("Enter Z: ")) #input atomic number
    CmaxCalc(Z) #calculates the maximum binding energy per nucleon
    
def partd(): #part d
    for Z in range(1,101): #calculates the maximum binding energy per nucleon for all Z values 1-100
        CmaxCalc(Z)

#####################################
# Functions used
#####################################
def a5calc(A,Z): #a5 calculator (according to the given guidelines in the book) in MeV
    if (A%2 != 0): 
        a5=0
    elif (Z%2 != 0):
        a5=-12.0
    else:
        a5=12
        
    return a5

def Bcalc(A,Z): #calculates the binding energy, B
    a5= a5calc(A,Z)
    B= a1*A - a2*(A**(2./3.)) - a3*(Z**2)*(A**(-1./3.)) - (a4*((A-2*Z)**2))/A + a5*(A**(-1./2.)) #formula for binding energy in the book
    
    return B

def CmaxCalc(Z): #calculates the maximum binding energy per nucleon
    Cmax=0
    for A in range(Z,3*Z+1):
        B=Bcalc(A,Z)
        C=B/A #binding energy per nucleon value
        if (C>Cmax):
            Cmax=C
            Amax=A
    C=Cmax
    A=Amax    
    print(A, " most stable A for Z = ", Z, " with binding energy per nucleon of ", C, "MeV/nucleon")
    
def graph():
    data=zeros([200,200],float)
    for Z in range(1,201):
        for A in range(1+Z,201+Z): #which is the same as the range of N from 1-200
            B=Bcalc(A,Z)
            C=B/A
            N=A-Z #Neutron number
            if C>=0: #only positive values are shown
                data[Z-1,N-1]=C            
    imshow(data,origin="lower",extent=[1,200,1,200])
    xlabel("N")
    ylabel("Z")
    show()

####################################################################
# Input which part, where 1-4 is equal to part a-d, respectively
# and other input, such as 0, returns a graph
####################################################################
part=int(input("show part (using an int, 1-5): "))

if (part == 1):
    print("part a:")
    original(1)
elif (part == 2):
    print("part b:")
    original(2)
elif (part == 3):
    print("part c:")
    partc()
elif (part == 4):
    print("part d:")
    partd()
else:
    print("Extra Credit:")
    graph()
