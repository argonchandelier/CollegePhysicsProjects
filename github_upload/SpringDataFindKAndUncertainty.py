# Logan Richan
# ph150

from numpy import std,array,size,sqrt,mean

g=9.8

###SPRING 1###
m1=.001*array([147.5,355.5,500,503,647.5,855.5,1000,1050,1355.5,1503],float) #in kg
x1=.01*array([56.3,62.9,67.6,67.7,71.7,78.7,82.9,84.3,93.8,99.1],float)-.515 #in cm


###SPRING 2###
m2=.001*array([147.5,355.5,500,503,647.5,855.5,1000,1050,1355.5,1503],float) #in kg
x2=.01*array([45.7,51.9,56.3,56.7,61.2,67.3,71.7,73.4,82.5,86.7],float)-.413 #in m


### k values ###
k1=m1*g/x1 #in N/m
k2=m2*g/x2

print(k1,k2)






mean1=mean(k1)
mean2=mean(k2)

N1=size(k1)
N2=size(k2)

std1=std(k1)
std2=std(k2)

uncertaintyk1=std1/sqrt(N1)
uncertaintyk2=std2/sqrt(N2)

print("k1:", mean1, "+/-", uncertaintyk1)
print("k2:", mean2, "+/-", uncertaintyk2)
