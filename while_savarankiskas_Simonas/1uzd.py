# Suprogramuokite programinę įrangą kavos aparatui. Pradinė kavos kaina įvedama klaviatūra.  Kaina nurodoma eurais (tarkim 2.20). Nurodžius kavos kainą, prašoma mesti monetą. 
# Kavos aparatas priima 10, 20, 50 centų arba 1, 2 eurus (klaviatūra įvedamas skaičius 10 arba 20 arba 50 arba 1 arba 2) Įmetus tinkamą monetą (tarkim 1),parodomas 
# pranešimas, kiek liko sumokėti (tarkim 1.20) ir prašoma mesti monetą dar. Įmetus tinkamą monetą (tarkim 2),kavos aparatas išveda pranešimą: Grąža (tarkim 80 centų arba 
# tarkim 1.20euro) ir palinkima „Skanios kavos“.Įmetus netinkamą monetą (tarkim 58 ),išvedamas pranešimas „Netinkama moneta. Meskite dar kartą“. Suskaičiuoti ir išvesti 
# pabaigoje, kiek buvo bandymų įmesti „padirbtą“ monetą ir kiek kartų buvo metama „tikra“ moneta

kaina = float(input("Įmeskite kavos kainą "))
pinigai = 0
tMonetos = 0
nMonetos = 0
while pinigai < kaina:
    moneta = int(input("Įmeskite monetą "))
    if moneta == 1 or moneta == 2:
        moneta *= 100
    if moneta == 10 or moneta == 20 or moneta == 50 or moneta == 100 or moneta == 200:
        pinigai += (moneta / 100)
        tMonetos +=1
        graza = kaina - pinigai
        if (graza) < 0:
            print(f"Sumokėta, grąža {-graza:.2f} eur, iš duotų monetų tinkamos {tMonetos}, netinkamos {nMonetos}")
        else:
            print(f"Liko sumokėti {graza:.2f}, įmeskite monetą")
    else:
        nMonetos += 1
        print("Netinkama moneta. Meskite dar kartą.")