
# definuje funkci s libovolným počtem argumenentů
def secti(*args):
    """
    Funkce secti() sečte všechny zadané argumety \n
    :param args: libovolný počet čísel
    """
    vysledek = sum(args)        #vysledek = 0
                                #for cislo in args:
                                #    vysledek += cislo
    return vysledek


# zavolá funkci a vypíše výsledek
soucet = secti(1,2,3,4,5)
print(soucet)
