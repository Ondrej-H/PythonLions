
# Uloží celkovou cenu za nákup a počet kusů v nákupu
cena_nakupu = float(input("Zadejte celkovou cenu za nákup: "))
kusu = int(input("Zadejte počet kusů v nákupu: "))


# Spočítá a vypíše cenu za jeden kus
cena_kus = cena_nakupu / kusu
print("Cena za jeden kus je: ", cena_kus)


# Pokud je cena pod 100 korun napíše nakupuj, jinak napíše nic nekupovat
if cena_kus < 100:
    print("Cena za jeden kus je pod sto korun! Nakupuj!")
else:
    print("Cena za kus je dražší než sto korun. Nic nekupovat.")