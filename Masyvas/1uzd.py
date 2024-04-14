# 3. Masyvas nuskaitomas iš bylos duom.txt. Parašykite programą, kuri apskaičiuotų  didžiausio ir mažiausio teigiamų  elementų  sumą  
# ir  ja  pakeistu  visus mažiausius   masyvo   elementus. Rezultatas spausdinamas    byloje rez.txt.    Byloje    
# pateiktas pradinis masyvas; didžiausias ir mažiausias teigiami elementai; elementų, kurie bus pakeisti numeriai; ir naujas masyvas.

masyvas1 = open("duom.txt", "r").read().split(",")
intMasyvas1 = []
for i in masyvas1:
    intMasyvas1.append(int(i))
masyvas2 = masyvas1.copy()
minIndex = []
min = max = intMasyvas1[0]
index = 0
for i in intMasyvas1:
    if min > i:
        min = i
    if max < i:
        max = i
print(min, max)
sum = min + max

for i in intMasyvas1:
    if i == min:
        minIndex.append(str(index))
        masyvas2[index] = sum
    index += 1
print(intMasyvas1)
print(masyvas1)
print(masyvas2)
print(minIndex)

with open('rez.txt', 'a') as f:
    f.write("Originalus masyvas: " + ', '.join(str(x) for x in masyvas1) + 
            '\nDidziausias masyvo elementas - ' + str(max) + " , o maziausias - " + str(min) 
            + "\nElementu, kurie keiciami, numerai: " + ', '.join(str(x) for x in minIndex) + 
            "\nNaujas masyvas: " + ', '.join(str(x) for x in masyvas2) + "\n" + "\n")
    
    
