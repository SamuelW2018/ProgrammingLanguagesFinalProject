myInput = open("DataFile2.txt", "r")

myOutput = open("RefinedDataForSecondDistribution.txt", "w")

myOutput.write('[')
for line in myInput:
    r = line.split()
    if r == []:
        r.append('0')
    newl = r[0] + ','
    myOutput.write(newl)
myOutput.write(']')

myInput.close()
myOutput.close()
