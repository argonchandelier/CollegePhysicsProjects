# Logan Richan
# ph295

#relaxation; binary search; Newton's methods
from math import exp

errorMax=10**-6
count1=0
count2=0
count3=0

#FUNCTION
def f(x):
    return 5*exp(-x)+x-5

#BINARY SEARCH METHOD
err=1
a=ainitial=3
b=binitial=10
br=0

while abs(err)>errorMax:
    if f(a)==0:
        x=a
        err=errorMax
    elif f(b)==0:
        x=b
        err=errorMax
    elif f(a)*f(b)<0:
        x=.5*(a+b)
        if f(x)==0:
            err=errorMax
        elif f(x)*f(a)<0:
            b=x
            err=x-a
        else:
            a=x
            err=b-x
    else:
        print("No single root in range")
        break
    count1+=1

print('Binary Search Method: root: ', x, 'error: ', err, "a & b: ", ainitial, binitial, "Count: ", count1)

#NEWTON'S METHOD
def df(x):
    return -5*exp(-x)+1

x=xinitial=10
tol=1e-6
err=1

while abs(err)>tol:
    y=x
    x=x-f(x)/df(x)
    err=y-x
    count2+=1
print("Newton's Method: root: ", x, 'error: ', err, "x initial: ", xinitial, "Count: ", count2)

#RELAXATION METHOD
tol=1e-6
err=1
x=xinitial=1
while err>tol:
    x2=5-5*exp(-x)
    err=x2-x
    x=x2
    count3+=1
print('Relaxation Method: root: ', x, 'error: ', err, "x initial: ", xinitial, "Count: ", count3)
