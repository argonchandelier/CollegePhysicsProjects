# Logan Richan
# ph295

from random import random
from numpy import zeros
from matplotlib import pyplot as plt

def shift(): # Shift the ball to the left or right pin
    x = random()
    if x<0.5:
        return -0.5
    else:
        return 0.5

N=100000
place=zeros(7,int) # Stores the number of balls in each bin

for i in range(N): # Droping each ball
    ball=0
    for j in range(6): # Shift the ball 6 times
        ball+=shift()
    place[int(ball+3)]+=1 # Store ball in appropriate bin

print(place)
for i in range(-3,4): # Plot each bin with its balls
    rect=plt.bar(i, place[i+3], 0.5)

plt.xlabel("Bin")
plt.ylabel("Number of balls")
plt.show()
