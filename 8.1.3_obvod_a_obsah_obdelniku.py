
# definuje funkci pro výpočet obvodu obdélníku
def vypocitej_obvod(a, b):
    vysledek = 2 * (a + b)
    return vysledek


# definuje funkci pro výpočet obsahu obdélníku
def vypocitej_obsah(a, b):
    vysledek = a * b
    return vysledek


# získá data od uživatele (rozměry obdélníku)
strana_a = float(input("Zadejte délku strany a: "))     # namísto 'strana_a' lze sice použít jen 'a',
strana_b = float(input("Zadejte délku strany b: "))     # ale dle pylintu je špatně používání stejného názvu jako v definici funkce (zřejmě kvůli čitelnosti...?)

# zavolá funkci pro výpočet obvodu a vypíše výsledky
obvod = vypocitej_obvod(strana_a, strana_b)
print(f"Obvod obdélníku je: {obvod}")

# zavolá funkci pro výpočet obsahu a vypíše výsledky
obsah = vypocitej_obsah(strana_a, strana_b)
print(f"Obsah obdélníku je: {obsah}")
