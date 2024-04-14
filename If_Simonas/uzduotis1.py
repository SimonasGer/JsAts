# Įvedami reikalaujami skaičiai
sk1 = int(input("Įveskite pirmą skaičių "))
sk2 = int(input("Įveskite antrą skaičių "))
sk3 = int(input("Įveskite trečią skaičių "))

# Randamas mažiausias skaičius iš trijų
min = sk1
if min > sk2:
    min = sk2
if min > sk3:
    min = sk3
    
# Iš visų skaičių sumos atėmus mažiausia gaunama didžiausio ir vidurinio skaičių suma
suma = sk1 + sk2 + sk3 - min
print(f"Didžiausio ir vidutinio suma yra {suma}")
