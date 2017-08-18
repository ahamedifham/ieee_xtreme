import sys
lines=[]
linesToPrint=[]
for line in sys.stdin:
    linesToPrint.append(line.strip('\n'))
    lines.append(line.split())
base=int(lines[0][0])
symbols=list(lines[0][1])
no1=list(lines[1][0])
symbolicDic={}
no2=list(lines[2][0][1:])
if(len(no2)==0):
    no2=list(lines[2][1])
no1Reversed=list(reversed(no1))
no2Reversed=list(reversed(no2))

for i in range(0,len(symbols)):
    symbolicDic[symbols[i]]=i

no1DecimalValue=0
no1DecimalValueArray=[]
for j in range(0, len(no1)):
    no1DecimalValue= no1DecimalValue + symbolicDic[no1Reversed[j]]*pow(base,j)
    no1DecimalValueArray.append(symbolicDic[no1Reversed[j]]*pow(base,j))

no2DecimalValue=0
no2DecimalValueArray=[]
for l in range(0, len(no2)):
    no2DecimalValue= no2DecimalValue + symbolicDic[no2Reversed[l]]*pow(base,l)
    no2DecimalValueArray.append(symbolicDic[no2Reversed[l]]*pow(base,l))


if(len(no1DecimalValueArray)>len(no2DecimalValueArray)):
    diff= len(no1DecimalValueArray)-len(no2DecimalValueArray)
    for k in range(0,diff):
        no2DecimalValueArray.append(0)
elif(len(no2DecimalValueArray)>len(no1DecimalValueArray)):
    diff= len(no2DecimalValueArray)-len(no1DecimalValueArray)
    for k in range(0,diff):
        no1DecimalValueArray.append(0)

remainder=0
tempValue=0
sumInDecimal=[]
sumInDigits=[]

for m in range(0, len(no1DecimalValueArray)):
    comparator = pow(base,m+1)
    tempValue = no1DecimalValueArray[m] + no2DecimalValueArray[m] + remainder
    remainder=0
    if(tempValue>=comparator):
        remainder=comparator
        tempValue=tempValue-comparator
    sumInDecimal.append(tempValue)
    sumInDigits.append(tempValue/(pow(base,m)))

sumInDigitsRightOrder = list(reversed(sumInDigits))


finalOutput=[]
for n in range(0, len(sumInDigitsRightOrder)):
    temp = symbolicDic.keys()[symbolicDic.values().index(sumInDigitsRightOrder[n])]
    finalOutput.append(temp)
# print linesToPrint
linesToPrint.pop()
for tempLine in linesToPrint:
    print tempLine
print '',''.join(finalOutput)
