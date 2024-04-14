# Parašytą pinigų sumą skaičiumi –eurus užrašykite žodžiais, o centus –skaičiumi. Skaičius ne didesnis kaip 100 000. Pav.: 
# Įvedus 25.31 spausdinamas rezultatas: Dvidešimt penki eurai 31centas; 
# Įvedus 1254.25 spausdins: Vienas tūkstantis du šimtai penkiasdešimt keturi eurai 25 centai
# Įvedus 10304.05 spausdins: Dešimt tūkstančių trys šimtai keturi eurai 5 centai
# Nepamirškite, galima naudoti match-case sakinį 
# Funkcijas naudokite savo nuožiūraGalima duomenis suvedinėti klaviatūra, o rezultatus spausdinti ekrane

skaicius = input("Įveskite pinigų sumą skaičiais ")
i = len(skaicius)
if skaicius[-3] != ".":
    i += 3
while i < 9:
    skaicius = "0" + skaicius
    i += 1
cent = skaicius[6:9]
vien = skaicius[3:6]
tukst = skaicius[0:3]
if skaicius[-3] != ".":
    cent = "000"
print(skaicius)
def moneta(nr, mon):
    segment = ""
    if nr == "000":
        return ""
    if nr[1] == "1" or nr[2] == "0":
        if mon == "tūkstan":
            segment = mon + "čių " + segment
        else:
            segment = mon + "ų " + segment
    else:
        if nr[2] == "1":
            if mon == "tūkstan":
                segment = mon + "tis " + segment
            else:
                segment = mon + "as " + segment
        else:
            if mon == "tūkstan":
                segment = mon + "čiai " + segment
            else:
                segment = mon + "ai " + segment
    if mon == "cent":
        segment = nr[1:3] + " " + segment
        return segment
    else:
        return segment

def first(nr):
    segment = ""
    match nr[0]:
        case "1": segment = "vienas " + segment
        case "2": segment = "du " + segment
        case "3": segment = "trys " + segment
        case "4": segment = "keturi " + segment
        case "5": segment = "penki " + segment
        case "6": segment = "šeši " + segment
        case "7": segment = "septyni " + segment
        case "8": segment = "aštuoni " + segment
        case "9": segment = "devyni " + segment
    return segment

def teen(nr):
    segment = ""
    match nr:
        case "1": segment = "vienuolika " + segment
        case "2": segment = "dvylika " + segment
        case "3": segment = "trylika " + segment
        case "4": segment = "keturiolika " + segment
        case "5": segment = "penkiolika " + segment
        case "6": segment = "šešiolika " + segment
        case "7": segment = "septyniolika " + segment
        case "8": segment = "aštuoniolia " + segment
        case "9": segment = "devyniolika " + segment
    return segment

def second(nr):
    segment = ""
    match nr:
        case "1": segment = "dešimt " + segment
        case "2": segment = "dvidešimt " + segment
        case "3": segment = "trisdešimt " + segment
        case "4": segment = "keturiasdešimt " + segment
        case "5": segment = "penkiasdešimt " + segment
        case "6": segment = "šešiasdešimt " + segment
        case "7": segment = "septyniasdešimt " + segment
        case "8": segment = "aštuoniasdešimt " + segment
        case "9": segment = "devyniasdešimt " + segment
    return segment

def simt(nr):
    if nr[0] == "1":
        return "šimtas "
    elif nr[0] == "0":
        return ""
    else:
        return "šimtai "

def kint(nr):
    if nr[1] == "1":
        return teen(nr[2]) 
    else: 
        return second(nr[1]) + first(nr[2])

zodziai = first(tukst) + simt(tukst) + kint(tukst) + moneta(tukst, "tūkstan") + first(vien) + simt(vien) + kint(vien) + moneta(vien, "eur") + moneta(cent, "cent")
print(zodziai)


            
            