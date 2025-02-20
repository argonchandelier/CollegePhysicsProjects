# Logan Richan
# ph336

import xlrd
from numpy import array
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
# Use local kernal

loc = ("ph336FinalProj.xlsx")
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(1)

wavelengths = array(sheet.col_values(0))

def TotalLum(a):
    return sum((wavelengths[1:]-wavelengths[:-1])*(a[1:]+a[:-1])/2.)



led = array(sheet.col_values(2))
tube = array(sheet.col_values(3))
soft = array(sheet.col_values(4))
helix = array(sheet.col_values(5))

H = array(sheet.col_values(7))
Hg = array(sheet.col_values(8))
Xe = array(sheet.col_values(9))
Ne = array(sheet.col_values(10))
He = array(sheet.col_values(11))

def fit2(x,a,b):
    return (a*dataA + b*dataB)
guess2=[1,1]

def fit3(x,a,b,c):
    return (a*dataA + b*dataB + c*dataC)
guess3=[1,1,1]

dataA = None
dataB = None
dataC = None
dataD = None
def combData(A,B,C=None,D=None):
    global dataA
    global dataB
    global dataC
    global dataD
    dataA = A
    dataB = B
    dataC = C
    dataD = D    

trial1 = array(sheet.col_values(13))
trial1l = array(sheet.col_values(14))
trial2 = array(sheet.col_values(15))
trial2l = array(sheet.col_values(16))
trial3 = array(sheet.col_values(17))
trial3l = array(sheet.col_values(18))
trial4 = array(sheet.col_values(19))
trial4l = array(sheet.col_values(20))
trial5 = array(sheet.col_values(21))
trial5l = array(sheet.col_values(22))
trial6 = array(sheet.col_values(23))
trial6l = array(sheet.col_values(24))
trial7 = array(sheet.col_values(25))
trial7l = array(sheet.col_values(26))

background = array(sheet.col_values(28))

### Put into a loop and return best fit w/ vars closeness, fitParams, & expec ###
# Try every combination of ogData: (9+1)!/((2!)*(9+1-2)!) = 9+8+7+... = 45

#combData(tube, led) # right
#combData(tube, soft) # wrong
combData(helix, H) # wrong

fitT1,error=curve_fit(fit2,wavelengths,trial1,p0=guess2)#######
expecT1=fit2(wavelengths,*fitT1)
plt.plot(wavelengths,expecT1,'--r')
plt.plot(wavelengths, trial1, 'b')

closenessT1 = sum((trial1 - expecT1)**2)

#################################################################################

print("closenessT1", closenessT1)

'''
plt.plot(wavelengths, trial1l-trial1, 'r', label='Trial 1 Background Light')
plt.plot(wavelengths, trial2l-trial2, 'b', label='Trial 2 Background Light')
plt.plot(wavelengths, trial3l-trial3, 'g', label='Trial 3 Background Light')
plt.plot(wavelengths, trial4l-trial4, 'c', label='Trial 4 Background Light')
plt.plot(wavelengths, trial5l-trial5, 'm', label='Trial 5 Background Light')
plt.plot(wavelengths, trial6l-trial6, color = '#ff7f0e', label='Trial 6 Background Light')
plt.plot(wavelengths, trial7l-trial7, color = '#9467bd', label='Trial 7 Background Light', linewidth=0.3)
plt.plot(wavelengths, background, '--k', label='Actual Background Light', linewidth=3.0)
plt.plot(wavelengths, helix*0.1, color = '#888888', label='Helix Light', linewidth=3.0)
'''

plt.legend()
plt.show()
print("done")