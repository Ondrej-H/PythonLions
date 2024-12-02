
# načte od uživatele aktuální čas jako číslo
cas = float(input("Zadejte aktuální čas jako číslo (0 - 24): "))


# vyhodnotí jaký je čas a napíše příslušný pozdrav
if cas < 10:
    print("Dobré ráno!")
elif cas < 12:
    print("Dobré dopoledne!")
elif cas < 18:
    print("Dobré odpoledne!")
else:
    print("Dobrý večer!")