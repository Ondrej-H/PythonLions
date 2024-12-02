
# definuje funkci 'vynasob'
def vynasob(a, b):
    vysledek = a * b
    return vysledek


# načte od uživatele dvě čísla k násobení
cislo_1 = int(input("Zadejte první číslo k vynásobení: "))
cislo_2 = int(input("Zadejte druhéčíslo k vynásobení: "))

# zavolá funkci 'vynasob' a jako poziční argumenty jí dá data od uživatele (cislo_1 a cislo_2)
# a vypíše výsledek
nasobeni = vynasob(cislo_1, cislo_2)
print(f"Násobení: {cislo_1} * {cislo_2} = {nasobeni}")
