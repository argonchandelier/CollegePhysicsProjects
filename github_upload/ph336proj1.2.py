# Logan Richan
# ph336

import xlrd
from numpy import array
from matplotlib import pyplot as plt
from scipy.optimize import curve_fit
# Use local kernel

# Close all previous lots
plt.close('all')

experiment=3
print("Experiment #" + str(experiment))
plt.title("Experiment #" + str(experiment))

# Get data from Excel
loc = ("ph336FinalProj.xlsx")
wb = xlrd.open_workbook(loc) 
sheet = wb.sheet_by_index(experiment)

################ Define Functions ###################
def TotalLum(a):
    return sum((wavelengths[1:]-wavelengths[:-1])*(a[1:]+a[:-1])/2.)

def fit2(x,a,b):
    return (a*dataA + b*dataB)
guess2=[1,1]

def fit3(x,a,b,c):
    return (abs(a)*dataA + abs(b)*dataB + c*dataC)
guess3=[0.1,1,1]

def fit4(x,a,b,c,d):
    return (abs(a)*dataA + abs(b)*dataB + abs(c)*dataC + abs(d)*dataD)
#guess4=[0.3, 0.04, 1., 0.5]
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

# fit data to given sources; called by the finding best fit and finding actual fit functions below
def Fit(fit,guess,trialNum,i,j,k=None,l=None):
    combData(sources[i],sources[j],C=k,D=l)
                
    fitT,error=curve_fit(fit,wavelengths,trials[trialNum-1],p0=guess)
    expectT=fit(wavelengths,*fitT)
    closenessT = sum((trials[trialNum-1] - expectT)**2)
    #print("closenessAct2:",sum(abs(trials[trialNum-1] - expectT)))
    
    return fitT, expectT, closenessT

def findBest(trialNum,doPlot=False): # only 2 for now
    #combData(tube, led) # right
    #combData(tube, soft) # wrong
    #combData(helix, H) # wrong
    fit = fit2
    guess = guess2
    l=2
    '''
    if sourcesPerTrial[trialNum-1] >= 3:
        fit = fit3
        guess = guess3
        l=3
    if sourcesPerTrial[trialNum-1] >= 4:
        fit = fit4
        guess = guess4
        l=4
    '''
    
    fitBest = None
    expectBest = None
    closenessBest = 10e100
    sourcesBest = None
    if l == 2:
        for i in range(len(sources)):
            for j in range(len(sources)):
                if i < j:
                    '''
                    combData(sources[i],sources[j])
                    
                    fitT,error=curve_fit(fit,wavelengths,trials[trialNum-1],p0=guess)
                    expectT=fit2(wavelengths,*fitT)
                    closenessT = sum((trials[trialNum-1] - expectT)**2)
                    '''
                    fitT, expectT, closenessT = Fit(fit,guess,trialNum,i,j)
                    if closenessT < closenessBest:
                        fitBest, expectBest, closenessBest = fitT, expectT, closenessT
                        sourcesBest = [i, j]
    if l == 3:
        for i in range(len(sources)):
            for j in range(len(sources)):
                for k in range(len(sources)):
                    if i < j and j < k:
                        fitT, expectT, closenessT = Fit(fit,guess,trialNum,i,j,k=k)
                        if closenessT < closenessBest:
                            fitBest, expectBest, closenessBest = fitT, expectT, closenessT
                            sourcesBest = [i, j]
                        
    print(sourcesNames[sourcesBest[0]], sourcesNames[sourcesBest[1]])
    print("closenessBest", closenessBest)
    
    plt.plot(wavelengths, expectBest, '--r')
    plt.plot(wavelengths, trials[trialNum-1], 'b')
    plt.xlabel("Wavelengths")
    plt.ylabel("Relative Intensity")

