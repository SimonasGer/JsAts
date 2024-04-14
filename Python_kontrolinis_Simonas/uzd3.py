# Norint įvykdyti užduotį reikalingas math modulis
import math

# Programos naudojimo metu įvedama reikalinga informacija
baudosDydis = float(input("Koks baudos dydis eurais? "))*100
baudosDydis = int(baudosDydis)

# Apskaičiuojamas centų svoris
kg = baudosDydis * 0.0023

# Apskaičiuojamas centų bokšto aukšis
aukstis = baudosDydis * 0.00167

# Apskaičiuojama centų kvadrato kraštinė 
krastine = int(math.floor(math.sqrt(baudosDydis)))

# Apskaičiuojama iš kiek centų susidaro centų kvadratas
kvadratas = krastine**2

# Apskaičiuojama kiek centų liks nepanaudota centų kvadrate
nepanaudota = baudosDydis - kvadratas

# Apskaičiuojamas centų kvadrato plotas
plotas = 0.01625**2 * kvadratas

# Atsakymas atspausdinamas, dydžiai suapvalinti 
print(f"""Monetos svers {kg:.3f} kilogramų, iš jų pastatytas bokštas bus {aukstis:.2f} metrų aukščio,
kvadratui sudaryti prireiks {kvadratas} monetų, jo kraštinei - {krastine}, atliks {nepanaudota}, 
kvadrato plotas bus {plotas:.4f} kvadratinai metrai""")