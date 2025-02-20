# Logan Richan
# ph295

from numpy import array,zeros,arange,cos,pi
from cmath import polar
from numpy.linalg import solve
from matplotlib import pyplot as plt
from datetime import datetime

start=datetime.now()

#################
### CONSTANTS ###
#################
R1=1e3 #in Ohms
R2=2e3
R3=1e3
R4=2e3
R5=1e3
R6=2e3

C1=1e-6 #in Farads
C2=0.5e-6

xPlus=3 #in Volts
omega=1000 #in s^-1

R=array([1,R1,R2,R3,R4,R5,R6],float)
Rinv=1./R
C=array([1,C1,C2],float)
iwC=1j*omega*C

### MATRICES: Ax=v
A = array([[(Rinv[1]+Rinv[4]+iwC[1]), -iwC[1]                        , 0                       ],
           [-iwC[1]                 , (Rinv[2]+Rinv[5]+iwC[1]+iwC[2]), -iwC[2]                 ],
           [0                       , -iwC[2]                        , (Rinv[3]+Rinv[6]+iwC[2])]], complex)
           
v = xPlus * array([Rinv[1], Rinv[2], Rinv[3]], float)

x = solve(A,v)
print(x)

 
#Calculate amplitude and phase
amp=zeros(4,float)
phase=zeros(4,float)
for i in range(0,3):
    amp[i],phase[i]=polar(x[i])
amp[3],phase[3]=polar(xPlus)

period=zeros(4,float)

#For each Voltage:
for i in range(0,4):
    j=0
    N=1000
    Vvalues=zeros(N,complex)
    tValues=zeros(N,float)
    a=float(0)
    b=float(0.013)
    k=1
    diff=zeros(2,float)
    for t in arange(a,b,(b/N)): #through time...
        Vvalues[j] = amp[i]*cos(omega*t+phase[i]) #calculate voltage amplitudes
        tValues[j] = t
        if (j-1)>0 and k<3: #calculate period
            if Vvalues[j-1]>=0 and Vvalues[j]<0:  
                diff[k-1]=tValues[j]
                if k==2:
                    period[i]=diff[1]-diff[0]
                k+=1       
        j+=1
    plt.figure(1) # ...and plot Voltage amplitude over time
    plt.plot(tValues,Vvalues)
    plt.gca().legend(("V1", "V2", "V3", "V+"))
    plt.xlabel("time (s)")
    plt.ylabel("Voltage (V)")
    print("Computed period: ",period[i]) #Output actual period of voltage (Check with known period to Verify)
    print("Voltage", i+1, " amplitude = ", amp[i], " phase = ", phase[i]*180/pi, "degrees") #Output voltage amplitude and phase
print("Actual period: ",1/float(omega)*2*pi) #Expected period 


print(datetime.now()-start)
plt.show()
