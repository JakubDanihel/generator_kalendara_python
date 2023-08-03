import datetime

#nastavenie konstant
DNI = ("Pondelok", "Utorok", "Streda", "Stvrtok", "Piatok", "Sobota", "Nedela")
MESIACE = ("Januar", "Februar", "Marec", "April", "May", "Jun", "Jul", "August", "September", "Oktober", "November", "December")

print("Tvorba kalendaru")

#ziskanie roku pre kalendar a ziskanie iba roku
while True:
    print("Zadaj rok pre kalendar: ")
    odpoved = input()
    
    if odpoved.isdecimal() and int(odpoved) > 0:
        rok = int(odpoved)
        break
    
    #ak je odpoved ina ako pozadovany format:
    print("Zla odpoved! Zadaj spravny rok ako je napriklad 2023. ")
    continue

    
while True:
    print("Zadaj mesiac pre kalendar ale len ako cislo od 1 po 12: ")
    odpoved = input()
    
    if not odpoved.isdecimal():
        print("Zadaj ciselnu hodnotu pre mesiac ako je napriklad 1 pre Januar. ")
        continue
    
    mesiac = int(odpoved)
    if 1 <= mesiac <= 12:
        break
    
    print("Zadaj hodnotu od 1 po 12")

def getKalendarPre(rok, mesiac):
    text = "" #premenna obsahuje prazdny string pre vyplnenie
    
    #pridanie mesiacu a datumu na vrch kalendaru
    text += (" "*34)+MESIACE[mesiac - 1] + " " + str(rok) + "\n"
    
    #pridanie dni pre tyzden do kalendara
    text += "..Pondelok....Utorok....Streda.....Stvrtok....Piatok.....Sobota.....Nedela..\n"
    
    #Horizontalna ciara ktora predeluje tyzdne
    tyzdenDelenie = ("+----------"*7)+"\n"
    
    #Prazdny riadok pre delenie dni
    prazdnyRiadok = ("|          " * 7) + "|\n"
    
    #ziskanie prveho dna v mesiaci
    sucasnyDatum = datetime.date(rok, mesiac, 1)
    
    # kedze tyzden zacina v pondelok nastavi sa hodnota 0 pre pondelok a nasledne sa pokracuje podla nej
    while sucasnyDatum.weekday() != 0:
        sucasnyDatum -= datetime.timedelta(days=1)
        
    #loop pre pre kazdy tyzden v mesiaci
    while True:
        text += tyzdenDelenie
        
        #denPocetRiadok je premenna v ktorej su oznacene dni v tyzdni
        denPocetRiadok = ""
        
        for i in range(7):
            denCisloLabel = str(sucasnyDatum.day).rjust(2)
            denPocetRiadok += "|" + denCisloLabel + (" " * 8)
            sucasnyDatum += datetime.timedelta(days=1) #prejdenie k dalsiemu dnu
        
        denPocetRiadok += "|\n" #pridanie verikalnych ciar
        
        #Pridanie cisla pre pocet riadkov a pridanie 3 prazdnych riadkov pre text kalendar
        text += denPocetRiadok
        for i in range(3):
            text += prazdnyRiadok
            
        #urcenie ci sme stale v tom istom mesiaci
        if sucasnyDatum.month != mesiac:
            break
        
    #pridanie horizontalnej ciary na spodku kalendara
    text += tyzdenDelenie
    return text

text = getKalendarPre(rok, mesiac)
print(text)

#ulozenie suboru ako txt
kalendarMeno = "kalendar_{}_{}.txt".format(rok, mesiac)
with open(kalendarMeno, "w") as fileObj:
    fileObj.write(text)
    
print("Ulozenie do suboru: " + kalendarMeno)

