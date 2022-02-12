from KniffelController import *
from KniffelReihe import Row

amountOfPlayers = int(input("Geben sie die Anzahl der Spieler an:"))
KniffelBlock = []
cubeArray = []
playersTurn = 0
newPlayerThrow = True
for x in range(amountOfPlayers):
    name = input("Geben sie den Namen des " + str(x) + " Spielers ein:")
    componentPlaceholder = []
    for j in range(12):
        componentPlaceholder.append("-")
    placeholder = Row(name, componentPlaceholder,0)
    KniffelBlock.append(placeholder)
print("Alle Spieler gespeichert.")

initThrows(cubeArray)
while(KniffelBlock[(amountOfPlayers-1)].full == 0):
    print(KniffelBlock[playersTurn].playerName, " ist am Zug.")
    Speichern("Version1", KniffelBlock, amountOfPlayers)
    throwsPlayer = 1
    while throwsPlayer != 3:
        newCubes = 0
        newPlayerThrow = throw(newPlayerThrow, cubeArray)
        displayResults(cubeArray)
        throwAgain = input("Möchtest du noch einmal Werfen? J für JA N für NEIN")
        if throwAgain == "N":
            break
        elif throwAgain == "J":
            throwsPlayer += 1
            for x in range(5):
                cubeArray[x].state = 0
            newCubes = int(input("Wie viele Würfel möchtest du neu Würfeln?"))
            while newCubes > 5:
                newCubes = int(input("Es wurden zu viele Würfel neu gewürfelt! Du kannst nur 5 neu Würfeln."))
            while newCubes > 0:
                cubeToRethrow = int(input("Geben sie die ID des Würfels ein, welchen sie neu Würfeln wollen."))
                cubeArray[cubeToRethrow].state = 1
                newCubes -= 1
    newPlayerThrow = throw(newPlayerThrow, cubeArray)
    displayResults(cubeArray)
    possibleCombinations = getCombinations(cubeArray)
    possibleInputs = checkPossibleInputsForTable(possibleCombinations, KniffelBlock, playersTurn)

    freeSlots = getFreeFields(KniffelBlock, playersTurn)
    skip = False
    canFill = True
    if len(possibleInputs) == 0 and len(freeSlots) != 0:
        print("Du hast leider kein Kriterium erfüllt. Du musst eines deiner freien Felder streichen.")
        canFill = False
        possibleInputs = freeSlots
    print("---------------------------------")
    for x in possibleInputs:
        print(str(x))
    print("---------------------------------")
    if not skip:
        pickedCombination = int(input("Geben sie ein, in welche Spalte sie eintragen wollen."))
        pickSuccess = False
        if pickedCombination in possibleInputs:
            pickSuccess = True
        else:
            print("Du hast diese Kombination nicht gewürfelt!")
        while not pickSuccess:
            pickedCombination = int(input("Geben sie ein, in welche Spalte sie eintragen wollen."))
            if pickedCombination in possibleInputs:
                pickSuccess = True
            else:
                print("Du hast diese Kombination nicht gewürfelt, oder bereits etwas in diese Spalte eingetragen!")

        if canFill:
            noteSuccess = noteIntoLowerTable(pickedCombination, playersTurn, KniffelBlock,cubeArray)
            while not noteSuccess:
                pickedCombination = int(input("Eintragefehler: Geben sie ein neues Feld an."))
                noteSuccess = noteIntoLowerTable(pickedCombination, playersTurn, KniffelBlock,cubeArray)
        else:
            KniffelBlock[playersTurn].components[pickedCombination] = "0"
    displayKniffelBlock(KniffelBlock, amountOfPlayers)

    if len(possibleInputs) == 0 and len(freeSlots) == 0:
        maxPoints = 0
        winner = 0
        
        #get player with higehst points
        for x in range(amountOfPlayers):
            if calculatePlayerPoints(x,KniffelBlock) > maxPoints:
                maxPoints = calculatePlayerPoints(x, KniffelBlock)
                winner = x

        print("Das Spiel ist vorbei. Der Gewinner ist: " + KniffelBlock[winner].playerName)
        skip = True
        KniffelBlock[playersTurn].full = 1
        continue

    if playersTurn == (int(amountOfPlayers) - 1):
        playersTurn = 0
    else:
        playersTurn = playersTurn + 1
    newPlayerThrow = True