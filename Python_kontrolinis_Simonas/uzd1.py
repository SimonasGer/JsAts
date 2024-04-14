# Norint įvykdyti užduotį reikalinga math modulio ceil funkcija
import math

# Programos naudojimo metu įvedama reikalinga informacija
plytelesIlgis = int(input("Koks yra plytelės ilgis? (centimetrais, sveikas skaičius) "))
garazoIlgis = float(input("Koks yra garažo ilgis? (metrais, realus skaičius) "))
plytelesPlotis = int(input("Koks yra plytelės plotis? (centimetrais, sveikas skaičius) "))
garazoPlotis = float(input("Koks yra garažo plotis? (metrais, realus skaičius) "))
plyteliuSkaiciusPakuoteje = int(input("Kiek plytelių yra vienoje pakuotėje? (Sveikas skaičius) "))
vienoMKaina = float(input("Kiek kainuoja vienas kvadratinis metras plytelių? (Eurais, realus skaičius) "))

# Apskaičiuojama kiek prireiks plytelių iš ilgio
ilgisSk = (garazoIlgis*100 / plytelesIlgis)
ilgisSk = math.ceil((garazoIlgis*100 / plytelesIlgis)+(math.ceil(ilgisSk-1))*0.02)

# Apskaičiuojama kiek prireiks plytelių iš pločio
plotisSk = (garazoIlgis*100 / plytelesIlgis)
plotisSk = math.ceil((garazoPlotis*100 / plytelesPlotis)+(math.ceil(plotisSk-1))*0.02)

# Apskaičiuojama kiek reikia plytelių
plytelesSk = ilgisSk * plotisSk

# Apskaičiuojama kiek prireiks plytelių pakuočių
pakuotesSk = math.ceil(plytelesSk / plyteliuSkaiciusPakuoteje)

# Apskaičiuojama pakuotės kaina
pakuotesKaina = ((plytelesIlgis * plytelesPlotis * plyteliuSkaiciusPakuoteje) / 10000) * vienoMKaina

# Apskaičiuojama plytelių kaina
kaina = pakuotesKaina * pakuotesSk

# Apskaičiuojama kiek plytelių atliks
nPlyteles = pakuotesSk * plyteliuSkaiciusPakuoteje - plytelesSk

# Apskaičiuojama kokia atlikusių plytelių kaina
nPlytelesKaina = ((nPlyteles * plytelesIlgis * plytelesPlotis)/10000) * vienoMKaina

# Atspausdinamas rezultatas
print(f"""Plytelių iš ilgio prireiks {ilgisSk}, iš pločio - {plotisSk}, iš viso prireiks {plytelesSk}, prireiks {pakuotesSk} pakuočių, 
plytelės kainuos {kaina} eurų, atliks {nPlyteles} ir jos kainuos {nPlytelesKaina} eurus""")