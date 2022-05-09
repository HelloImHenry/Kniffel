class CheckFürKombinationen:
    #Sortierung des Array [1,2,3,4,5,6,KleineStraße,GroßeStraße,Dreier,Vierer,Kniffel,FullHouse,Chance]
    
    errechneteErgebnise = [0,0,0,0,0,0,0,0,0,0,0,0,0]
    ANZAHLGEBRAUCHTFÜRKLEINESTRASSE = 4
    ANZAHLGEBRAUCHTFÜRGROßESTRASSE = 5
    ANZAHLGEBRAUCHTFÜRDREIERPASCH = 3
    ANZAHLGEBRAUCHTFÜRVIERERPASCH = 4
    ANZAHLGEBRAUCHTFÜRKNIFFEL = 5
    PUNKTEGEBRAUCHTFÜRBONUSPUNKTEOBEREHAELFTE = 60

    BELOHNUNGFÜRKLEINESTRASSE = 35
    BELOHNUNGFÜRGROSSESTRASSE = 45
    BELOHNUNGFÜRFULLHOUSE = 25
    BELOHNUNGFÜRKNIFFEL = 50
    
    def berrechneTabelle(self,würfelEingabe):
        for x in range(len(self.errechneteErgebnise)):
            self.errechneteErgebnise[x] = 0
        #Kopieren des Array
        würfelKombination = []
        for x in würfelEingabe:
            würfelKombination.append(x)
        #Zurückübersetzen der Gelockten Werte
        for x in range(len(würfelKombination)):
            if würfelKombination[x] > 10:
                würfelKombination[x] -=10
        self.ErrechneergebnisseEinzelneZahlen(würfelKombination)
        self.ErrechneErgebnissePascheUndFullHouse(würfelKombination)
        self.ErrechneErgebnisseStraßen(würfelKombination)
        self.ErrechneergebnisseEinzelneZahlen(würfelKombination)
        self.ErrechneChance(würfelKombination)
    def ErrechneChance(self,würfelKombinationen):
        punkte = 0
        for x in würfelKombinationen:
            punkte+=x
        self.errechneteErgebnise[12] = punkte
    def ErrechneErgebnisseStraßen(self, würfelKombination):
        würfelKombination.sort()
        anzahlInReihe = 0
        for x in range(len(würfelKombination)-1):
            if würfelKombination[x+1] == würfelKombination[x]+1:
                anzahlInReihe +=1
            elif würfelKombination[x+1] != würfelKombination[x]+1 and anzahlInReihe >=3:
                anzahlInReihe = self.ANZAHLGEBRAUCHTFÜRKLEINESTRASSE
            else:
                anzahlInReihe = 0
        if anzahlInReihe == 3:
            self.errechneteErgebnise[6] = self.BELOHNUNGFÜRKLEINESTRASSE
        if anzahlInReihe == 4:
            self.errechneteErgebnise[6] = self.BELOHNUNGFÜRKLEINESTRASSE
            self.errechneteErgebnise[7] = self.BELOHNUNGFÜRGROSSESTRASSE
    def ErrechneErgebnissePascheUndFullHouse(self,würfelKombinaiton):
        maximaleAnzahlDerGleichenAugen = []
        würfelKombinaiton.sort()
        for x in range(6):
            maximaleAnzahlDerGleichenAugen.append(würfelKombinaiton.count(x+1))
        #Fullhouse
        if maximaleAnzahlDerGleichenAugen.count(3) == 1 and maximaleAnzahlDerGleichenAugen.count(2) == 1:
            self.errechneteErgebnise[11] = self.BELOHNUNGFÜRFULLHOUSE
        #DreierPasch
        elif maximaleAnzahlDerGleichenAugen.count(3) == 1 and maximaleAnzahlDerGleichenAugen.count(1) == 2:
            self.errechneteErgebnise[8] = self.berechneBelohnungFuerPasch(würfelKombinaiton)
        #ViererPasch und auch DreierPasch, da inkludiert
        elif maximaleAnzahlDerGleichenAugen.count(4) == 1 and maximaleAnzahlDerGleichenAugen.count(1) == 1:
            self.errechneteErgebnise[9] = self.berechneBelohnungFuerPasch(würfelKombinaiton)
            self.errechneteErgebnise[8] = self.berechneBelohnungFuerPasch(würfelKombinaiton)
        #Kniffel und auch ViererPasch und auch DreierPasch, da inkludiert
        elif maximaleAnzahlDerGleichenAugen.count(5) == 1:
            self.errechneteErgebnise[10] = self.BELOHNUNGFÜRKNIFFEL
            self.errechneteErgebnise[9] = self.berechneBelohnungFuerPasch(würfelKombinaiton)
            self.errechneteErgebnise[8] = self.berechneBelohnungFuerPasch(würfelKombinaiton)
    def berechneBelohnungFuerPasch(self,würfelKombination):
        ergebnis = 0
        for x in range(len(würfelKombination)):
            ergebnis += würfelKombination[x]
        return ergebnis
    def ErrechneergebnisseEinzelneZahlen(self,würfelKombination):
        maximaleAnzahlDerGleichenAugen = []
        würfelKombination.sort()
        for x in range(6):
            maximaleAnzahlDerGleichenAugen.append(würfelKombination.count(x+1))
        
        ergebnisseDerRechnung = self.berrechneBelohnungFuerEinzelneZahl(maximaleAnzahlDerGleichenAugen)
        #Die Einzelnen Zahlen durchgehen
        for x in range(6):
            self.errechneteErgebnise[x] = ergebnisseDerRechnung[x]
    def berrechneBelohnungFuerEinzelneZahl(self,maximaleAnzahlDerGleichenAugen):
        ergebnisse = []
        #[0,2,0,1,0,2] = [0*1,2*2,0*3,1*4,0*5,2*6]
        for x in range(len(maximaleAnzahlDerGleichenAugen)):
            ergebnisse.append((x+1)*maximaleAnzahlDerGleichenAugen[x])
        return ergebnisse
    def berrechneObBonus(KniffelBlock):
        punkteInDenErstenSechsSpalten = 0
        #Kommt wenn KniffelBlock Fertig
        test = 0