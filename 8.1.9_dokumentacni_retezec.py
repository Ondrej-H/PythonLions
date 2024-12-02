
# definuje funkci na dělení a popíše ji dokumentačním řetězcem (docstringem)
def vydel(a, b):
    """
    Funkce vydel() provede dělení 2 čísel \n
    :param a: Dělenec (libovolné číslo) \n
    :param b: Dělitel (libovolné číslo kromě 0) \n
    :return: Výsledek po dělení
    """
    if b == 0:
        print("Dělení nulou není povoleno!")
        exit()          # ukončuje celý program
    return a / b


# načte od uživatele 2 čísla
cislo_1 = int(input("Zadejte číslo 1: "))
cislo_2 = int(input("Zadejte číslo 2: "))

# zavolá funkci a vypíše
vysledek = vydel(cislo_1, cislo_2)
print(f"Výsledek: {vysledek}")
