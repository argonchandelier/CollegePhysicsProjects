# Logan Richan
# ph336

import numpy as np
from scipy.optimize import curve_fit
from matplotlib import pyplot as plt

plt.close('all')

t = [10,20,30,40,50,60,70,80,90,100,110,120,130,140,150,160,170,180,190,200,210,220,230,240,250,260,270,280,290,300,\
310,320,330,340,350,360,370,380,390,400,410,420,430,440,450,460,470,480,490,500,510,520,530,540,550,560,570,580,590,600] 
counts = [792,811,716,690,714,625,628,616,605,567,496,459,508,493,447,367,407,367,420,353,371,324,313,328,270,270,248,267,242,230,212,225,\
209,201,205,157,199,124,160,162,141,145,139,133,122,112,131,120,107,98,83,108,96,89,118,84,81,70,76,65]

def f(x,halfL,A,k):
    return(A * 0.5**(x/float(halfL)) + k)

guess=[1,1,1]

fit,error=curve_fit(f,t,counts,p0=guess)

print(fit) # half life of 3.226 min, background = k = 45
print("errors:",np.sqrt(np.diag(error)))

plt.plot(t,counts,'ob')
X=np.linspace(10,600)
plt.plot(X,f(X,*fit),'--r')
plt.show()
