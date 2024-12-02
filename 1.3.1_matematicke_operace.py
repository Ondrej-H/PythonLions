
# načte čísla
cislo_1 = input('Vaše první číslo: ')
cislo_2 = input('Vaše druhé číslo: ')

# převede vstup na celá čísla (integer)
cislo_1 = int(cislo_1)
cislo_2 = int(cislo_2)

# vypočte součet, rozdíl, součin a podíl
soucet = cislo_1 + cislo_2
rozdil = cislo_1 - cislo_2
soucin = cislo_1 * cislo_2
podil = cislo_1 / cislo_2

# vypíše všechny výsledky
print('Součet prvního a druhého čísla je: ', soucet)
print('Rozdíl prvního a druhého čísla je: ', rozdil)
print('Součin prvního a druhého čísla je: ', soucin)
print('Podíl prvního a druhého čísla je: ', podil)