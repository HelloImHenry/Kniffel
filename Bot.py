import random

class Pattern():
    difference = 100
    def __init__(self,ID,patternCombinations):
        self.patternCombinations = patternCombinations
        self.ID = ID
    def resetDifference(self):
        self.difference = 100
cubes = []
def throw():
    global cubes
    global patterns
    for y in patterns:
        y.resetDifference()
    for x in range(5):
        output = random.randint(1,6)
        cubes.append(output)
"""
0 = Kleine Straße
1 = Große Straße
2 = Full House
3 = 3 Pasch
4 = 4 Pasch
5 = 5 Pasch
"""
patternDifferences = []
patterns = []
patterns.append(Pattern(0, ["12340", "01234"]))
patterns.append(Pattern(1, ["12345"]))
patterns.append(Pattern(2, ["11222", "11122"]))
patterns.append(Pattern(3, ["00111", "01110", "11100"]))
patterns.append(Pattern(4, ["01111", "11110"]))
patterns.append(Pattern(5, ["11111"]))

def optimalOffset(patternToCompareTo):
    global cubes
    offsets = []
    for x in range(5):
        if patternToCompareTo[x] != "0":
            offset = int(cubes[x] - int(patternToCompareTo[x]))
            if offset not in offsets:
                offsets.append(offset)
    amountOfCorrectNumersInPattern = 0
    perfectOffset = 0
    for x in range(len(offsets)):
        currentSameCubes = 0
        for y in range(5):
            if int(patternToCompareTo[y]) == int(cubes[y] - offsets[x]) and patternToCompareTo[y] != "0":
                currentSameCubes = currentSameCubes +1
        if currentSameCubes > amountOfCorrectNumersInPattern:
            amountOfCorrectNumersInPattern = currentSameCubes
            perfectOffset = offsets[x]
    return perfectOffset

def calculating(type):
    points = 0
    if type == 0 or type == 1:
        for x in cubes:
            points = points + x.amount
    if type >= 6:
        for x in cubes:
            if (x.amount + 5) == type:
                points = points + x.amount
    if type == 2:
        points = 50
    if type == 3:
        points = 30
    if type == 4:
        points = 40
    if type == 5:
        points = 25
    return points
    
def getOffset(patternToCompareTo, posToCompareTo):
    global cubes
    output = 0
    pos = 0
    while patternToCompareTo[pos] == "0":
        pos+=1
    if posToCompareTo != 0:
        pos = posToCompareTo
    output = cubes[(pos)] - int(patternToCompareTo[(pos)])
    return output
def getDouble():
    global cubes
    cubes.sort()
    output = 99
    for x in range(4):
        if cubes[x] == cubes[(x+1)]:
            output = x
    return output
def kickOutDouble(pos):
    global cubes
    cubes.sort()
    cubes.append(cubes[pos])
    cubes.pop(pos)
def bigRoadPattern():
    global cubes
    numbersContained = 0
    for x in range(7):
        if x != 0:
            if x in cubes:
                numbersContained+=1
    difference = 6 - numbersContained
    return difference
def getClosestPatterns():
    global patterns
    array = []
    for x in range(len(patterns)):
        print(patterns[x].difference)
    patterns.sort(key=lambda x: x.difference)   # sort by difference
    lowestDifference = patterns[0].difference
    for x in range(len(patterns)):
        if patterns[x].difference == lowestDifference:
            array.append(patterns[x].ID)
    print("The lowest difference: " + str(lowestDifference))
    return array
def compare():
    global patterns
    global cubes
    for x in range(len(patterns)):
        for y in range(len(patterns[x].patternCombinations)):
            currentPattern = patterns[x].patternCombinations[y]
            cubes.sort()
            differenceToPattern = 0
            offset = optimalOffset(currentPattern)

            if currentPattern == patterns[1].patternCombinations[0]:
                differenceToPattern = bigRoadPattern()
            else:
                #The little Streets need to be checked if they contain duplicates. If yes we need to put it into the last spot to fit the pattern
                if currentPattern == patterns[0].patternCombinations[0] or currentPattern == patterns[0].patternCombinations[1]:
                    getDoublePos = getDouble()
                    if getDoublePos != 99:
                        kickOutDouble(getDoublePos)
                for z in range(5):
                #Full House needs two Offsets.
                    if currentPattern == patterns[2].patternCombinations[0] and z == 2:
                        offset = getOffset(currentPattern,z)
                    elif currentPattern == patterns[2].patternCombinations[0] and z == 0:
                        offset = getOffset(currentPattern,z)
                    if currentPattern == patterns[2].patternCombinations[1] and z == 3:
                        offset = getOffset(currentPattern,z)
                    elif currentPattern == patterns[2].patternCombinations[1] and z == 0:
                        offset = getOffset(currentPattern,z)
                    if str(currentPattern[z]) == "0":
                        continue
                    else:
                        if int(currentPattern[z]) == (cubes[z] - offset):
                            continue
                        else:
                            differenceToPattern+=1
            if patterns[x].difference > differenceToPattern:
                patterns[x].difference = differenceToPattern
        if patterns[x].difference == 0:
            print("Bei dem Gewürfelten Ergebnis handelt es sich um eine " + str(patterns[x].ID))
throw()
cubes.sort()
for x in cubes:
    print(str(x))
compare()
print("")
closest =getClosestPatterns()

print(str(closest))