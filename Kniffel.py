import random
from tkinter import messagebox
from Player import PlayerClass
from KniffelKombinationen import CheckFürKombinationen
from tkinter import *
from tkinter.font import Font
FIRSTCOLUMNINGAME = ["Spielername","nur Einser zählen","nur Zweier zählen","nur Dreier zählen","nur Vierer zählen","nur Fünfer zählen","nur Sechser zählen","Bonus bei 63 oder mehr", "Dreierpasch","Viererpasch", "Full-House", "Kleine Straße", "Große Straße", "Kniffel", "Chance", "Gesamt"]
TRANSPARENTCOLOR = '#123456'
TABELTOPOINTAMOUNT = [-1,0,1,2,3,4,5,-1,8,9,11,6,7,10,12,-1]
HOEHETEXT = 45
FORDERGRUNDFARBE = "#000000"
BREITETEXT = 150
MINDESTANZAHLANSPIELERN = 1
MAXIMALANZAHLANSPIELERN = 6
HINTERGRUNDFARBE = "#00FFFF"
ANZAHLDERSPIELERDIEANGEZEITWERDEN = 5
MAXIMALEANZAHLANERLAUBTENWÜRFEN = 3
ANZAHLDERSPALTEN = 16
ANZAHLDERREIHEN = 7
MAXIMALESPIELERNAMENLÄNGE = 9
OFFSET = 10
errechneteErgebnisse = CheckFürKombinationen()
player = []
sizeOfRethrowButton = 50
DISPLAYRESLTCUBESIZE = 50
spielerAnzeigeOffset = 0
startGroesseX = 1100
startGroesseY = 750
fenster = Tk()
spielBeendet = False
#The Font of the Text
preGameFont = Font(
family = 'Times',
size = 20,
weight = 'bold'
)
gameFont = Font(
    family = "Times",
    size = 16,
    #weight = "bold"
)
fenster.geometry(str(startGroesseX) + "x" + str(startGroesseY))
underline = None
def underlineCurrentPlayer(id):
    global oberfläche
    global underline
    global BREITETEXT
    global HOEHETEXT
    if spielerAmZug >5:
        id = 5
    if underline != None:
        oberfläche.delete(underline)
    offset = 230 # Der Offset ist leider dumm gecodet sorry. Du wirst ihn noch an 2 weiteren stellen finden
    underline = oberfläche.create_line(offset + id*BREITETEXT + 10, HOEHETEXT/2+15,offset+ (id+1)*BREITETEXT -10, HOEHETEXT/2+15, width = 2, fill = "red")
def calculateWholePoints(spielerAmZug):
    pointAmount = 0
    global player
    for x in range(14):
        if player[spielerAmZug].kniffelBoardInformation[x] != 99:
            pointAmount+= player[spielerAmZug].kniffelBoardInformation[x]
    player[spielerAmZug].kniffelBoardInformation[15] = pointAmount
def calculateBonus(spielerAmZug):
    global kniffelBlockUI
    pointAmount = 0
    global player
    for x in range(6):
        if player[spielerAmZug].kniffelBoardInformation[x] <90:
            pointAmount += player[spielerAmZug].kniffelBoardInformation[x]
    print(str(pointAmount))
    if pointAmount >= 63:
        player[spielerAmZug].kniffelBoardInformation[6] = 35 # 35 ist die Anzahl an Zusatzpunkten für 63 im Oberen berreich
