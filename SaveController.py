class SaveController():
    doc = ""
    def __init__(self,path):
        self.doc = path
    def writeNewLine(self,text):
        f = open(self.doc,'a')
        f.write(text + "\n")
        f.close()
    def scanDocument(self):
        f = open(self.doc, 'r')
        output = f.readlines()
        return output
    def getPlays(self):
        file = SaveController("DocLibrary.txt")
        file.checkAndCreateLibrary()
        output = file.scanDocument()
        return output
    def fileAlreadyExists(self):
        prompt = input("Ein Dokument mit diesem Namen existiert bereits. Möchten sie dieses überschreiben? J für JA N für Nein")
        while(prompt != "N" and prompt != "J"):
            prompt = input("Keine Gültige Eingabe.")
        if prompt == "N":
            newFileName = input("Geben sie den Neuen Namen des Spielstand an.")
            while newFileName in self.getPlays():
                newFileName = input("Geben sie den Neuen Namen des Spielstand an.")
            self.doc = newFileName
            self.createNewSaveFile()
        elif prompt == "J":
            f = open(self.doc , "w")
            f.write("")
            f.close()
    def checkAndCreateLibrary(self):
        try:
            f = open("DocLibrary.txt")
            f.close()
        except IOError:  
            f = open("DocLibrary.txt",'w')
            f.close()
    def createNewSaveFile(self):
        output = True
        if self.doc[:-4] != ".txt":
            self.doc = self.doc + ".txt"
        try:
            f = open(self.doc)
            f.close()
            #elf.fileAlreadyExists()
            output = False
        except IOError:
            self.checkAndCreateLibrary()
            file = open("DocLibrary.txt" , 'a')
            file.write(self.doc + "\n")
            file.close()
            newFile = open(self.doc,'w')
            newFile.close()
        return output
