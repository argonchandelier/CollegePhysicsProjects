from math import pi
from datetime import datetime

start=datetime.now()

G = 6.67e-11 #m^3 kg^-1 s^-2
M = 5.97e24 #kg
R = 6371000.0 #m

T = float(input("input the period in seconds: "))

afterInput=datetime.now()

h = (G*M*(T**2.)/(4.*((pi)**2.)))**(1./3.) - R

# Alters based on input
print ("Altitude is ", h, " meters and ", h/1000, " km.")

# runs for 2 numbers: T = 5400 & 2400
for T in [90.*60., 40.*60.]:
    h = (G*M*(T**2.)/(4.*((pi)**2.)))**(1./3.) - R
    print ("Altitude is ", h, " meters and ", h/1000, " km.")
    
print(datetime.now()-afterInput)
