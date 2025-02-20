from matplotlib import pyplot as plt
from numpy import sqrt, pi, exp, arange, zeros
from gaussxw import gaussxwab

#R=8.3
#c=1.5*R

k = 1.381e-23 #J/K    ...=8.617e-5eV/K
AN=6.02e23

T=115.3+273.15      #373.15 #+ 100 #*c #J/mol
enth=35100   #40660. #J/mol
Nt=AN

Ecut=enth/AN    #J
R=k*AN

Q=k*T

#Reconstruct
#'''
Q=500.
Ecut=Q*7*1.5#12
#'''

print("deltaS = ", enth/(k*AN*T)) #==~10.5 usually

def N(E,T):
    #Q=500 #Q=k*T
    NE=2*Nt/(sqrt(pi)*((Q)**(3./2.))) * sqrt(E) * exp(-E/(Q))
    return NE

def N2(E,T):
    N2=N(E,T)*E
    return N2
    
def integ(f,a,b,T): #integrating using Gaussian quadrature
    N=1000
    x,w=gaussxwab(N,a,b)
    I=0
    for i in range(0,N):
        I+=w[i]*f(x[i],T)
    return I

def graph():

    Npt=1000
    a=0
    b=Ecut #/14
    h=(b-a)/Npt
    #X=int((b-a)*h)
    Evalues=zeros(Npt,float)
    Nvalues=zeros(Npt,float)
    N2values=zeros(Npt,float)
    i=0
    #print(h)
    #gate=1
    for E in arange(a,b,h):
        if (i < Npt):
            Nvalues[i]=N(E,T)
            N2values[i]=N2(E,T) ###
            Evalues[i]=E
            i+=1
    #'''
    #plt.plot([1.5*k*T,1.5*k*T],[0,N(1.5*k*T,T)])
    plt.plot(Evalues,Nvalues)
    plt.plot(Evalues,N2values/(1.5*Q))#1.5*k*T scale ###
    plt.show()
    #'''
    #print(gate)
    print(Ecut/(1.5*k*T), Ecut/(k*T))
    x=integ(N,a,b,T)
    y=integ(N2,a,1.5*Q,T)
    z=integ(N2,1.5*Q,b*5,T)
    w=y+z
    x2=integ(N,a,b*1.2,T)
    print(y/AN/E,z/AN/E)
    print(1.5*k*T*AN) # temperature in J/mol in theory
    print(w/AN)
    print(w/x) # temperature in J/particle
    print(w/x*AN) # temperature in J/mol according to M-B distribution
    print(w/x*AN/T) # conversion factor, c, from Kelvin to J/mol, where 1K*c=1J/mol
    print(1.5*Q*AN/T) #Q scales with T. If we did not know Q, or how Q scaled with T, this output would still be equal to the conversion factor
    #                  Also, if Q scales with T by Q=qT, the conversion factor is just 1.5*q*AN
    q=Q/T
    print(1.5*q*AN) # conversion factor. q is arbitrary, but the conversion factor is not. Because of the set conversion factor in reality, q=k.
    print(x, w)
    N3values=zeros(Npt,float)
    '''
    N3values[0]=0
    for i in range(1,Npt):
        N3values[i]=N2values[i]/Nvalues[i] #Nvalues should instead be the integral of Nvalues (&same with N2??)
    plt.plot(Evalues,N3values)
    plt.show()
    '''
    return x,x2
    #print(Evalues)
    #print(Nvalues)
    
x,x2=graph()
print(x)
print(x/AN)
print((1-(x/AN))*100,'%',AN-x)
print((1-(x/Nt))*100,'%',Nt-x)
print((1-(x2/Nt))*100,'%',Nt-x2)

