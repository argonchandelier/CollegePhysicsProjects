# Logan Richan
# ph295

from random import randrange
from numpy import zeros, arange
from matplotlib import pyplot as plt
import numpy as np
freq=zeros(11,int)
freqExp=zeros(11,float)
numRolls=int(1e5)

index=PossibleNums=arange(2,13)
bar_width=0.4


'''
rolls=zeros(numRolls, int)
rollsExp=zeros(numRolls, int)
'''
#expected
for i in range(6):
    freqExp[i]=freqExp[10-i]=float(numRolls)/36.*(i+1)
'''
k=0
for i in range(11):
    for j in range(int(freqExp[i])):
        rollsExp[k]=i+2
        k+=1
'''
#experiment
for i in range(numRolls):
    a=randrange(6)+1
    b=randrange(6)+1
    t=a+b
    for j in range(2,12+1):
        if t==j:
            freq[j-2]+=1
    #rolls[i]=t ###

print(freq)
print(freqExp)

'''
#plt.hist(rolls, 11)
plt.hist([rolls,rollsExp], 11)
#plt.xlim(2,12)
#plt.hist(range(2,13),freq)
#plt.hist([freq,freqExp], 11, label=['Rolled frequencies','Expected Frequencies'])
#plt.hist(freq, 11, alpha=0.5, label='x')
#plt.hist(freqExp, 11, alpha=0.5, label='y')

#plt.ylabel("Frequencies")
#plt.xlabel("Dice Number")
plt.show()

'''
#plt.bar(0.35+index, data_prob, bar_width)
rects1 = plt.bar(index + 0.2, freq, bar_width,
#alpha=opacity,
color='b',
label='Rolled frequencies')
 
rects2 = plt.bar(index + bar_width + 0.2, freqExp, bar_width,
#alpha=opacity,
color='g',
label='Expected Frequencies')

plt.xticks(index + bar_width, ('2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'))
plt.show()

plt.xticks(index + bar_width, ('2', '3', '4', '5', '6', '7', '8', '9', '10', '11', '12'))