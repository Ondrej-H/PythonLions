
# načte od uživatele dosažený počet bodů jako číslo
pocet_bodu = int(input("Zadejte dosažený počet bodů (0 - 100): "))

# vyhodnotí počet bodů a známky a vypíše počet bodů a příslušnou známku
if pocet_bodu >= 90:             # if pocet_bodu > 90 or pocet_bodu == 90   # pocet bodu 90 - 100
    print(f"Dosáhl jste {pocet_bodu} bodů, Vaše známka je 1!")
elif pocet_bodu >= 80:                                                      # pocet bodu 80 - 89
    print(f"Dosáhl jste {pocet_bodu} bodů, Vaše známka je 2!")
elif pocet_bodu >= 70:                                                      # pocet bodu 70 - 79
    print(f"Dosáhl jste {pocet_bodu} bodů, Vaše známka je 3!")
elif pocet_bodu >= 60:                                                      # pocet bodu 60 - 69
    print(f"Dosáhl jste {pocet_bodu} bodů, Vaše známka je 4!")
else:                                                                       # pocet bodu 0 - 59
    print(f"Dosáhl jste {pocet_bodu} bodů, Vaše známka je 5!")