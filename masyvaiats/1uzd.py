# 1. Įvedamas masyvas. Parašykite programą, kuri apskaičiuotų masyvo neigiamų lyginių elementų vidurkį.

skaiciai = input("Įveskite skaičių masyvą, skaičius atskiriant tarpais ")
skaiciai = skaiciai.split(" ")
skaiciai = [int(i) for i in skaiciai]
sum = 0
sk = 0
for i in skaiciai:
    if i < 0 and i % 2 == 0:
        sum += i
        sk += 1
avg = sum / sk
print(avg)