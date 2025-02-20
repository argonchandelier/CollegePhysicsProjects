from matplotlib import pyplot as plt
from numpy import linspace, sin, pi

Time = [  0.6,   0.7,   0.8,   1.6,   1.7,   3.6,   3.7,   4.6,
          4.7,   4.8,   5.6,   5.7,   5.8,   6.6,   6.7,   7.7, 
          7.8,   8.6,   8.7,   8.8,   9.6,   9.7,   9.8,  10.6, 
         10.7,  10.8,  11.7,  11.8,  12.6,  12.7,  13.6,  13.7] # in Julian Days
v    = [-20.2, - 8.1,   5.6,  56.4,  66.8, -35.1, -42.6, -33.5,
        -27.5, -22.7,  45.3,  47.6,  56.2,  65.3,  62.5, -22.6,
        -31.7, -44.1, -37.1, -35.3,  25.1,  35.7,  41.2,  61.3,
         56.9,  51.0, - 2.5, - 4.6, -38.5, -48.7,   2.7,  17.6] # velocity in m/s

plt.plot(Time, v, '.')

plt.xlabel("Time in days")
plt.ylabel("radial velocity in m/s")
plt.title("51 Pegasi b")

plt.xlim(0,14)
plt.ylim(-70,70)




x = linspace(0,14,200)
y = 70*sin(1.49*x-1.3)
plt.plot(x,y)
print(2*pi/1.49)


plt.show()
