# Logan Richan
# ph295

from math import sqrt
from numpy import zeros
from pylab import plot,show,xlabel,ylabel

m=0.75
g=-9.8
yi1=0
vi1=0
thrust=float(input("Thrust (in N): ")) # added float assertion
while (thrust/m)<(-g): #added line
    print("Thrust too small, please try again.") #added line
    thrust=input("Thrust (in N): ") #added line
t1=float(input("Burn time (in s): ")) # added float assertion
a=thrust/m
a1=a+g # "-" changed to "+"
vi2=a1*t1
a2=g

def yfCalc(yi,vi,t,a):
    yf=yi+vi*t+0.5*a*(t**2)
    return yf

yi2=yfCalc(yi1,vi1,t1,a1)
t2=-(vi2/a2)-(sqrt((vi2**2)+(2*a2*(-yi2)))/a2)
tTotal=int(t1+t2)
yValues=zeros((tTotal+1),float)
tValues=zeros((tTotal+1),float)

for t in range(0,int(t1)+1):
    yValues[t]=yfCalc(yi1,vi1,t,a1)
    tValues[t]=t

for t in range(1,int(t2)+1): #starting at 1 because the 0 value was included as the last value in the previous loop
    yValues[int(t1)+t]=yfCalc(yi2,vi2,t-(t1-int(t1)),a2)
    tValues[int(t1)+t]=int(t1)+t
    if (t==int(t2) and (tTotal>int(t1)+int(t2))):
        tValues[tTotal]=tTotal #assertions are used in case int(t1+t2) is more than int(t1)+int(t2)
        yValues[tTotal]=yfCalc(yi2,vi2,1+t-(t1-int(t1)),a2) #"y" changed to "t" in "tTotal"

plot(tValues,yValues)
xlabel("time (s)")
ylabel("height (m)")
show()
