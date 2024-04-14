# Programos naudojimo metu įvedama reikalinga informacija
isvykoVal = int(input("Kiek buvo valandų kai Petriukas išvyko? "))
isvykoMin = int(input("Kiek minučių? "))
atvykoVal = int(input("Kiek buvo valandų kai Petriukas atvyko "))
atvykoMin = int(input("Kiek minučių "))

# Apskaičiuojamas kelionės laikas minutėmis
min = atvykoVal * 60 + atvykoMin - isvykoVal * 60 + isvykoMin

# Kelionės laikas paverčiamas į valandas ir minutes
val = min // 60
min = min - 60 * val

# Atsakymas atspaudinamas
print (f"Petriukas keliavo {val} valandų ir {min} minučių")
