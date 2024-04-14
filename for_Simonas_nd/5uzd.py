# Autobusų parko administracija nusprendė keleiviams, kurių bilietų numeriai laimingi, dovanoti kelionę už pusę kainos. Autobuso bilietas laikomas laimingu, 
# jei jo pirmųjų trijų skaitmenų trejetas sutampa su paskutinių trijų skaitmenų trejetu (pvz., laimingas bilietas, kurio numeris yra 234234). Autobusų parko administracija 
# nutarė bilietus sunumeruoti nuo m-tojo iki n-tojo šešiaženklio skaičiaus. Parašykite programą, kuri apskaičiuotų, kiek keleivių įsigis laimingus bilietus. 
# Pasitikrinkite. Kai m = 170849, o n = 189965, turi būti išvesta: Laimingus bilietus įsigijo 19 keleivių.

m = int(input("Pirmo bilieto numeris "))
n = int(input("Paskutinio bilieto numeris "))
sum = 0
for i in range(m, n + 1):
    sk1 = i // 1000
    sk2 = i % 1000
    if sk1 == sk2:
        sum +=1
print(f"Laimingus bilietus įsigijo {sum} keleivių")