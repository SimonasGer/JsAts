# Parašykite programą simpatiškajai eilutei 7 + 77 + 777 + ... apskaičiuoti. Pradinis duomuo – paskutinio nario septynetų skaičius.

nariai = int(input("Įveskite skaičių "))
sum = 0
sk = 0
sk1 = 0
for i in range(0, nariai):
    sk = (7*10**i)
    sk += sk1
    if i < nariai - 1:
        print (sk, end = " + ")
    else:
        print(sk, end = " = ")
    sum += sk
    sk1 = sk
print(sum)