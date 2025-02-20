#############################
# Class Assignment PH150
# Logan Richan
#############################
from numpy import sqrt

# Function to calculate I
def f(F,r,t,w): 
    I = F*r*t/float(w)
    return I

# Given measured variables with their given uncertainties
Fm=10.
Func=0.3

rm=0.12
runc=0.005

tm=500./60.
tunc=1./6.

wm=6.
wunc=0.8

# Calculate I using the measured variables
I = f(Fm,rm,tm,wm)

#get the partial derivatives used in uncertainty calculation
df_dF = rm*tm/wm
df_dr = Fm*tm/wm
df_dt = Fm*rm/wm
df_dw = -Fm*rm*tm/(wm**2)

# Calculate the uncertainty of I
Iunc = sqrt((df_dF*Func)**2 + (df_dr*runc)**2 + (df_dt*tunc)**2 + (df_dw*wunc)**2)

# Print I with its computed uncertainty
print("The moment of Inertia is:",I, "+-", Iunc,'kg*m^2')