def oberflächenPress(event):
    global BREITETEXT
    global HOEHETEXT
    global player
    global spielerAmZug
    offsetZ = 230
    offsetY = HOEHETEXT
    mousePosOrgX = event.x
    mousePosOrgY = event.y
    differenceX = mousePosOrgX-offsetZ
    differenceY = mousePosOrgY-offsetY
    idX = int(differenceX/BREITETEXT)
    idY = int(differenceY/HOEHETEXT)
    print(str(idX),",",str(idY))
    print(str(würfel))
    print(str(player[spielerAmZug].kniffelBoardInformation))
    #Wenn die Reihe des SPielers am Zug gedrückt
    if idY != 6:
        if spielerAmZug <= ANZAHLDERSPIELERDIEANGEZEITWERDEN:
            if idX == spielerAmZug:
                #----------------------------------------------------------------------------------------------------
                if player[spielerAmZug].kniffelBoardInformation[idY] == 99:
                    player[spielerAmZug].kniffelBoardInformation[idY] = errechneteErgebnisse.errechneteErgebnise[TABELTOPOINTAMOUNT[idY+1]]
                    oberfläche.itemconfig(kniffelBlockUI[idY+1][idX+1], text =str(errechneteErgebnisse.errechneteErgebnise[TABELTOPOINTAMOUNT[idY+1]]))
                        
                    würfelFensterUI[0].destroy()
                    calculateBonus(spielerAmZug)
                    calculateWholePoints(spielerAmZug)
                    oberfläche.itemconfig(kniffelBlockUI[15][idX+1], text = str(player[spielerAmZug].kniffelBoardInformation[15]))
                    if player[spielerAmZug].kniffelBoardInformation[6] < 90:
                        oberfläche.itemconfig(kniffelBlockUI[7][idX+1], text = str(player[spielerAmZug].kniffelBoardInformation[6]))
                    else :
                        oberfläche.itemconfig(kniffelBlockUI[7][idX+1], text = str(0))
                    spielerWechsel()
                    würfeln(1)
            #----------------------------------------------------------------------------------------------------
        #Das ist der Code der für mehr als 6 Spieler relevant wird
        elif spielerAmZug > ANZAHLDERSPIELERDIEANGEZEITWERDEN:
            if idX == 5:
                if player[spielerAmZug].kniffelBoardInformation[idY] == 99:
                    player[spielerAmZug].kniffelBoardInformation[idY] = errechneteErgebnisse.errechneteErgebnise[TABELTOPOINTAMOUNT[idY+1]]
                    oberfläche.itemconfig(kniffelBlockUI[idY+1][idX+1], text =str(errechneteErgebnisse.errechneteErgebnise[TABELTOPOINTAMOUNT[idY+1]]))
                    würfelFensterUI[0].destroy()
                    calculateBonus(spielerAmZug)
                    calculateWholePoints(spielerAmZug)
                    oberfläche.itemconfig(kniffelBlockUI[15][idX+1], text = str(player[spielerAmZug].kniffelBoardInformation[15]))
                    if player[spielerAmZug].kniffelBoardInformation[6] < 90:
                        oberfläche.itemconfig(kniffelBlockUI[7][idX+1], text = str(player[spielerAmZug].kniffelBoardInformation[6]))
                    else :
                        oberfläche.itemconfig(kniffelBlockUI[7][idX+1], text = str(0))
                    spielerWechsel()
                    würfeln(1)
            

#Nur zum testen
fenster.wm_attributes('-transparentcolor', TRANSPARENTCOLOR)
fenster.title("Kniffel")
oberfläche = Canvas(fenster, width =startGroesseX, height = startGroesseY, bg = HINTERGRUNDFARBE)
datentyp = PhotoImage(file = "Unbenannt.png")
oberfläche.pack()
#BILD
oberfläche.create_image((startGroesseX/2),(startGroesseY/2),image = datentyp)
oberfläche.bind("<Button-1>", oberflächenPress)
lockUI = []
uiElemente = []
status = 0
spieler = []
anzahlDerSpieler = 0
anzahlDesWurfes = 0
würfel = []
spielerAmZug = 0
kniffelBlockUI = [[0 for x in range(7)] for y in range(16)] 
würfelFensterUI = []

def initLockOrUnlock():
    global lockUI
    global würfel
    for x in range(5):
        if würfel[x] > 10:
            _rectangle = würfelFensterUI[1].create_rectangle(50*x+10, 10, 50*(x+1)-10,40, outline = "red")
            lockUI[x] = _rectangle
def lockOrUnlockCube(id):
    global würfel
    global würfelFensterUI
    if würfel[id] <10:
        würfel[id] +=10
        _rectangle = würfelFensterUI[1].create_rectangle(50*id+10, 10, 50*(id+1)-10,40, outline = "red")
        lockUI[id] = _rectangle
    else:
        würfel[id] -=10
        würfelFensterUI[1].delete(lockUI[id])
def tryParseInt(s):
    try:
        return int(s)
    except ValueError:
        return None
def calculateWinner():
    winner = 99
    maxPoints = 0
    for x in range(len(player)):
        if player[x].kniffelBoardInformation[15] > maxPoints:
            winner = x
            maxPoints = player[x].kniffelBoardInformation[15]
    return winner
def spielEndeTest():
    global spielBeendet
    amountOfBrackets = 0
    for x in range(17):
        if player[(anzahlDerSpieler-1)].kniffelBoardInformation[x] != 99:
            amountOfBrackets+=1
    if amountOfBrackets >= 14:
        winner = calculateWinner()
        spielBeendet = True
        messagebox.showinfo("Spiel beendet!", (str(spieler[winner]) + " hat Gewonnen!"))
