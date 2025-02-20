# Logan Richan
# ph295

from numpy import empty, zeros, max
from pylab import imshow, gray, show, jet, colorbar
from datetime import datetime

start=datetime.now()

M=40
V=1.0
errMax=1e-6

phi = zeros([M+1,M+1], float)
phi[0,:]=phi[M,:]=V
#phiprime = empty([M+1, M+1], float)

delta = 1.
for k in range(90):
    delta=0.0 ###
    for i in range(M+1):
        for j in range(M+1):
            #
            err=1.0
            #while err>errMax:
            for l in range(1):
                oldphi=phi[i,j]
                if i!=0 and j!=0 and i!=M and j!=M:
                    if k>M-1:
                        k=M-1
                    #k=35
                    if i!=M-k+1 and j!=M-k+1:
                        phi[i,j] = 0.5*(phi[i+1,j] + phi[i-1,j] )#+ phi[i,j+1] + phi[i,j-1])
                    else:
                        phi[i,j] = 0.25*(phi[i+1,j] + phi[i-1,j] + phi[i,j+1] + phi[i,j-1])
                err= abs(phi[i,j]-oldphi)
                
                #'''
                if err>delta:
                    delta=err
                #'''
            #
        '''
        if i==0 or j==0 or i==M or j==M:
            phiprime[i,j] = phi[i,j]
        else:
            phiprime[i,j] = 0.25*(phi[i+1,j] + phi[i-1,j] + phi[i,j+1] + phi[i,j-1])
delta = max(abs(phi-phiprime))
phi,phiprime=phiprime,phi
'''
imshow(phi)
jet()
colorbar()
show()
print(datetime.now()-start)
