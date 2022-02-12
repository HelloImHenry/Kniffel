from tkinter import *
from turtle import width
from SaveController import *
root = Tk()
sizeX = 500
sizeY = 800
currentPanelID = 0
hoverOver = 0
hoverColor = "#F8E0F7"
defaultColor = "#ffffff"
pressedColor = "#DF01D7"
inputStrings = []
playersTurn = 0
amountOfPlayers = 0
playerNames = []
"""
0 = Main
1 = New Game
2 = Spieler Panel
3 = Load Game
4 = In Game
"""
"""
LinksOben = 0
RechtsOben = 1
LinksUnten = 2
RechtsUnten = 3
"""
geometryProperty = str(sizeX) + "x" + str(sizeY)
root.geometry(geometryProperty)
root.maxsize(sizeX,sizeY)
root.minsize(sizeX,sizeY)
cv = Canvas(root,width = sizeX,height = sizeY)
uiElements = []
def DisplayPlayerPanel():
    global cv
    global sizeX
    global sizeY
    global uiElements
    global hoverOver
    #Size of Rectangle Y
    rectSizeY = 20
    id = cv.create_text(30,(sizeY/4), text = "Geben sie die Anzahl der Spieler ein:", anchor = W)
    hoverOver = 0
    uiElements.append(id)
    id = cv.create_rectangle(30,((sizeY/2)-(rectSizeY/2)), (sizeX-30),((sizeY/2)+(rectSizeY/2)))
    uiElements.append(id)
    id = cv.create_text(30,(sizeY/2), text = "", anchor = W)    
    uiElements.append(id)


def DisplayNewGamePanel():
    global cv
    global sizeX
    global sizeY
    global uiElements
    #Offset der das Rechteck von den Rändenr vernhält.
    offset = 30
    #Falls man per Buttonpress bestätigen können soll muss hier ein Offset rein damit der Button nicht als Eingabe fenster gezeichnet wird.
    buttonSize = 0
    #y Größe des Eingabe fensters
    inputSizeY = 100
    #TextOffset
    textoffset = 5
    id = cv.create_text(30,(sizeY/4),text = "Geben sie den Dateipfad ein: ", anchor = W)
    uiElements.append(id)
    id = cv.create_rectangle(offset,(sizeY/2), (sizeX-offset-buttonSize), ((sizeY/2)+inputSizeY), fill = 'white')
    uiElements.append(id)
    id = cv.create_text((offset+textoffset), ((sizeY/2) + (inputSizeY/2)), text = "Dateipfad eingeben...", anchor = W)
    uiElements.append(id)
    

def DisplayMainMenuPanel():
    global cv
    global defaultColor
    global hoverColor
    global uiElements
    id = cv.create_line(0,(sizeY/2), (sizeX),(sizeY/2))
    uiElements.append(id)
    id = cv.create_line((sizeX/2),0,(sizeX/2),sizeY)
    uiElements.append(id)

    #Oben Links
    id = cv.create_rectangle(0,0,(sizeX/2),(sizeY/2),fill = defaultColor)
    uiElements.append(id)
    id = cv.create_text((sizeX/4), (sizeY/4), text = "Neues Spiel")
    uiElements.append(id)
    #Unten Links
    id = cv.create_rectangle(0,(sizeY/2),(sizeX/2),sizeY,fill = defaultColor)
    uiElements.append(id)
    id = cv.create_text((sizeX/4), ((sizeY/4)*3), text = "Replay anschauen")
    uiElements.append(id)
    #ObenRechts
    id = cv.create_rectangle((sizeX/2),0,sizeX,(sizeY/2),fill = defaultColor)
    uiElements.append(id)
    id = cv.create_text(((sizeX/4)*3), (sizeY/4), text = "Spiel laden")
    uiElements.append(id)
    #Unten Rechts
    id = cv.create_rectangle((sizeX/2),(sizeY/2),sizeX,sizeY,fill = defaultColor)
    uiElements.append(id)
    id = cv.create_text(((sizeX/4)*3), ((sizeY/4)*3), text = "Spielstände verwalten")
    uiElements.append(id)

def hoverController(pos):
    global currentPanelID
    global defaultColor
    global hoverColor
    global uiElements
    if currentPanelID == 0:
        cv.itemconfig(uiElements[2],fill = defaultColor)
        cv.itemconfig(uiElements[4],fill = defaultColor)
        cv.itemconfig(uiElements[6],fill = defaultColor)
        cv.itemconfig(uiElements[8],fill = defaultColor)
        translatedPos = 2 + (2*pos)
        cv.itemconfig(uiElements[translatedPos],fill = hoverColor)
