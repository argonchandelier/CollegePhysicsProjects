# Logan Richan
# ph295

from numpy import zeros
from math import sqrt

k=8.99e9
q=4.23e-9

E_field=zeros([7,7], float)

#get distance
def distance(x,y):
    r=sqrt(x**2+y**2)
    return r

#get E_field
def magnitude(r):
    if r!=0:
        E=k*q/(r**2)
    else:
        E=0
        
    return round(E,0)
    
#iterate to find the field for each point
for i in range(7):
    x=(-6. + 2.*i)/100.
    for j in range(7):
        y=(-6. + 2.*j)/100.
        r=distance(x,y)
        E_field[i,j]=magnitude(r)
        
print(E_field)