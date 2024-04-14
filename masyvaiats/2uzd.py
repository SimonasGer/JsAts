# 2. Parduotuvėje yra n skirtingų prekių. Į masyvą A(n) surašyta, kiek yra vienetų kiekvienos prekės. Distributorius dar atveža 
# kiekvienos prekės po tam tikrą kiekį vienetų. Duomenys kiek atveža pateikti masyve B(n). Rasti kiek parduotuvėje yra kiekvienos 
# prekės vienetų.

A = input("Įveskite prekių skaičių parduotuvėje, skaičius atskiriant tarpais ")
A = A.split(" ")
A = [int(i) for i in A]
B = input("Įveskite atvežtų prekių skaičių, skaičius atskiriant tarpais ")
B = B.split(" ")
B = [int(i) for i in B]
sk = 0
for i in A:
    item = i + B[sk]
    sk += 1
    print(f"{sk} prekių yra {item}")
    