def actualFit(trialNum):    
    #plt.figure(2)
    plt.xlabel("Wavelengths")
    plt.ylabel("Relative Intensity")
    
    fit = fit2
    guess = guess2
    ci=None
    di=None
    if sourcesPerTrial[trialNum-1] >= 3:
        fit = fit3
        guess = guess3
        ci = trialSources[trialNum-1][2]
        #c = sources[ci]
    if sourcesPerTrial[trialNum-1] >= 4:
        fit = fit4
        guess = guess4
        di = trialSources[trialNum-1][3]
        #d = sources[di]
    
    '''
    combData(sources[trialSources[trialNum-1][0]], sources[trialSources[trialNum-1][1]], C=c, D=d)
    #combData(tube, led) # right T1
    #combData(tube, soft) # wrong
    #combData(helix, H) # wrong
    
    fitT,error=curve_fit(fit,wavelengths,trials[trialNum-1],p0=guess)#######
    expecT=fit(wavelengths,*fitT)
    '''
    fitT, expectT, closenessT = Fit(fit,guess,trialNum,trialSources[trialNum-1][0],trialSources[trialNum-1][1],k=ci,l=di)
    
    plt.plot(wavelengths, expectT, '--r', label='Fit using fit function lin. comb. consts.')
    plt.plot(wavelengths, trials[trialNum-1], 'b', label='Trial Data')
    
    #closenessT = sum((trials[trialNum-1] - expecT)**2)
    sourceNames = str(sourcesNames[trialSources[trialNum-1][0]]) + " & " + str(sourcesNames[trialSources[trialNum-1][1]])
    if sourcesPerTrial[trialNum-1] >= 3:
        sourceNames += " & " + str(sourcesNames[trialSources[trialNum-1][2]])
    if sourcesPerTrial[trialNum-1] >= 4:
        sourceNames += " & " + str(sourcesNames[trialSources[trialNum-1][3]])
    print(sourceNames)
    print(fitT)
    #print("closenessActual", closenessT)

##################################################################

###################### Get Data ##################################
# Get wavelengths
wavelengths = array(sheet.col_values(0))

# Get source data
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

# Get trial data
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
trialSources = [[0,1],[1,3],[2,8],[0,2,8],[1,2,7],[1,3,4],[1,2,3,8]]

# Get background
background = array(sheet.col_values(28))

##### Plot all light data ###################################################
'''
plt.xlabel("Wavelengths")
plt.ylabel("Relative Intensity")

plt.plot(wavelengths, H,label='H')
plt.plot(wavelengths, He,label='He')
plt.plot(wavelengths, Ne,label='Ne')
plt.plot(wavelengths, Hg,label='Hg')
plt.plot(wavelengths, Xe,label='Xe')

plt.plot(wavelengths, helix,label='helix')
plt.plot(wavelengths, soft,label='soft')
plt.plot(wavelengths, tube,label='tube')
plt.plot(wavelengths, led,label='LED')
'''
######################################################################################

sourcesLum = [TotalLum(sources[0]), TotalLum(sources[1]), TotalLum(sources[2]), TotalLum(sources[3]), TotalLum(sources[4]), TotalLum(sources[5]), TotalLum(sources[6]), TotalLum(sources[7]), TotalLum(sources[8])]

#findBest(2,doPlot=True)
#actualFit(5)

'''
# Get graphs of all "actual" fits (lin combination of actual sources)
for i in range(len(trials)-1):
    plt.figure(i+1)
    actualFit(i+1)
'''

### Correct in prediction that mult. light sources measure badly ###
#'''
t=7
actualFit(t)
#a,b,c,d=0.3,0.04,1,0.5
#a,b,c,d=0.3, 0.06, 0.1, 0.9
a,b,c,d=0.46, 0.24, 0.6, 0.4
expect = a*tube + b*soft + c*helix + d*He
#expect=0.3*tube + 0.06*soft + 0.1*helix + 0.9*He
#expect=0.46*tube + 0.24*soft + 0.6*helix + 0.4*He
print("Manual relative intensity fit:", [a,b,c,d])
plt.plot(wavelengths, expect, '--k', label='Fit using self-chosen lin. comb. consts.')
#closeness = sum((trials[6] - expect)**2)
#closeness2 = sum(abs(trials[6] - expect))
#print(closeness)
#print(closeness2)
#'''
#####################################################################

### Plotting some sources to see what they look like ###
'''
plt.figure(3)
plt.xlabel("Wavelengths")
plt.ylabel("Relative Intensity")

plt.plot(wavelengths, He)
plt.plot(wavelengths, helix)
plt.plot(wavelengths, soft)
plt.plot(wavelengths, tube)

plt.plot(wavelengths, tube*4.5)
plt.plot(wavelengths, soft)

plt.plot(wavelengths, led)
plt.plot(wavelengths, helix*2.5)
'''
#########################################################

### Correct in prediction of background ###
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
############################################

plt.legend()
plt.show()
print("done")