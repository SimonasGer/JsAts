# Importuojamas math modulis
import math

# Funkcija, kuri patikrina ar įvesta matematinė operacija yra galima
def op(vk):
    if vk == "+" or vk == "-" or vk == "*" or vk == "/" or vk == "^" or vk == "q":
        return vk
    else:
        vk = input('Operacija netinkama, bandykite dar kartą ')
        return op(vk)

# Funkcija, kuri prašo įvestį antrą skaičių
def sk2():
    if vk != "q":
        sk2 = int(input('Iveskite antra skaiciu '))
        return sk2
    
# Funkcija kuri atspausdina atsakymą, kai visi įvesti duomenys naudojami
def atsakymas():
    print(f"{sk1} {vk} {sk} = {ats}")

# Įvedamas pirmas, antras skaičius ir matematinė operacija
sk1 = int(input('Iveskite pirma skaiciu '))    
vk = input('Įveskite norimą matematinę operaciją ')
vk = op(vk)
sk = sk2()

# Atspausdinamas atsakymas
if vk == '+':
    ats = sk1 + sk
    atsakymas()
elif vk == '-':
    ats = sk1 - sk
    atsakymas()
elif vk == '*':
    ats = sk1 * sk
    atsakymas()
elif vk == '^':
    ats = sk1 ** sk
    atsakymas()
elif vk == '/':
    if sk == 0:
        print("Dalyba iš nulio negalima")
    else:
        ats = sk1 / sk
        atsakymas()
elif vk == 'q':
    if sk1 < 0:
        print("Šaknies traukimas iš neigiamo skaičiaus negalimas")
    else:
        ats = math.sqrt(sk1)
        print(f"Skaičiaus {sk1} šaknis yra {ats}")
else:
    print('klaida')