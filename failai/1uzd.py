# Suvedam sveiką teigiamą skaičių n (tarkim 100). Programa sugeneruoja atsitiktinį skaičių nuo 1 iki n Sugeneravus atsitiktinį skaičių 
# vartotojui siūloma atspėti kokį skaičių sugeneravo programa. Įvedus spėjamą skaičių (tarkim 75) programa praneša ar sugeneruotas 
# skaičius didesnis ar mažesnis už įvestą skaičių ir siūlo spėti dar kartą (tarkim „Sugeneruotas skaičius didesnis už 75. Atliksite 3 
# spėjimą...“). Įvedus bet kokius simbolius ar neigiamus skaičius programa prašo kartoti įvedimą ir jo neprisumuoja prie spėjimų 
# skaičiaus. Vartotojui atspėjus skaičių rodomas pranešimas, koks buvo sugeneruotas skaičius ir kiek spėjimų buvo atlikta. Pabaigus 
# žaidimą –siūloma sužaisti dar kartą. Žaidimo programavime panaudoti funkcijasBe žaidimo paslaugos programa sukuria žaidimo 
# „registravimo“ failą reg.txt, kuriame yra pateikiama informacija apie žaidimo eigą. Pav.Vartotojas įvedė skaičių 100.Sugeneruotas 
# atsitiktinis skaičius 56.1 spėjimu vartotojas įvedė 85. Atsakymas –sugeneruotas skaičius mažesnis2 spėjimu vartotojas įvedė 50. 
# Atsakymas –sugeneruotas skaičius didesnis3 spėjimu vartotojas įvedė 59. Atsakymas –
# sugeneruotas skaičius mažesnis........................................................................................................
# ..........5 spėjimu vartotojas atspėjo skaičiųĮ užklausą „Ar žaisite dar“ pasirinko „Taip“Vartotojas įvedė skaičių 50.Sugeneruotas 
# atsitiktinis skaičius 26.................Į užklausą „Ar žaisite dar“ pasirinko „Ne“Vartotojas žaidė 2 kartus(ų)
import random
def zaidimas():
    f = open("skaiciai.txt", "a")
    n = int(input("Įveskite sveiką skaičių "))
    f.write("Vartotojas ivede skaiciu " + str(n) + "\n")
    ivedimas = 1
    kartas = 1
    skaicius = random.randint(1, n)
    print(skaicius)
    while True:
        spejimas = int(input(f" įveskite spėjimą {ivedimas} "))
        f.write(str(ivedimas) + " spejimu vartotojas ivede " + str(spejimas) + " ")
        ivedimas += 1
        if not 0 < spejimas <= n:
            print("Klaida, kartokite įvedimą")
            ivedimas -= 1
            continue
        if skaicius > spejimas:
            print(f"Sugeneruotas skaičius didesnis už spėjimą,", end = "")
            f.write("sugeneruoutas skaicius didesnis uz spejima.\n")
            continue
        if skaicius < spejimas:
            print(f"Sugeneruotas skaičius mažesnis už spėjimą,", end = "")
            f.write("sugeneruoutas skaicius mazesnis uz spejima.\n")
            continue
        if not 0 < spejimas <= n:
            print("Klaida, kartokite įvedimą")
            f.write("sugeneruoutas skaicius netinkamas.\n")
            continue
        if spejimas == skaicius:
            print(f"Sugeneruotas skaičius - {skaicius}, atlikote {ivedimas-1} spėjimų")
            f.write("\n" + str(ivedimas-1) + " spejimu atspejote skaiciu\n")
            kartojimas = input("Ar norite žaisti? (t/n) ")
            if kartojimas == "t":
                f.write("Zaidziate dar karta\n")
                kartas += 1
                zaidimas()
            elif kartojimas == "n":
                print(f"Zaidete {kartas} kartu")
                f.write("Zaidimas zaidete " + str(kartas) + " kartu\n")
        break
        
zaidimas()