def hideAllPanels():
    global uiElements
    for x in uiElements:
        cv.delete(x)
    uiElements.clear()
def panelSwitcher(panel):
    hideAllPanels()
    if panel == 0:
        DisplayMainMenuPanel()
    elif panel == 1:
        DisplayNewGamePanel()
    elif panel == 2:
        DisplayPlayerPanel()
def overwritePathButtonEnter(element):
    cv.itemconfig(element, fill = "#16194C")
def overwritePathButtonExit(element):
    cv.itemconfig(element, fill = "red")
def intTryParse(value):
    try:
        return int(value), True
    except ValueError:
        return value, False
def enter(event):
    global uiElements
    global currentPanelID
    global inputStrings
    global cv
    global hoverOver

    global playersTurn
    global playerNames
    global amountOfPlayers
    #Offset of the Error Message
    element = 0
    element2 = 0
    if currentPanelID ==1:
        save = SaveController(inputStrings[1])
        success = save.createNewSaveFile()
        if success == True:
            print("Successfully created the save file.")
            currentPanelID = 2
            panelSwitcher(currentPanelID)
            
        else:
            element = cv.create_text(30,(sizeY/6),text = "Diesen Dateipfad gibt es bereits!" + "\n"+"Wenn sie ihn überschreiben wollen Drücken sie den Button!"+"\n"+"Falls nicht geben sie einen neuen Dateipfad ein.", anchor=W, fill = "#FF0000")
            element2 = cv.create_rectangle(300,300,350,350,fill = 'red', tag = "overwritePathButton")
            element2.bind('<Enter>',overwritePathButtonEnter(element2))
            element2.bind('<Leave>',overwritePathButtonExit(element2))
        
    elif currentPanelID == 2 and hoverOver == 0:
        outcome = intTryParse(inputStrings[2])
        if outcome[1] == True:
            hoverOver = 1
            amountOfPlayers = outcome[0]
            inputStrings[2] = ""
            cv.itemconfig(uiElements[2], text = inputStrings[2])
            cv.itemconfig(uiElements[0], text = "Geben sie den Namen des 1 Spieler ein:")
    elif currentPanelID == 2 and hoverOver == 1:
        if playersTurn == (amountOfPlayers):
            #Load new Panel
            hoverOver = 2
        else:
            playerNames[playersTurn] = inputStrings[2]
            inputStrings[2] = ""
            cv.itemconfig(uiElements[2], text = inputStrings[2])
            playersTurn+=1
            displayString = "Geben sie den Namen des " + str((playersTurn+1)) + " ein:"
            cv.itemconfig(uiElements[0], text = displayString)
            

               
def click(event):
    global hoverOver
    global currentPanelID
    if currentPanelID == 0:
        currentPanelID = hoverOver+1
        panelSwitcher(currentPanelID)
def removeLetter(event):
    global inputStrings
    global uiElements
    global cv
    global currentPanelID
    inputStrings[1] = inputStrings[1][:-1]
    cv.itemconfig(uiElements[2], text = inputStrings[1])
def keyUpEvent(event):
    global currentPanelID 
    global inputStrings
    global uiElements
    global cv
    #print("Hoch")
    inputStrings[1] += event.char
    cv.itemconfig(uiElements[2], text = inputStrings[1])


def mouseController(event):
    global hoverOver
    global currentPanelID
    global sizeX
    global sizeY
    output = 99
    posX = event.x
    posY = event.y
    if currentPanelID == 0:
        if posX > 0 and posX < (sizeX/2):
            if posY >0 and posY < (sizeY/2):
                output = 0
            elif posY > (sizeY/2) and posY < sizeY:
                output = 1
            else:
                #print("UIERROR: MouseHover: Out of Bounds[Intentional]")
                output = 0
        elif posX < sizeX and posX > (sizeX/2):
            if posY >0 and posY < (sizeY/2):
                output = 2
            elif posY <sizeY and posY > (sizeY/2):
                output = 3
            else:
                #print("UIERROR: MouseHover: Out of Bounds[Intentional]")
                output = 0
        else:
            #print("UIERROR: MouseHover: Out of Bounds[Intentional]")
            output = 0
    hoverController(output)
    hoverOver = output
for x in range(4):
    inputStrings.append("")
DisplayMainMenuPanel()

root.bind('<Motion>', mouseController)
root.bind('<Button-1>', click)
root.bind('<KeyRelease>', keyUpEvent)
root.bind('<BackSpace>', removeLetter)
root.bind('<Return>', enter)
cv.pack()
root.mainloop()