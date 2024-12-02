
"""
Identifikační údaje o autorovi projektu:
Jméno a Příjmení: Ondřej Hubert
tel.: 773 500 373
e-mail: ondrej.hubert@gmail.com
"""

print(40 * "-" + "\n")
# importuje modul os
import os

# definuje funkci pro výpočet všech priorit
def secti_priority(seznam):
    """
    Funkce převede písmena na čísla a vrátí jejich součet\n
    (a - z --> 1 - 26; A - Z --> 27 - 52)\n
    :param seznam: list písmen z ASCII
    """
    soucet_priorit = 0
    priorita = 0
    for char in seznam:
        char = str(char)
        if char.islower():
            priorita = ord(char) - (97 - 1)
            soucet_priorit += priorita
        elif char.isupper():
            priorita = ord(char) - (65 - 27)
            soucet_priorit += priorita
    return soucet_priorit


# získá cestu k adresáři s tímto programem
cesta_k_adresari = os.path.dirname(os.path.abspath(__file__))
batohy_nazev_souboru = "batohy_vstup.txt"
cesta_k_batohum = os.path.join(cesta_k_adresari, batohy_nazev_souboru)

# vypíše úvod programu (nadpisy + cesty)
nadpis_1 = "Vyhledání společných věcí v každém batohu"
print(nadpis_1)
print(len(nadpis_1) * "*" + "\n")
print(f"Cesta k aktuálně spuštěnému programu:\n{cesta_k_adresari}\n")
print(f"Cesta ke vstupnímu souboru s popisem batohů:\n{cesta_k_batohum}\n")

nadpis_2 = "Obsah batohů v první a ve druhé polovině (odděleno mezerou)"
print(nadpis_2)
print(len(nadpis_2) * "*")

# otevře zdrojový soubor jako "batohy" pro čtení a uloží do proměnné v něm obsažené řádky
with open(cesta_k_batohum, "r") as batohy:
    seznam_batohu_s_escape = batohy.readlines()

# odstraní escape sekvence načtené na prvních pět řádků ze souboru .txt
# a vytvoří nový list seznam_batohu
seznam_batohu = []
posledni_batoh = seznam_batohu_s_escape.pop()
for batoh in seznam_batohu_s_escape:
    seznam_batohu.append(batoh[:-1])
seznam_batohu.append(posledni_batoh)

# rozdělí batohy na dvě přihrádky, vypíše je
# a vytvoří seznam všech předmětů vyskytujících se v obou přihrádkách
spolecne_predmety = []
spolecny_znak = None
for batoh in seznam_batohu:
    slice_point = int(len(batoh) / 2)
    prihradka_1 = batoh[:slice_point]
    prihradka_2 = batoh[slice_point:]
    print(f"{prihradka_1} {prihradka_2}\n")
    for char_1 in prihradka_1:
        for char_2 in prihradka_2:
            if char_1 == char_2:
                spolecny_znak = char_1
    for znak in batoh:
        if znak == spolecny_znak:
            spolecne_predmety.append(znak)

# vypíše třetí nadpis
nadpis_3 = "Zjištěné informace o batozích"
print(nadpis_3)
print(len(nadpis_3) * "*")

# vypíše seznam druhů společných předmětů (položek) v každém batohu
spolecne_druhy = []
for item in spolecne_predmety:
    if item not in spolecne_druhy:
        spolecne_druhy.append(item)
print(f"Seznam společných položek v každém batohu: {spolecne_druhy}\n")
print(f"Celkový součet priorit u všech batohů: {secti_priority(spolecne_predmety)}")
