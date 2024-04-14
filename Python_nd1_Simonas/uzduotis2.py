# Vandens saugykloje yra v kubinių metrų vandens (realusis skaičius). Saugyklos vandenį vartoja n žmonių. 
# Vienas žmogus per parą vidutiniškai sunaudoja vv kubinių metrų vandens (realusis skaičius). 

# Parašykite programą, kuri apskaičiuotų, kelioms paroms pužteks saugykloje esančio vandens.

v = float(input('Įveskite kiek vandens saugykloje yra kubinių metrų vandens '))
n = int(input('Įveskite kiek žmonių vartoja vandenį '))
vv = float(input('Įveskite kiek kubinių metrų vandens vienas žmogus vidutiniškai suvartoja per parą '))

days = v/(n*vv) # Atsakymo formulė

print(f"Saugykloje esančio vandens užteks {round(days,3)} paroms") # Atsakymas atspaudinamas
