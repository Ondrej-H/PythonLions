
# definuje funkci pro zjištění zda je číslo kladné, záporné nebo nula
def rozhodni_zda_kladne(cislo):
    if cislo > 0:
        return "Číslo je kladné"
    elif cislo == 0:
        return "Číslo je nula"
    else:
        return "Číslo je záporné"


# získá vstup od uživatele - číslo
zadane_cislo = int(input("Zadejte číslo: "))

# zavolá funkci a vypíše výsledek
vysledek = rozhodni_zda_kladne(zadane_cislo)
print(vysledek)
