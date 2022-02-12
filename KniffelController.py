import random
from KniffelReihe import Cube
def calculatePointAmountOfType(type, cubeArray):
    output = 0
    if type == 0 or type == 1:
        for x in cubeArray:
            output = output + x.amount
    if type >= 6:
        for x in cubeArray:
            if (x.amount + 5) == type:
                output = output + x.amount
    if type == 2:
        output = 50
    if type == 3:
        output = 30
    if type == 4:
        output = 40
    if type == 5:
        output = 25
    return output


def calculatePlayerPoints(player, KniffelBlock):
    output = 0
    for x in range(12):
        if KniffelBlock[player].components[x] != "-":
            output = output + int(KniffelBlock[player].components[x])
    return output


def displayResults(cubeArray):
    for x in cubeArray:
        print(str(x.amount))


def getSmallestNumber(cubeArray):
    output = 6
    for x in cubeArray:
        if output > x.amount:
            output = x.amount
    return output


def getBiggestNumber(cubeArray):
    output = 0
    for x in cubeArray:
        if output < x.amount:
            output = x.amount
    return output


def Speichern(path, KniffelBlock, amountOfPlayers):
    pathComplete = path + ".txt"
    f = open(pathComplete, 'wb')
    for x in range(amountOfPlayers):
        text = ""
        text = KniffelBlock[x].playerName
        for y in range(12):
            text = text + ":" + str(KniffelBlock[x].components[y])

        convToBin = ' '.join(map(bin, bytearray(text, 'utf8')))
        byte_obj = convToBin.encode('ascii')
        f.write(byte_obj + b"\n")
    f.close()


def getCombinations(cubeArray):
    combinations = ""
    if checkAmountSame(getAmounts(cubeArray)) == 5:
        combinations = "111"
    elif checkAmountSame(getAmounts(cubeArray)) == 4:
        combinations = "110"
    elif checkAmountSame(getAmounts(cubeArray)) == 3:
        combinations = "100"
    else:
        combinations = "000"
    if checkIfRoadRoad(4, cubeArray) == True:
        combinations = combinations + "1"
    else:
        combinations = combinations + "0"
    if checkIfRoadRoad(5, cubeArray) == True:
        combinations = combinations + "1"
    else:
        combinations = combinations + "0"
    if checkFullHouse(getAmounts(cubeArray)) == True:
        combinations = combinations + "1"
    else:
        combinations = combinations + "0"
    for z in range(6):
        z = z + 1
        if checkIfNumberIsContained(z, cubeArray) == True:
            combinations = combinations + "1"
        else:
            combinations = combinations + "0"
    return combinations


def checkIfNumberIsContained(number, cubeArray):
    combination = getAmounts(cubeArray)
    if int(combination[(number - 1)]) > 0:
        return True
    else:
        return False


def checkFullHouse(combinationString):
    parameter2, parameter3 = 0, 0
    for x in combinationString:
        if int(x) == 2:
            parameter2 = 1
        if int(x) == 3:
            parameter3 = 1
    if parameter2 == 1 and parameter3 == 1:
        return True
    else:
        return False


def checkAmountSame(combinationString):
    highestNumber = 0
    for x in (combinationString):
        if int(x) > highestNumber:
            highestNumber = int(x)
    return highestNumber


def checkIfRoadRoad(amount, cubeArray):
    combination = getAmounts(cubeArray)
    smallestNumber = getSmallestNumber(cubeArray)
    biggestNumber = getBiggestNumber(cubeArray)
    # Amount gets subtracted by one, due to the fact that for example 1,2,3,4 has a diffrence of 3
    if (biggestNumber - smallestNumber) >= (amount - 1):
        numbersInRow = 0
        for x in range(6):
            if int(combination[x]) > 0:
                numbersInRow = numbersInRow + 1
            else:
                numbersInRow = 0
            if numbersInRow >= amount:
                break
        if numbersInRow >= (amount):
            return True
        else:
            return False

    else:
        return False


def getAmounts(cubeArray):
    output = ""
    numbers = []
    for x in range(6):
        numbers.append(0)
    for y in range(5):
        numbers[((cubeArray[y].amount) - 1)] = numbers[((cubeArray[y].amount - 1))] + 1
    for x in (numbers):
        output = output + str(x)
    return output


def throw(newPlayerThrow, cubeArray):
    if newPlayerThrow:
        for x in range(5):
            cubeArray[x].amount = 0
            cubeArray[x].state = 1
        newPlayerThrow = False
    for x in range(5):
        if cubeArray[x].state == 1:
            result = random.randint(1, 6)
            cubeArray[x].amount = result
        else:
            continue

    return newPlayerThrow


def checkPossibleInputsForTable(combinations, KniffelBlock, playersTurn):
    output = []
    for x in range(12):
        if combinations[x] == "1" and str(KniffelBlock[playersTurn].components[x]) == "-":
            output.append(x)
    return output


def displayKniffelBlock(KniffelBlock, amountOfPlayers):
    print(
        "  Spieler  |  Drei  |  Vier  |  Fünf  |  KleineStraße  |  GroßeStraße  |  FullHouse  |  1  |  2  |  3  |  4  |  5  |  6  |")
    for x in range(amountOfPlayers):
        combinedString = "  " + KniffelBlock[x].playerName + "  |"
        for y in range(12):
            combinedString = combinedString + "  " + str(KniffelBlock[x].components[y]) + "  |"
        combinedString = combinedString + " = " + str(calculatePlayerPoints(x,KniffelBlock))
        print(combinedString)


def noteIntoLowerTable(pos, playersTurn, KniffelBlock,cubeArray):
    if str(KniffelBlock[playersTurn].components[pos]) != "-":
        print("Platz schon belegt")
        return False
    else:
        KniffelBlock[playersTurn].components[pos] = calculatePointAmountOfType(pos,cubeArray)
        print("Es wurde in die ", pos, " Zeile eingetragen.")
        return True


def initThrows(cubeArray):
    cubeArray.append(Cube(0, 0))
    cubeArray.append(Cube(0, 0))
    cubeArray.append(Cube(0, 0))
    cubeArray.append(Cube(0, 0))
    cubeArray.append(Cube(0, 0))


def getFreeFields(KniffelBlock, playersTurn):
    output = []
    for x in range(12):
        if KniffelBlock[playersTurn].components[x] == "-":
            output.append(x)
    return output


def unlockCube(posInArray, cubeArray):
    cubeArray[posInArray].state = 0
