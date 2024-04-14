# Programa prašo įvesti sveiką teigiamą skaičių n (tarkim 100). Programa sugeneruoja atsitiktinį skaičių nuo 1 iki n. Sugeneravus 
# atsitiktinį skaičių vartotojui siūloma atspėti kokį skaičių sugeneravo programa. Įvedus spėjamą skaičių(tarkim  75)programa praneša 
# ar sugeneruotas skaičius didesnis ar mažesnis už įvestą skaičių ir siūlo spėti dar kartą (tarkim „Sugeneruotas skaičius didesnisuž 75.
# Atliksite 3 spėjimą...“). Įvedus didesnius skaičius už n ar neigiamus skaičius programa prašo kartoti įvedimą ir jo neprisumuoja prie 
# spėjimų skaičiaus. Vartotojui atspėjus skaičių-pranešimas, koks buvo sugeneruotas skaičius ir kiek spėjimų buvo atlikta ir kiek buvo 
# bandymų įvesti netinkamą skaičių.Pabaigus žaidimą – siūloma sužaisti dar kartą.
import random
def zaidimas():
    n = int(input("Įveskite sveiką skaičių "))
    ivedimas = 1
    skaicius = random.randint(1, n)
    print(skaicius)
    while True:
        spejimas = int(input(f" įveskite spėjimą {ivedimas} "))
        ivedimas += 1
        if not 0 < spejimas <= n:
            print("Klaida, kartokite įvedimą")
            ivedimas -= 1
            continue
        if skaicius > spejimas:
            print(f"Sugeneruotas skaičius didesnis už spėjimą,", end = "")
        if skaicius < spejimas:
            print(f"Sugeneruotas skaičius mažesnis už spėjimą,", end = "")
        if spejimas == skaicius:
            print(f"Sugeneruotas skaičius - {skaicius}, atlikote {ivedimas} spėjimų")
            kartojimas = input("Ar norite žaisti? (t/n) ")
            if kartojimas == "t":
                zaidimas()
            break
        if not 0 < spejimas <= n:
            print("Klaida, kartokite įvedimą")
            continue
        
zaidimas()