def spielerWechsel():
    global spielerAmZug
    global anzahlDerSpieler
    spielEndeTest()
    if spielerAmZug == (anzahlDerSpieler-1):
        spielerAmZug = 0
    else:
        spielerAmZug+=1
    underlineCurrentPlayer(spielerAmZug)
    
def würfelFensterPress(event):
    global anzahlDesWurfes
    mouseX = event.x
    mouseY = event.y
    if(event.y > DISPLAYRESLTCUBESIZE):
        anzahlDesWurfes +=1
        würfelFensterUI[0].destroy()
        würfelFensterUI.pop(0)
        würfeln(0)
    else:
        id = int(mouseX/50)
        lockOrUnlockCube(id)
#Zeigt an was gewürfelt wurde, und übernimmt die Interaktionen mit dem Würfelfenster
def displayResult():
    global würfelFensterUI
    global würfel
    global sizeOfRethrowButton
    global DISPLAYRESLTCUBESIZE
    global lockUI
    würfelFenster = Tk()
    würfelFensterUI.insert(0,würfelFenster)
    würfelFenster.title("Ihr gewürfeltes Ergebnis:")
    sizeX = 5*DISPLAYRESLTCUBESIZE
    sizeY = DISPLAYRESLTCUBESIZE+sizeOfRethrowButton
    würfelFenster.geometry(str(sizeX)+"x"+str(sizeY))
    cv = Canvas(würfelFenster,width = sizeX, height = sizeY)
    würfelFensterUI.insert(1,cv)
    initLockOrUnlock()
    for x in range(5):
        cv.create_line(x*(DISPLAYRESLTCUBESIZE),0,x*DISPLAYRESLTCUBESIZE,sizeY-sizeOfRethrowButton,width = 2)
        if würfel[x] > 10:
            cv.create_text(x*DISPLAYRESLTCUBESIZE+(DISPLAYRESLTCUBESIZE/2),(DISPLAYRESLTCUBESIZE/2), text = str((würfel[x])-10))
        else:
            cv.create_text(x*DISPLAYRESLTCUBESIZE+(DISPLAYRESLTCUBESIZE/2),(DISPLAYRESLTCUBESIZE/2), text = str((würfel[x])))
        
    cv.create_line(0,sizeY-sizeOfRethrowButton,sizeX,sizeY-sizeOfRethrowButton,width = 2)
    cv.create_text(sizeX/2,sizeY-(sizeOfRethrowButton/2),anchor="center",text = "Nicht ausgewählt Würfel neu Würfeln.")
    cv.pack()
    cv.bind("<Button-1>", würfelFensterPress)
    würfelFenster.mainloop()
def würfeln(neuWürfeln):
    global würfel
    global errechneteErgebnisse
    global MAXIMALEANZAHLANERLAUBTENWÜRFEN
    global anzahlDesWurfes
    global spielBeendet
    if neuWürfeln == 1:
        for x in range(len(würfel)):
            würfel[x] = 1
        anzahlDesWurfes = 0
    if anzahlDesWurfes < MAXIMALEANZAHLANERLAUBTENWÜRFEN:
        for x in range(5):
            if würfel[x] < 10:
                würfel[x] = random.randint(1,6)
                #würfel[x] = x+1
            else:
                print(str(x),"war über 10")
        errechneteErgebnisse.berrechneTabelle(würfel)
        if spielBeendet == False:
            displayResult()
def spielerNamenRegistrieren(event = None):
    global oberfläche
    global uiElemente
    global spieler
    global status
    if len(spieler) != (anzahlDerSpieler):
        if status != 0:
            if uiElemente[1].get() not in spieler and len(uiElemente[1].get()) <= MAXIMALESPIELERNAMENLÄNGE:
                spieler.append(uiElemente[1].get().lower())
                uiElemente[1].delete(0,'end')
            elif uiElemente[1].get() in spieler:
                uiElemente[1].delete(0,'end')
                uiElemente[1].insert(0,"SPIELERNAME BEREITS VERGEBEN!")
            else:
                uiElemente[1].delete(0,'end')
                uiElemente[1].insert(0,"SPIELERNAME ZU LANG. MAX " + str(MAXIMALESPIELERNAMENLÄNGE) + " ZEICHEN")
        else:
            status = 1
        if len(spieler) == anzahlDerSpieler:
            for x in range(len(uiElemente)):
                if x != 0:
                    uiElemente[x].destroy()
                else:
                    oberfläche.delete(uiElemente[x])
            initialisiereSpieleOberfläche()
        else:
            oberfläche.itemconfig(uiElemente[0], text = "Geben Sie den Namen des " + str(len(spieler)) + " ein:" )
