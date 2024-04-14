# 3. Tekstinėje  byloje  duomA.txt  surašyti  masyvo  A elementai,  o  duomB.txt surašyti masyvo B elementai Nuskaityti  šiuos  
# masyvus,  surasti  jų  didžiausius  ir mažiausius  elementus.  Sukurti  naujus  masyvus, kuriuose   yra  pašalinti  visi  didžiausi  
# ir  mažiausi elementai.Rezultatų  byloje  turi  būti  atspausdinti masyvai A ir B prieš pakeitimą, atitinkamai jų didžiausi ir 
# mažiausi elementai ir nauji masyvai A ir B.Programa parašyta su funkcijomis:a)Duomenų skaitymas;b)Didžiausio radimas;c)Mažiausio 
# radimas;d)
# Rezultatų išvedimas ---------------------------------------------------------------
# Pav.A{5 8 -9 7 2 14 -9 8 14}  maxA=14, minA=-9B{9 8 7 -1 2 -1 4 9}maxB=9, minB=-1Po pakeitimų turėsimeA{5 8 7 2 8}B{8 72 4}

def skaitymas(failas):
    masyvas = []
    for i in open(failas, "r").read().split(","):
        masyvas.append(int(i))
    return masyvas

def maximum(masyvas):
    max = masyvas[0]
    for i in masyvas:
        if max < i:
            max = i
    return max

def minimum(masyvas):
    min = masyvas[0]
    for i in masyvas:
        if min > i:
            min = i
    return min

def pluck(masyvas):
    newMasyvas = []
    for i in masyvas:
        if i != minimum(masyvas) and i != maximum(masyvas):
            newMasyvas.append(i)
    return newMasyvas

def isvedimas():
    with open('rez2.txt', 'a') as f:
        f.write("A{" + ', '.join(str(x) for x in masyvas1) + "} max A - " + str(maximum(masyvas1)) + ", min A - " + str(minimum(masyvas1)) +
                "\nB{" + ', '.join(str(x) for x in masyvas2) + "} max A - " + str(maximum(masyvas2)) + ", min A - " + str(minimum(masyvas2)) + 
                ".\nPo pakeitimu turesime A{" + ", " .join(str(x) for x in pluck(masyvas1)) + "} ir B{" + ", " .join(str(x) for x in pluck(masyvas2)) + "}\n")

masyvas1 = skaitymas("duomA.txt")
masyvas2 = skaitymas("duomB.txt")
isvedimas()