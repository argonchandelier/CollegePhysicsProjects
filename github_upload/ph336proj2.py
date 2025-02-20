# Logan Richan
# ph336

import xlrd
from numpy import array
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
# Use local kernal
######################################################### OLD
plt.close('all')

experiment=3
print("Experiment #" + str(experiment))
plt.title("Experiment #" + str(experiment))
#plt.xlabel("wavelengths in nm")
#plt.ylabel("Intensity")

loc = ("ph336FinalProj.xlsx")
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(experiment)

wavelengths = array(sheet.col_values(0))

def TotalLum(a):
    return sum((wavelengths[1:]-wavelengths[:-1])*(a[1:]+a[:-1])/2.)

def xx(x):
    return x**2



led = array(sheet.col_values(2))
tube = array(sheet.col_values(3))
soft = array(sheet.col_values(4))
helix = array(sheet.col_values(5))

H = array(sheet.col_values(7))
Hg = array(sheet.col_values(8))
Xe = array(sheet.col_values(9))
Ne = array(sheet.col_values(10))
He = array(sheet.col_values(11))

sources = array([led, tube, soft, helix, H, Hg, Xe, Ne, He])
sourcesNames = ["led", "tube", "soft", "helix", "H", "Hg", "Xe", "Ne", "He"]
sourcesLum = [TotalLum(sources[0]), TotalLum(sources[1]), TotalLum(sources[2]), TotalLum(sources[3]), TotalLum(sources[4]), TotalLum(sources[5]), TotalLum(sources[6]), TotalLum(sources[7]), TotalLum(sources[8])]

def fit2(x,a,b):
    return (a*dataA + b*dataB)
guess2=[1,1]

def fit3(x,a,b,c):
    return (a*dataA + b*dataB + c*dataC)
guess3=[1,1,1]

def fit4(x,a,b,c,d):
    return (a*dataA + b*dataB + c*dataC + d*dataD)
guess4=[1,1,1,1]

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

trials = array([trial1, trial2, trial3, trial4, trial5, trial6, trial7])
trialsl = array([trial1l, trial2l, trial3l, trial4l, trial5l, trial6l, trial7l])
sourcesPerTrial = array([2,2,2,3,3,3,4])
trialSources = [[0,1],[1,3],[2,8],[0,2,8],[1,2,7],[1,3,4],[1,2,3,4]] # Trial 1&2
#trialSources = [[0,1],[1,3],[0,8],[0,2,8],[1,2,7],[2,3,4],[1,2,3,4]] # Trial 3


background = array(sheet.col_values(28))

### Put into a loop and return best fit w/ vars closeness, fitParams, & expec ###
# Try every combination of ogData: (9+1)!/((2!)*(9+1-2)!) = 9+8+7+... = 45

def findBest(trialNum,doPlot=False): # only 2 for now
    #combData(tube, led) # right
    #combData(tube, soft) # wrong
    #combData(helix, H) # wrong
    fit = fit2
    guess = guess2
    '''
    if sourcesPerTrial[trialNum-1] == 3:
        fit = fit3
        guess = guess3
    if sourcesPerTrial[trialNum-1] == 4:
        fit = fit4
        guess = guess4
    '''
    
    fitBest = None
    expectBest = None
    closenessBest = 10e100
    sourcesBest = None
    for i in range(len(sources)):
        for j in range(len(sources)):
            if i < j:
                combData(sources[i],sources[j])
                
                fitT,error=curve_fit(fit,wavelengths,trials[trialNum-1],p0=guess)
                expectT=fit2(wavelengths,*fitT)
                closenessT = sum((trials[trialNum-1] - expectT)**2)
                if closenessT < closenessBest:
                    fitBest, expectBest, closenessBest = fitT, expectT, closenessT
                    sourcesBest = [i, j]
    print(sourcesNames[sourcesBest[0]], sourcesNames[sourcesBest[1]])
    print("closenessBest", closenessBest)
    
    plt.plot(wavelengths, expectBest, '--r')
    plt.plot(wavelengths, trials[trialNum-1], 'b')



def actualFit(trialNum):    
    #plt.figure(2)
    
    if sourcesPerTrial[trialNum-1] == 3:
        fit = fit3
        guess = guess3
    if sourcesPerTrial[trialNum-1] == 4:
        fit = fit4
        guess = guess4
    
    combData(sources[trialSources[trialNum-1][0]], sources[trialSources[trialNum-1][1]])
    #combData(tube, led) # right T1
    #combData(tube, soft) # wrong
    #combData(helix, H) # wrong
    
    fitT,error=curve_fit(fit2,wavelengths,trials[trialNum-1],p0=guess2)#######
    expecT=fit2(wavelengths,*fitT)
    plt.plot(wavelengths, expecT, '--r')
    plt.plot(wavelengths, trials[trialNum-1], 'b')
    
    closenessT = sum((trials[trialNum-1] - expecT)**2)
    print(sourcesNames[trialSources[trialNum-1][0]], sourcesNames[trialSources[trialNum-1][1]])
    print(fitT)
    print("closenessActual", closenessT)

z=5
findBest(z,doPlot=True)
plt.figure(2)
actualFit(z)
    

#plt.figure(3)
'''
plt.plot(wavelengths, tube*4.5)
plt.plot(wavelengths, soft)
'''
#plt.plot(wavelengths, led)
#plt.plot(wavelengths, helix*2.5)


'''
plt.plot(wavelengths, trial1l-trial1, 'r', label='Trial 1 Background Light')
plt.plot(wavelengths, trial2l-trial2, 'b', label='Trial 2 Background Light')
plt.plot(wavelengths, trial3l-trial3, 'g', label='Trial 3 Background Light')
plt.plot(wavelengths, trial4l-trial4, 'c', label='Trial 4 Background Light')
plt.plot(wavelengths, trial5l-trial5, 'm', label='Trial 5 Background Light')
plt.plot(wavelengths, trial6l-trial6, color = '#ff7f0e', label='Trial 6 Background Light')
plt.plot(wavelengths, trial7l-trial7, color = '#9467bd', label='Trial 7 Background Light')#, linewidth=0.3)

plt.plot(wavelengths, background, '--k', label='Actual Background Light', linewidth=3.0)

plt.plot(wavelengths, helix*0.1, color = '#888888', label='Helix Light', linewidth=3.0)
'''

plt.legend()
plt.show()
print("done")