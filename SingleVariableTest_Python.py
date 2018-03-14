import math

myInput = open("DataFile1.txt", "r")
myInput2 = open("DataFile2.txt", "r")

myList = list()
myList2 = list()

for line in myInput:
    myList.append(int(line))

for line in myInput2:
    if(line != '\n'):
        myList2.append(int(line))
    else:
        myList2.append(0)

def mean(d):
    calc = 0.0
    total = len(d)
    for i in d:
        calc += i
    return (calc/total)

def firstQ(d):
    c = sorted(d)
    location = int(len(c) / 4)
    return c[location]

def median(d):
    c = sorted(d)
    location = int(len(c) / 2)
    return c[location]

def thirdQ(d):
    c = sorted(d)
    location = int(len(c) * 3 / 4)
    return c[location]

def mode(d):
    c = sorted(d)
    maxElem = c[0]
    current = 1
    maximum = 1
    for i in range(1, len(c)):
        if c[i] > c[i-1]:
            current = 1
        else:
            current = current + 1
        if current > maximum:
            maximum = current
            maxElem = c[i]
    return maxElem

def rangeR(d):
    c = sorted(d)
    return c[len(c)-1] - c[0]

def stDev(d, m):
    total = len(d)
    calc = 0.0
    for i in range(0, len(d)):
        calc += ((d[i] - m)*(d[i] - m))
    calc = calc / total

    result = calc**(1/2)
    return result

def variance(sd):
    return (sd * sd)

def covar(d1, d2, mean1, mean2):
    total = len(d1)
    calc = 0.0
    for i in range(0, len(d1)):
        calc += ((d1[i]-mean1)*(d2[i]-mean2))
    calc = calc / total
    return calc

def corrcoef(covariance, stdev1, stdev2):
    return (covariance / (stdev1 * stdev2))

def bestLineA(corre, st1, st2):
    return (corre * st2) / st1

def bestLineB(corre, st1, st2, mean1, mean2):
    return (mean1 + ((corre * st2) / st1) * mean2)
        

t = mean(myList)
print(t)
print(firstQ(myList))
print(median(myList))
print(thirdQ(myList))
print(mode(myList))
print(rangeR(myList))
s = stDev(myList, t)
print(s)
print(variance(s))

t2 = mean(myList2)
print('\n')
print(t2)
print(firstQ(myList2))
print(median(myList2))
print(thirdQ(myList2))
print(mode(myList2))
print(rangeR(myList2))
s2 = stDev(myList2, t2)
print(s2)
print(variance(s2))

c = covar(myList, myList2, t, t2)
print(c)
corr = corrcoef(c, s, s2)
print(corr)
ax = bestLineA(corr, s, s2)
b = bestLineB(corr, s, s2, t, t2)
newString = str(ax) + "x + " + str(b)
print(newString)
