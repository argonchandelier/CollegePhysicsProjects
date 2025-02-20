#######################
# PH385
# Problem H3.4
# Logan Richan
########################
from numpy import pi, sinh, linspace

### a ###
#initialize variables
a=0
b=pi
N=500
dx=(b-a)/float(N)

x=linspace(a+dx/2.,b-dx/2.,N-1) # create a cell-center grid from a-b

### b ###
y=sinh(x)

### c ###
x_501=x[-1]+dx
y_501=sinh(b+dx/2.) # True value for parts c and d
y_ext_lin = 2*y[-1] - y[-2] # linear extrapolation
print(y_ext_lin, y_501) # value comparison

### d ###
y_ext_qud = y[-3] - 3*y[-2] + 3*y[-1] # quadratic extrapolation
print(y_ext_qud, y_501) # value comparison

### e ###
y_t=sinh(b-dx) # True value for parts e and f
y_int_lin = 0.5*y[-1] + 0.5*y[-2] # linear interpolation
print(y_int_lin, y_t) # value comparison

### f ###
y_int_qud = (1./8.) * (-y[-3] + 6*y[-2] + 3*y[-1]) # quadratic interpolation
print(y_int_qud, y_t) # value comparison

print(y[-3:]) # The last 3 y values for scale comparison