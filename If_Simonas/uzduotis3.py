# Įvedami duomenys
b7 = int(input("Įveskitę pirmą dvejetainio kodo skaičių "))
b6 = int(input("Įveskitę antrą dvejetainio kodo skaičių "))
b5 = int(input("Įveskitę trečią dvejetainio kodo skaičių "))
b4 = int(input("Įveskitę ketvirtą dvejetainio kodo skaičių "))
b3 = int(input("Įveskitę penktą dvejetainio kodo skaičių "))
b2 = int(input("Įveskitę šeštą dvejetainio kodo skaičių "))
b1 = int(input("Įveskitę septintą dvejetainio kodo skaičių "))
b0 = int(input("Įveskitę aštuntą dvejetainio kodo skaičių "))

# Patikrinama ar įvestos vertės teisingos ir invertuojamos jeigu reikia
if (b7 == 1 or b7 == 0) and (b6 == 1 or b6 == 0) and (b5 == 1 or b5 == 0) and (b4 == 1 or b4 == 0) and (b3 == 1 or b3 == 0) and (b2 == 1 or b2 == 0) and (b1 == 1 or b1 == 0) and (b0 == 1 or b0 == 0):
    if b7 == 1:
        if b6 == 1:
            b6 = 0
        else:
            b6 = 1
        if b5 == 1:
            b5 = 0
        else:
            b5 = 1
        if b4 == 1:
            b4 = 0
        else:
            b4 = 1
        if b3 == 1:
            b3 = 0
        else:
            b3 = 1
        if b2 == 1:
            b2 = 0
        else:
            b2 = 1
        if b1 == 1:
            b1 = 0
        else:
            b1 = 1
        if b0 == 1:
            b0 = 0
        else:
            b0 = 1
else:
    print("klaida")

# Patikrinama, kuri formulė naudojama apskaičiuoti rezultatui
if b7 == 0:
    ats = (b6 * 64) + (b5 * 32) + (b4 * 16) + (b3 * 8) + (b2 * 4) + (b1 * 2) + (b0 * 1)
else:
    ats = -((b6 * 64) + (b5 * 32) + (b4 * 16) + (b3 * 8) + (b2 * 4) + (b1 * 2) + (b0 * 1) + 1)

# Atsakymas atspausdinamas
print(ats)
        