from math import*
import sys

def primeFactors(n):
    x=[1]
    while(n%2==0):
        x.append(2)
        n=n/2


    for i in range(3,int(sqrt(n))+1):
        while(n%i == 0):
            x.append(i)
            n=n/i

    if(n>2):
        x.append(n)

    return x


lines=[]
totalOutput=[]
for line in sys.stdin:
    lines.append(line)
line1=lines[0].split()
testCases = int(line1[0])
for j in range(1, testCases+1):
    tempLine = lines[j].split()
    n=int(tempLine[0])
    a=int(tempLine[1])
    b=int(tempLine[2])
    initiSet=[]
    y=divisorGen(n)
    for k in range(a,b):
        temp=divisorGen(k)
        #print temp
        commonSet = set(temp) & set(y)
        if (commonSet==set([1])):
            # print commonSet
            initiSet.append(k)

    #print initiSet

    finalOutput = sum(initiSet)%1000000007
    totalOutput.append(finalOutput)

for l in totalOutput:
    print l
