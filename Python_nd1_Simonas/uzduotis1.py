# Sraigė per pirmą minutę nušliaužė x1 centimetrų ir y1 milimetrų, o per antrą minutę – x2 centimetrų ir y2 milimetrų. 
# Parašykite programą, kuri apskaičiuotų, kokį atstumą sraigė nušliaužė per 2 minutes?

x1 = int(input('Įveskite kiek centimetru sraigė nušliaužė per pirmą minutę '))
y1 = int(input('Įveskite kiek milimetrų sraigė nušliaužė per pirmą minutę '))
x2 = int(input('Įveskite kiek centimetru sraigė nušliaužė per antrą minutę '))
y2 = int(input('Įveskite kiek milimetrų sraigė nušliaužė per antrą minutę '))

total = 10*(x1+x2)+y1+y2 # Apskaičiuojamas visas kelias milimetrais
cm = total // 10 # Benrą kelią dalinant be liekanos iš 10 gaunami centimetrai
mm = total % 10 # Benro kelio liekana dalinant iš 10 yra milimetrai

print(f"Sraigė nušliaužė {cm} cm. ir {mm} mm.kelio") # Atsakymas atspaudinamas

