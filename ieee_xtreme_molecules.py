import sys
# atoms = [689187,1394824,851438]
sys.setrecursionlimit(pow(10,10))
lines=[]
for line in sys.stdin:
    lines.append(line)

line1=lines[0].split()
atoms=map(long,line1)

noOfCAtoms=atoms[0]
noOfHAtoms=atoms[1]
noOfOAtoms=atoms[2]

noOfCO2Molecules=0
noOfH2OMolecules=0
noOfGlucoseMolecules=0
finalOutput=[]
finalOutput.append(noOfH2OMolecules)
finalOutput.append(noOfCO2Molecules)
finalOutput.append(noOfGlucoseMolecules)

error=0

if(noOfCAtoms==0):
    if(noOfOAtoms==(noOfHAtoms/2)):
        noOfH2OMolecules=noOfOAtoms
        finalOutput[0]=noOfH2OMolecules
    else:
        error=1
elif(noOfHAtoms==0):
    if(noOfOAtoms==noOfCAtoms*2):
        noOfCO2Molecules=noOfCAtoms
        finalOutput[1]=noOfCO2Molecules
    else:
        error=1
else:
    noOfCO2Molecules=((2*noOfOAtoms)-noOfHAtoms)/4
    finalOutput[1]=noOfCO2Molecules
    if not(isinstance(noOfCO2Molecules,( int, long ))):
        error=1
    # else:
    #     error=1

    noOfGlucoseMolecules=((4*noOfCAtoms)-(2*noOfOAtoms)+noOfHAtoms)/24
    finalOutput[2]=noOfGlucoseMolecules
    if not(isinstance(noOfGlucoseMolecules,( int, long ))):
        error=0
    # else:
    #     error=1

    noOfH2OMolecules=(noOfHAtoms+(2*noOfOAtoms)-(4*noOfCAtoms))/4
    finalOutput[0]=noOfH2OMolecules
    if not(isinstance(noOfH2OMolecules,( int, long ))):
        error=1
    # else:
    #     error=1
if(noOfCAtoms>pow(10,10) or noOfHAtoms>pow(10,10) or noOfOAtoms>pow(10,10)):
    pass
elif(error==1):
    print 'Error'
else:
    for l in finalOutput:
        print l,
