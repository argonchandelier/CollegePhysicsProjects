# Logan Richan
# ph385

from numpy import linspace, meshgrid, exp, cos
from matplotlib import pyplot as plt
from mpl_toolkits.mplot3d import Axes3D

a=0
b=2
Nx=30
x,dx=linspace(a,b,Nx,retstep=True)

c=-1
d=3
Ny=50
y,dy=linspace(c,d,Ny,retstep=True)

X,Y=meshgrid(x,y)
print(X)
print(Y)

z=exp(-(X**2 + Y**2)) * cos(5*(X**2 + Y**2)**(0.5))
print(z)

fig = plt.figure()
ax = fig.gca(projection='3d')
ax.plot_wireframe(X,Y,z)
plt.xlabel('x')
plt.ylabel('y')
plt.show()
