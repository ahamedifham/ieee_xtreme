import sys
# def sendLoveNo(petals, notLove):
#     for petal in petals:
#         print petal,notLove
#         if(notLove==False):
#             notLove=True
#         elif(notLove==True):
#             notLove=False
#             petals.pop(petal)

    # print petals
    # print notLove
    # if (len(petals)==1):
    #     print petals
    #     return petals
    # elif(len(petals) !=1):
        # notLove=1
        # return sendLoveNo(petals,notLove)

def removekey(d, key):
    r = dict(d)
    del r[key]
    return r

lines=[]
for line in sys.stdin:
    lines.append(line)
testCases=int(lines[0])
for i in range(0, testCases):
    noOfPetals = int(lines[i+1])
    petals=[]
    for l in range(1,noOfPetals+1):
        petals.append(l)
    # print petals
    notLove= False
    # print petals
    petalDict = {}
    for petal in petals:
        petalDict[petal]=petal
    #print petalDict
    notLove= False
    while(len(petalDict)!=1):
        # for j in range(1,len(petalDict)+1):
        for key in petalDict:
            # if(len(petalDict)!=1):
            if(notLove==False):
                notLove=True
            elif(notLove==True):
                notLove=False
                petalDict = removekey(petalDict,key)
                    #print (petalDict)

    #print petalDict.keys()
    print ''.join(str(petalDict.keys()[0]))
