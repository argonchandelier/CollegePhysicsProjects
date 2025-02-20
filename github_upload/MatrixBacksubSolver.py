# Logan Richan
# Matrix Backsubstitution Solver - Assignment

from numpy import array,empty

A=array([[3,2,3,4],[3,29,13,3],[5,3,7,5],[4,7,2,9]],float)

v=array([5,3,8,6],float)
N=len(v)

#Gaussian elimination
def GaussElim(A,b):
    N=len(b)
    for m in range(N):
        div=A[m,m]
        A[m,:] /= div
        b[m] /= div
        
        for i in range(m+1,N):
            mult = A[i,m]
            A[i,:] -= mult*A[m,:]
            b[i] -= mult*b[m]
    return A,b

#print(A)

#Backsubstitution

def backsub(A,b):
    N=len(b)
    x=empty(N,float)
    for m in range(N-1,-1,-1):
        x[m]=b[m]
        for i in range(m+1,N):
            x[m]-=A[m,i]*x[i]
    return x

def LinEqSystemSolve(A,b):
    A,b=GaussElim(A,b)
    x=backsub(A,b)
    return x

x=LinEqSystemSolve(A,v)

print(x)

#from numpy.linalg import solve
#x=solve(A,v)
