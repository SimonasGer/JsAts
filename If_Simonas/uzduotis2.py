# Įvedami reikalaujami skaičiai
p1 = int(input("Įveskite pirmą Petriuko pažymį "))
p2 = int(input("Įveskite antrą Petriuko pažymį "))
p3 = int(input("Įveskite trečią Petriuko pažymį "))
p4 = int(input("Įveskite ketvirtą Petriuko pažymį "))
p5 = int(input("Įveskite penktą Petriuko pažymį "))

# Apskaičiuojamas pažymių vidurkis
vid = (p1 + p2 + p3 + p4 + p5) / 5

# Patikrinama ar įvesti skaičiai yra teisingi
if 1 <= (p1 or p2 or p3 or p4 or p5) <= 10:
    # Nustatoma kiek saldainių Petriukas gaus
    if vid > 9:
        print("Petriukas gaus tris saldainius")
    elif 7 <= vid <= 9:
        print("Petriukas gaus du saldainius")
    else:
        print("Petriukas gaus vieną saldainį")
else:
    print("Netinkami duomenys")

    