# 2. Suprogramuokite seną kinų žaidimą lazdomis. Žaidžia du žaidėjai. Yra 10 lazdelių. Žaidėjai paeiliui ima nuo vienos iki trijų lazdų.
# Pirmas žaidimą pradeda kompiuterio atsitiktiniu būdu sugeneruotas žaidėjas (tai gali būti žaidėjas Nr.1 arba žaidėjas Nr.2, jei yra 
# suvedami žaidėjų vardai kompiuteris atsitiktiniu būdu parenkažaidėjo vardą)*.Žaidimas tęsiasi tol, kol nesibaigia lazdelės. Pralaimi 
# tas, kuris paėmė paskutinę lazdelę. Suprogramuokite  žaidimą taip, kad galėtų žaisti du žmonės. Žaidimo pradžioje yra 10 lazdelių*. 
# Kiekviename žaidimo etape atspausdinamas žaidėjo numeris, lazdelių skaičius, ir užklausa, kiek lazdelių paims žaidėjas. Nepamirškite 
# pakeisti žaidėjų eilės numerius ir mažinti lazdelių skaičių. Nepamirškite, pabaigoje išvesti laimėjusio žaidėjo numerio. Nepamirškite,
# kad žaidėjas negali paimti daugiau nei tris lazdeles (apsaugokite ir nuo 0 ir neigiamų skaičių), ir taip pat negali paimti lazdelių 
# daugiau nei liko. *Žaidimo detalės gali skirtis. Galime suvesti žaidėjų vardus. Galima keisti pradinį lazdelių skaičių. Be žaidimo 
# paslaugos programa sukuria žaidimo „registravimo“ failą reg.txt, kuriame yra pateikiama informacija apie žaidimo eigą. Pav.Žaidėjų 
# vardai: Algis ir Jonas.Lazdelių pasirinktas skaičius yra 12.Žaidimą pradeda JonasJonas paima 3 lazdeles. Liko 9Algis paima 3 lazdeles.
# Liko 6Jonas paima 2 lazdeles. Liko 4Algis paima 3 lazdeles. Liko 1Jonas paima 1 lazdeles. Liko 0Žaidimą laimėjo Algis.Į užklausą 
# „Ar žaisite dar“ pasirinko „Ne“Žaidimąžaidė 1kartą(us)
f = open("reg.txt", "a")
import random
pirmas = random.randint(0,1)
kartai = 0
while True:
    zaisti = input("ar zaisite (t/n)")
    if zaisti == "n":
        f.write("Zaidete " + str(kartai) + " kartus")
        break
    kartai += 1
    z1 = input("pirmo zaidejo vardas ")
    z2 = input("antro zaidejo vardas ")
    lazdeles = int(input("lazdeliu kiekis "))
    f.write("Zaideju vardai: " + z1 + " ir " + z2 + "\n")
    f.write("Lazdeliu yra: " + str(lazdeles) + "\n")
    pirmas = random.randint(0,1)
    if pirmas == 0:
            pirmas = z1
    else:
        pirmas = z2
    f.write("Zaidima pradeda " + pirmas + "\n")
    while True:
            traukimas = int(input(f"{pirmas} traukia iki 3 lazdeliu"))
            if 0 < traukimas <= 3:
                lazdeles -= traukimas
                print(lazdeles)
                f.write(pirmas + " traukia " + str(traukimas) + " ir lieka " + str(lazdeles) + "\n")
            else:
                continue
            if pirmas == z1:
                if lazdeles <= 0:
                    f.write("Laimejo " + z2)
                    break
                traukimas = int(input(f"{z2} traukia iki 3 lazdeliu"))
                f.write(z2)
            else:
                if lazdeles <= 0:
                    f.write("Laimejo " + z1)
                    break
                traukimas = int(input(f"{z1} traukia iki 3 lazdeliu"))
                f.write(z1)

            if 0 < traukimas <= 3:
                lazdeles -= traukimas
                print(lazdeles)
                f.write(" traukia " + str(traukimas) + " ir lieka " + str(lazdeles) + "\n")
                if lazdeles <= 0:
                    break
            else:
                    continue


    
