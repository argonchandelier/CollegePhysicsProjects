# Logan Richan
# ph336

from numpy.random import random, uniform
from matplotlib import pyplot as plt
from matplotlib.patches import Rectangle

plt.close('all')

nmax=100000

rangex=2.0
rangey=1.0
rangez=1.0
x=[uniform(0,rangex) for i in range(nmax)]
y=[uniform(0,rangey) for j in range(nmax)]
z=[uniform(0,rangez) for k in range(nmax)]

Vx2=[0,1.9]
Vy2=[0.1,0.9]
Vz2=[0.1,0.5]

count1D,count2D,count3D=0,0,0
for l in range(nmax):
    if x[l] >= Vx2[0] and x[l] <= Vx2[1]:
        count1D += 1
        if y[l] >= Vy2[0] and y[l] <= Vy2[1]:
            count2D += 1
            if z[l] >= Vz2[0] and z[l] <= Vz2[1]:
                count3D += 1

print("Actual fraction in 1 dimension: " , count1D/float(nmax), " Expected Fraction: ", (Vx2[1]-Vx2[0]) / float(rangex))
print("Actual fraction in 2 dimensions: ", count2D/float(nmax), " Expected Fraction: ", (Vx2[1]-Vx2[0])*(Vy2[1]-Vy2[0]) / float(rangex*rangey))
print("Actual fraction in 3 dimensions: ", count3D/float(nmax), " Expected Fraction: ", (Vx2[1]-Vx2[0])*(Vy2[1]-Vy2[0])*(Vz2[1]-Vz2[0]) / float(rangex*rangey*rangez))

fig = plt.figure() # automatically sets a new figure
fig.gca(projection='3d')
plt.plot(x,y,z,'.r')
plt.plot([Vx2[0],Vx2[0],Vx2[1],Vx2[1],Vx2[0],Vx2[0],Vx2[0],Vx2[0],Vx2[0],Vx2[1],Vx2[1],Vx2[1],Vx2[1],Vx2[1],Vx2[1],Vx2[0]],
         [Vy2[0],Vy2[1],Vy2[1],Vy2[0],Vy2[0],Vy2[0],Vy2[1],Vy2[1],Vy2[1],Vy2[1],Vy2[1],Vy2[1],Vy2[0],Vy2[0],Vy2[0],Vy2[0]],
         [Vz2[0],Vz2[0],Vz2[0],Vz2[0],Vz2[0],Vz2[1],Vz2[1],Vz2[0],Vz2[1],Vz2[1],Vz2[0],Vz2[1],Vz2[1],Vz2[0],Vz2[1],Vz2[1]],'b')
plt.plot([     0,     0,rangex,rangex,     0,     0,     0,     0,     0,rangex,rangex,rangex,rangex,rangex,rangex,     0],
         [     0,rangey,rangey,     0,     0,     0,rangey,rangey,rangey,rangey,rangey,rangey,     0,     0,     0,     0],
         [     0,     0,     0,     0,     0,rangez,rangez,     0,rangez,rangez,     0,rangez,rangez,     0,rangez,rangez],'k')
#plt.axis('equal')
plt.show()
