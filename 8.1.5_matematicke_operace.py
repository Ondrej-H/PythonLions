
# definuje funkci pro násobení, sčítání a odečítání
def vypocet(a, b):
    soucet_vypocet = a + b
    rozdil_vypocet = a - b
    soucin_vypocet = a * b
    return soucet_vypocet, rozdil_vypocet, soucin_vypocet


# získá vstup od uživatele
cislo_1 = int(input("Zadejte číslo 1: "))
cislo_2 = int(input("Zadejte číslo 2: "))

# zavolá funkci a vypíše výsledky (součin, rozdíl a součet)
soucet, rozdil, soucin = vypocet(cislo_1, cislo_2)
print(f"Součet čísel je: {soucet}")
print(f"Rozdíl čísel je: {rozdil}")
print(f"Součin čísel je: {soucin}")
