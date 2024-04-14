# Keturženklis skaičius turi tokią įdomią savybę: (30 + 25)2 = 3025. Reikia parašyti programą, kuri tikrintų ir išvestų visus keturženklius skaičius, pasižyminčius šia 
# savybe, ir suskaičiuotų jų kiekį.

for i in range (1000, 10000):
    sk1 = i // 100
    sk2 = i % 100
    if (sk1 + sk2)**2 == i:
        print(i)