def initialisiereSpieleOberfläche():
    global lockUI
    global oberfläche
    global spieler
    global kniffelBlockUI
    global OFFSET
    global gameFont
    global HOEHETEXT
    global FORDERGRUNDFARBE
    global FIRSTCOLUMNINGAME
    global BREITETEXT
    global startGroesseY
    global startGroesseX
    global anzahlDerSpieler
    #Creating the Players
    for x in range(anzahlDerSpieler):
        spielerPlaceholder = PlayerClass()
        player.append(spielerPlaceholder)
    #Initialisierung des LockUI Array
    for x in range(5):
        lockUI.append(0)
    startPosX = 230
    incrementValue = 150
    for x in range(7):
        oberfläche.create_line(startPosX + (x*incrementValue), 0, startPosX+(incrementValue*x), startGroesseY, width = 2, fill = FORDERGRUNDFARBE)
    for y in range(16):
        oberfläche.create_line(0,y*(HOEHETEXT),startGroesseX,y*HOEHETEXT, width = 2, fill = FORDERGRUNDFARBE)

    for x in range(7):
        for y in range(16):
            if x == 0:
                id = oberfläche.create_text(OFFSET+x*( BREITETEXT),OFFSET + y*(HOEHETEXT), text = FIRSTCOLUMNINGAME[y], anchor = "nw", font = gameFont, fill = FORDERGRUNDFARBE)
                kniffelBlockUI[y][x] = (id)
            else:
                if y == 0:
                    if (x) > anzahlDerSpieler:
                        id = oberfläche.create_text(OFFSET + x*( BREITETEXT) + (BREITETEXT/2),OFFSET + y*(HOEHETEXT), text = "", font = gameFont, anchor = "nw", fill = FORDERGRUNDFARBE)
                    else:
                        id = oberfläche.create_text(OFFSET + x*( BREITETEXT) + (BREITETEXT/2),OFFSET + y*(HOEHETEXT), text = spieler[x-1], font = gameFont, anchor = "nw", fill = FORDERGRUNDFARBE)
                else:
                    id = oberfläche.create_text(OFFSET + x*( BREITETEXT) + (BREITETEXT/2),OFFSET + y*(HOEHETEXT), text = " ", font = gameFont, anchor = "nw", fill = FORDERGRUNDFARBE)
                    kniffelBlockUI[y][x] = (id)
    
    würfeln(1)
def anzahlderSpielerRegistrieren(event = None):
    global anzahlDerSpieler
    eingabe = tryParseInt(uiElemente[1].get())
    if eingabe != None:
        if eingabe >= MINDESTANZAHLANSPIELERN and eingabe <= MAXIMALANZAHLANSPIELERN:
            #Event wird neu gebindet, damit nach bestätigen durch Enter ein name registriert wird und nicht mehr die Anzahl der Spieler
            uiElemente[1].bind("<Return>",spielerNamenRegistrieren)
            uiElemente[1].delete(0,'end')
            anzahlDerSpieler = eingabe
            spielerNamenRegistrieren()
        else:
            uiElemente[1].delete(0,"end")
            uiElemente[1].insert(0,"DIE DERZEITIGE MAXIMALE SPIELERANZAHL BETRÄGT 6")
def spielerAnzahlEingabe():
    global startGroesseX
    global FORDERGRUNDFARBE
    global startGroesseY
    global oberfläche
    lbl = oberfläche.create_text(50,150,font = ("Courier", 20), text = "Geben sie die gewünschte Anzahl an Spielern ein:", anchor = "nw", fill = FORDERGRUNDFARBE)
    uiElemente.append(lbl)
    oberfläche.pack()
    e = Entry(fenster, width = 50,font=("Courier", 20))
    e.place(x = 50, y = 200)
    uiElemente.append(e)
    e.bind("<Return>",anzahlderSpielerRegistrieren)
def initialisiereWuerfel():
    global würfel
    for x in range(5):
        würfel.append(0)
initialisiereWuerfel()
spielerAnzahlEingabe()
fenster.mainloop()