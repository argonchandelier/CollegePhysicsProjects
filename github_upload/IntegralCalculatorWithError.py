# Logan Richan
# ph295

from math import sin,sqrt
from numpy import zeros
from datetime import datetime

start=datetime.now()

IerrorMax=10e-6 #given maximum error
N1=1 #Start with 1 slice
Ni=N1

a=0 #Integral is from a to b
b=1

def IiCalc(Iim1,i,a,b): # Equation 5.34
    Ii=0.5*Iim1
    Ni=N1*2**(i-1)
    hi=float((b-a))/Ni    
    for k in range(1,Ni,2):
        Ii+=hi*f(a+k*hi)
    return Ii,Ni

def f(x): # function being integrated
    f=(sin(sqrt(100*x))**2)
    return f

def IerrorCalc(Ii,Iim1): # Equation 5.35
    error=(1./15.)*(Ii-Iim1)
    if error<0: #take the absolute value
        error*=-1
    return error

def increasei(Ii,i): # Increases i by 1 and reevaluates the integral for the new i
    Iim1=Ii
    i+=1
    Ii,Ni=IiCalc(Iim1,i,a,b)
    Ierror=IerrorCalc(Ii,Iim1)
    return Ni,Ii,i,Ierror

h1=(b-a)/N1 #starting values
I1=h1*0.5*(f(a)+f(b))
Ilist=[I1]
i=1
Ii=I1
Ierror=1

def parta(Ierror,Ii,i,Ni): # evaluate until the error is within the desired range
    print(Ni, Ii, Ierror)
    while Ierror>IerrorMax:
        Ni,Ii,i,Ierror=increasei(Ii,i)
        Ilist.append(Ii)
        print("n parts:", Ni, " Integral:", Ii, "+/-", Ierror)

parta(Ierror,Ii,i,Ni)
print("parta done")
print(datetime.now()-start)

##############
### PART B ###
##############

start2=datetime.now()

def RimCalc(Rleft,Rupperleft,m): #Using equation 5.51 to calculate R_i,m
    Rim=Rleft+float(Rleft-Rupperleft)/float((4**m)-1)
    return Rim

Rerror=1 #starting values
repeated=0
X=20 #create a large array of 0s for R values to fill in
Rarray=zeros([X,X],float)
RerrorMax=10e-6

#i=1

Rarray[i-1][0]=Ilist[i-1]

while Rerror>RerrorMax and i<=10: 
    Ni,Ii,i,Ierror=increasei(Ii,i)
    Rarray[i-1][0]=Ii
    for m in range(2,i+1):
        Rarray[i-1][m-1]=RimCalc(Rarray[i-1][m-2],Rarray[i-2][m-2],m)
    Rerror=float(Rarray[i-1][i-2]-Rarray[i-2][i-2])/float((4**(i-1))-1)
    if Rerror<0: #take the absolute value of Rerror
        Rerror*=-1

R=zeros([i,i],float) #put the large array into an array that will cleanly fit the R values
for j in range(0,i):
    for k in range(0,i):
        R[j][k]=Rarray[j][k]

print(R)

print(datetime.now()-start2)
