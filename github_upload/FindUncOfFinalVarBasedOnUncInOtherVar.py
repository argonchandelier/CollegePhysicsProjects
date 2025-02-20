# Logan Richan
# Ph150 assignment

from math import sqrt

l1=18.9
w1=19
h1=47.1
m1=149.6

unc=0.1

l2=50.9
w2=19
h2=19
m2=162


def function(l,w,h,m,unc):
    uncF=sqrt((unc/(l*w*h))**2+(unc*(-m)/(l*w*(h**2)))**2+(unc*(-m)/(l*h*(w**2)))**2+(unc*(-m)/(h*w*(l**2)))**2)
    return uncF
    
def function2(l,w,h,m):
    a=m/(l*w*h)
    return a
    
x1=function2(l1,w1,h1,m1)
y1=function2(l2,w2,h2,m2)
    
x2=function(l1,w1,h1,m1,unc)
y2=function(l2,w2,h2,m2,unc)

print(x1,x2)
print(y1,y2)

print(x1-x2)
print(y1+y2)