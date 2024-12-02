
# definuje rekurzivní funkci - odpocet
def odpocet(a):
    """
    Funkce oodpocet() vypisuje rekurzivně čísla od 'a' po 1 \n
    :param a: počáteční číslo pro odpočítávání (musí být kladné)
    """
    # ukončující podmínka
    if a < 1:      #  a <= 0:
        return      # pouze ukončí funkci, nic nevrací
    
    # vypíše číslo
    print(a)
    odpocet(a - 1)      # rekurzivní funkce volá samu sebe

# zavolá funkci
odpocet(3)


