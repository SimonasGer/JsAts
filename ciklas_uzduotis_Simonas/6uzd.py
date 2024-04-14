# Pradiniai duomenys – natūralusis skaičius N. Sudarykite programą patikrinančia, ar šis skaičius yra iš eilės einančių 
# skaičių(1+2+3+4+5+6+7....)suma.

n = int(input("Įveskite skaičių "))
sum = 0
sk = 1
while sum < n:
    sum += sk
    if sum >= n:
        print(f"{sk} = {sum}")
        if sum == n:
            print("TAIP")
        elif sum > n:
            print("NE")
    else:
        print(sk, end = " + ")
    sk += 1
    