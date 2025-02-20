# Logan Richan
# ph295

from random import randrange
from numpy import zeros, arange
from matplotlib import pyplot as plt

freq=zeros(11,int)
freqExp=zeros(11,float)
numRolls=int(1e6)

#expected
for i in range(6):
    freqExp[i]=freqExp[10-i]=float(numRolls)/36.*(i+1)

#experiment
for i in range(numRolls):
    freq[randrange(6)+randrange(6)]+=1

print(freq)
print(freqExp)

index=PossibleNums=arange(2,13)
bar_width=0.4

rects1 = plt.bar(index + bar_width*0.5, freq, bar_width, color='b', label='Rolled frequencies')
rects2 = plt.bar(index + bar_width*1.5, freqExp, bar_width, color='g', label='Expected Frequencies')

plt.legend()
plt.xticks(index + bar_width, (range(2,13)))
plt.xlabel("Dice Roll Numbers")
plt.ylabel("Frequencies of Rolls")
plt.show()
