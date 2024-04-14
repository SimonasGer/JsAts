# Vienu smūgiu stalius įkala vinį į k cm gylį. Parašykite programą, kuri išspausdintu plaktuko dūžį "Tuk!" su kiekvienu smūgiu, šalia smūgio numerį ir kiek 
# vinies ilgio dar liko neįkaltos. Kalamos vinies ilgis n cm. Baigus kalti vinį, pranešama "Vinis įkalta".

# Importuojamas math modulis, nes reikalinga math.ceil funkcija
import math
def kalimas():
    # Įvedami duomenys
    vinis = float(input("Koks vinies ilgis centimetrais? "))
    tuk = float(input("Kiek centimetrų vinies įkala vienas plaktuko smūgis? "))
    if vinis <= 0 or tuk <= 0:
        # Jeigu įvesti duomenys negalimi, prašome juos įvesti dar kartą
        print("klaida, įveskite dar kartą")
        kalimas()
    else:
        # Apskaičiuojamas dūžių skaičius
        sk = math.ceil(vinis / tuk) + 1
        # Atspausdinamas plaktuko dūžių skaičius ir likusios įkalti vinies ilgis
        for i in range(1, sk):
            vinis -= tuk
            if vinis > 0:
                print (f"Tuk! smūgis {i}, dar neįkalta liko {vinis:.2f} cm vinies")
            else:
                print (f"Tuk! smūgis {i}, vinis įkalta")
# Paleidžiama funkcija
kalimas()

