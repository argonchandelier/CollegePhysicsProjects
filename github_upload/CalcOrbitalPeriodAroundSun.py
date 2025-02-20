# Logan Richan
# ph295

from math import pi

print("distance to Sun at perihelion:")
l1 = float(input())

print("velocity at perihelion:") #closest point
v1 = float(input())

G=6.6738e-11
M=1.9891e30 # mass of sun

v2 = float((G*M/(v1*l1)) - 0.5*(( ((4.*(G**2.)*(M**2.))/((v1**2)*(l1**2))) +4*(v1**2)-(8*G*M/l1))**(1./2.)))

l2=l1*v1/v2

a=0.5*(l1+l2)
#print(v2)######
b=(l1*l2)**(0.5)

T=2*pi*a*b/(l1*v1)
e=(l2-l1)/(l2+l1)

# Problematic if v2 is negative
#print(l1, l2, (l1*l2)**0.5)
#print(a, b, l1, v1)
print("l2, v2, T, e = ", l2, v2, T, e)
print("time in years = ", T/31536000.)
