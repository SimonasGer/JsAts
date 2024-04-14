# Kartais žmonėms būna sunku prisiminti, kokia šiandien yra savaitės diena, o ir kalendorius ne visada būna po ranka. Parašykite programą, kuri išspausdintų vieno mėnesio 
# savaitės dienų sąrašą nuo a dienos iki b dienos, jei žinoma, kad mėnuo prasidėjo m-tąją savaitės dieną. 
# Savaitės dienos numeruojamos taip: 1-pirmadienis, 2-antradienis ... 7 - sekmadienis.

start = int(input("Įveskite, kurią savaitės dieną prasidėjo mėnuo "))
intervalStart = int(input("Įveskite dienų intervalo pradžią "))
intervalEnd = int(input("Įveskite dienų intervalo pabaigą "))
nDay = start
for i in range(1, intervalEnd + 1):
    if i < intervalStart:
        nDay += 1
        if nDay > 7:
            nDay = 1
        continue
    print (f"{i}-oji diena - {nDay}")
    nDay += 1
    if nDay > 7:
        nDay = 1