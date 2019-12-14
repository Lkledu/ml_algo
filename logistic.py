import math

y = {1,2,3,4,5,6,7,8,9,4.3,2.1,7.8, 30.4, 40.7}
x = {9,8,7,6,5,4,3,2,1}

def somatoria(listToCount):
    count = 0
    for x in listToCount:
        count += x
    return count

def squareList(listToSquare):
    listSquared = []

    for val in listToSquare:
        listSquared.append(math.pow(val,2))
    return listSquared

def multiplyMatriz(firstList, secondList):
    multiplied = []
    if len(firstList) == len(secondList):
        for idx, val in firstList:
            multiplied.append(val*secondList[idx])
    return multiplied

def slope():
    b = ((len(x) * multiplyMatriz(x,y)) - (somatoria(x)*somatoria(y))) / ((len(x) * (somatoria(squareList(x))) - (somatoria(squareList(x)))))
    return b

def interception():
    a = somatoria(y) - slope() * somatoria(x)
    return a

def yhat():
    #yHatValue = math.exp(interception() + slope()) / 1+ math.exp(interception() + slope())
    yHatValue = 1 / 1+ math.exp(somatoria(y) * (-1))
    return yHatValue


def gradient():
    r = 0
    return r

print("\nResultado:\n")
print(yhat())
print("\n gradiente:\n")
print(gradient())