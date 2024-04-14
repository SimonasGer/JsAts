# Atsiradus raštui, kurį supranta visi raštingi žmonės, natūralu, kad atsirado poreikis ieškoti būdų, skirtų informacijai paslėpti 
# (užkoduoti). Pirmieji skaitymą „apsunkino" egiptiečiai, kurie vietoj raidžių naudojo savus hieroglifus, tačiau dariki šiol nėra aišku,
# ar taip buvo daroma dėl to, kad informaciją galėtų perskaityti tik tie, kam tas raštas skirtas, ar dėl kitų priežasčių. Tačiau yra 
# aišku, kad slaptaraštį tikrai naudojo žydų raštininkai. Vienas iš jų naudojamų slaptaraščių –ATBASH, kurio esmė, kad vietoj vienų 
# raidžių yra naudojamos kitos.Sukurkite  programą,  kuri  iššifruotų  eilutes,  užkoduotas  ATBASH  slaptaraščiu.  ATBASH slaptaraščio 
# esmė tokia, kad pirmoji pateiktos abėcėlės raidė atitinka paskutiniąją, antroji –priešpaskutinę ir t.t. Pavyzdžiui, lietuviškai 
# abėcėlei būtų pritaikomi tokie raidžių pakeitimai:ABCDEFGHIJKLMZYXWVUTSRQPONJūsų užduotis: sukurti programą, kuri 
# naudoja lotynišką 26 raidžių abėcėlę ir iššifruoja tekstiniame faile pateiktus sakinius (iššifruojama kiekviena faile pateikta eilutė).
# Programos duomenys: duomenų failo duom.txt n eilučių pateiktos ATBASH šifru užkoduotos eilutės. Programos rezultatai: rezultatų failo 
# rez.txt atskirose eilutėse surašytos iššifruotos duomenų faile buvusios eilutės (kiekvieną duomenų failo eilutę atitinka viena 
# rezultatų failo eilutė) Šifruojami tik lotyniškoje abėcėlėje esantys simboliai, jei eilutėje yra kitų simbolių –jie paliekami tokie,
# kokie yra.Atkreipkite dėmesį į tai, kad didžiosios raidės iššifravus lieka didžiosiomis. Atitinkamai ta pati taisyklė galioja ir 
# mažosioms raidėms.Naudokite lotynišką abėcėlę (26 raidžių).Šiame uždavinyje žodžiai atskiriami apatiniu brūkšneliu.

txt = open("1duom.txt", "r", encoding="utf-8").read()
abc = "ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz"
atbash = "ZYXWVUTSRQPONMLKJIHGFEDCBAzyxwvutsrqponmlkjihgfedcba"
reverse = ""
for i in txt:
    if i in abc:
        reverse += atbash[abc.find(i)]
    else:
        reverse += i
f = open("1rez.txt", "a")
f.write(reverse + "\n" + "\n")