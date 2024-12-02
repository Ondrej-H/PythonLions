
# definuje "hlavní" funkci, kde zavolá funkce pro sčítání a násobení
def hlavni_funkce(a, b):
    soucet = secti(a, b)
    soucin = vynasob(a, b)
    return soucet, soucin


# definuje vnořenou funkci pro součet a druhou pro násobení
def secti(a, b):
    return a + b


def vynasob(a, b):
    return a * b


# získá vstup od uživatele
cislo_1 = int(input("Zadejte číslo 1: "))
cislo_2 = int(input("Zadejte číslo 2: "))

# zavolá hlavní funkci a vypíše výsledek
soucet_vysledek, soucin_vysledek = hlavni_funkce(cislo_1, cislo_2)
print(f"Součet čísel {cislo_1} + {cislo_2} = {soucet_vysledek}")
print(f"Součin čísel {cislo_1} * {cislo_2} = {soucin_vysledek}")
