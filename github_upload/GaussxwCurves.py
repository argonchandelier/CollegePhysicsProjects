# Logan Richan
# ph295

from datetime import datetime
from gaussxw import gaussxw
import matplotlib.pyplot as plt

start=datetime.now()

N1=10
N2=100
x,w=gaussxw(N1)
x2,w2=gaussxw(N2)

plt.figure(1)

plt.subplot(121)
plt.bar(x,w,.3) #location, weight, scale
plt.xlabel("x")
plt.ylabel("y")

plt.subplot(122)
plt.bar(x2,w2,.03)
plt.xlabel("x")
plt.ylabel("y")

plt.show()

print(x,w)