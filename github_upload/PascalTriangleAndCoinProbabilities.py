# Logan Richan
# ph295
# In-class assignment4

from numpy import zeros

#Part a
def fact(a): #calculaion of factorials of a given input number
    product=1
    if a==0:
        return 1
    for i in range(1,a+1):
        product*=i
    return product

def binomial(n,k): #calculation of binomial coefficient with n choose k
    coeff=fact(n)/(fact(k)*fact(n-k))
    return (int(coeff))
    
    
#Part b
numLines=20 #number of lines of Pascal's triangle to be printed
for i in range(1,numLines+1): #line by line calculating loop of a row of Pascal's triangle
    b=i+1
    line=zeros(b,int)
    for j in range(1,b+1):
        line[j-1]=binomial(i,j-1)
    print(line) #prints 20 (or whatever "numLines" is) times, 1 for each line to form Pascal's triangle
    
    
#Part c, calculation a
n=100 #number of times a coin is flipped
k=60 #number of times a coin lands on heads

def prob(n,k): #calculator of probability a coin lands on heads k times for n flips
    p=float(binomial(n,k)/(2.**n))
    return p
    
p=prob(n,k)
print("Probability a coin lands on", k, "heads with", n, "flips:", p)

#part c, calculation b
sum=0
for i in range(k,n+1): #calculator of a probability a coin lands on heads k times or more for n flips
    sum+=prob(n,i)
    
print("Probability a coin lands on", k, "heads or more with", n, "flips:", sum)