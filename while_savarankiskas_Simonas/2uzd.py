# Įvedamas bet koks skaičius. Parašykite programą, kuri tą skaičių pavaizduotu žvaigždutėmis pradedant vienetais.

skaicius = int(input("Įmeskite skaičių "))
i = skaicius
while i != 0:
    j = i % 10
    while j != 0:
        j -= 1
        print("*", end="")
    i //= 10
    print("")