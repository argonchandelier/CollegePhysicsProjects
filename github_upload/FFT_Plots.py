# Logan Richan
# ph295

from numpy import zeros, array, pi, sin,cos,arange
from matplotlib import pyplot as plt

def ILeftGraph(f,a,b):
    N=20.
    h=(b-a)/N
    I=0
    for x in arange(a,b,h):
        y=f(x)
        I+=y*h
        plt.plot([x,x,x+h,x+h],[0,y,y,0])
    plt.show()
    return I

def graph(f,a,b):
    N=1000
    h=(b-a)/(N-1)
    xvalues=zeros(N,float)
    yvalues=zeros(N,float)
    i=0
    for x in arange(a,b+h,h):
        xvalues[i]=x
        yvalues[i]=f(x)
        i+=1
    plt.plot(xvalues,yvalues)
    plt.show()

def f(x):
    y=.1682*x**3-1.674*x**2+5.123*x-3.431
    return y

def problem1():
    answer=ILeftGraph(f,0,5.492)
    print(answer)
    graph(f,0,5.492)

#problem1()

'''
'''
'''
'''
from numpy.linalg import solve



def problem2():
    #Resistances in Ohms
    RAB=2
    RBC=3
    RCD=2
    RDE=1
    REF=4
    RFG=3
    RBF=5
    RCE=2
    
    Vt=12 # Voltage in V
    
    #Ax=b
    A = array([[(1./RAB)+(1./RFG), 1./RBF, 0,                0,      0           ],
               [(1./RAB)+(1./RFG), 0,     (1./RBC)+(1./REF), 1./RCE, 0           ],
               [(1./RAB)+(1./RFG), 0,     (1./RBC)+(1./REF), 0,      1./(RCD+RDE)],
               [1,                -1,     -1,                0,      0           ],
               [0,                 0,      1,               -1,     -1           ]], float)
    
    b = array([Vt, Vt, Vt, 0, 0], float)
    
    #print(A)
    #print(b)
    x = solve(A,b)
    print(x)

#problem2()

'''
'''
'''
'''
from numpy import loadtxt, copy
from numpy.fft import rfft, irfft

data=loadtxt("gravity_wave_data.txt")

#print(data)

N=1024
h=.5/(N-1)
tvalues=zeros(1024,float)
i=0
for t in arange(0,.5+h,h):
    tvalues[i]=t
    i+=1
plt.subplot(221)
plt.plot(tvalues, data)
plt.title("A")
#plt.show()

k = rfft(data)
f = abs(copy(k))/.5

plt.subplot(222)
plt.plot(f)
plt.title("b")
#plt.show()

'''
f2 = zeros(80-20+1,float)
i=0
for i2 in range(20,80+1):
    f2[i]=f[i2]
'''
f2 = copy(f)
for i in range(0,20):
    f2[i]=0
for i in range(80,int(1024/2)):
    f2[i]=0


plt.subplot(223)
plt.plot(f2)
plt.xlim(20,80)
plt.title("c")
#plt.show()

#k2 = copy(f2)*.5
cleanedData = irfft(f2)

plt.subplot(224)
plt.plot(tvalues, cleanedData)
plt.title("d")
plt.show()
