# Sukurkite programą arba funkciją, nuskaitytų iš tekstinės bylos slaptažodžius  ir patikrintų, ar jieatitinka šiuos reikalavimus:
# 1.Turi turėti mažiausiai 12 simbolių.
# 2.Turi turėti bent 2 didžiąsiasraidės.
# 3.Turi turėti bent 2 mažąsiasraidės.
# 4.Turi turėti bent 2 skaičius.
# 5.Turi turėti bent 2 spec. simbolius (pvz., !, @, #, $ ir kt.).
# Programa turi grąžinti pranešimą, kuriame būtų nurodyta, ar slaptažodis yra tinkamas, ir jei ne, tai kokios konkrečios savybės jam 
# trūksta.
# Duom4.txt              Rez4.txt
# ManoSlaptazodis123@    Netinkamas. Trūksta  1 spec. simbolio(ų)
# asED15*+              Netinkamas. Slaptažodis per trumpas

txt = open("duom4.txt", "r", encoding="utf-8").read()
slaptazodziai = txt.split("\n")
characters = "AĄBCČDEĘĖFGHIĮJKLMNOPQRSŠTUŲŪVWXYZŽaąbcčdeęėfghiįjklmnopqrsštuųūvwxyzž0123456789"
requirements = ["upper", "lower", "number", "symbol"]

def length(passwd):
    if len(passwd) < 12:
        return "Netinkamas. Slaptažodis per trumpas. "
    return ""
    
def error(passwd, funk):
    symb = crit(passwd, funk)
    reason = ""
    if symb < 2:
        if funk == "upper":
            reason = (" didžiųjų radžių") + reason
        if funk == "lower":
            reason = (" mažųjų radžių") + reason
        if funk == "number":
            reason = (" skaičių") + reason
        if funk == "symbol":
            reason = (" simbolių") + reason
        return (f"Netinkamas. Trūksta {2-symb} {reason}. ")
    return ""

def crit(passwd, funk):
    upper = 0
    for i in passwd:
        if func(i, funk):
            upper += 1
    return upper
    
def func(symbol, function):
    if function == "upper":
        return symbol.isupper()
    if function == "lower":
        return symbol.islower()
    if function == "number":
        return symbol.isnumeric()
    if function == "symbol":
        return symbol not in characters


for i in slaptazodziai:
    print(i)
    f = open("rez4.txt", "a", encoding = "utf-8")
    f.write(length(i))
    for j in requirements:
        f.write(error(i, j))
    f.write("\n")
