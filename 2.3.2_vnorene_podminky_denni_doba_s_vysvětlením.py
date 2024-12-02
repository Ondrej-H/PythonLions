
# vypíše časové mezníky použité v programu (pro kontrolu při spuštění)
# print(0,6,10,12,18,22,24)

# načte od uživatele aktuální čas jako číslo
cas = int(input("Zadejte kolik je hodin (jako celé číslo): "))

# vyhodnotí denní dobu a vypíše hlášku je ta a ta denní doba (s použitím vnořené podmínky + elif)

# varianta lektora
if cas < 0 or cas > 24:
    print("Neplatná hodina!")
#else:
#    if cas ...:
#        print ...:
#    elif cas ...
#        print ...
#    else:
#        print ...

# varianta 1
if cas >= 0 and cas <= 24:
    if cas == 0:
        print("Je půlnoc.")
    elif cas < 6:
        print("Je noc.")
    elif cas < 10:
        print("Je ráno.")
    elif cas < 12:
        print("Je dopoledne.")
    elif cas == 12:
        print("Je pravé poledne.")
    elif cas < 18:
        print("Je odpoledne.")
    elif cas <= 22:
        print("Je večer.")
    elif cas < 24:
        print("Je pozdě večer.")
    elif cas == 24:
        print("Je půlnoc.")
else:
    print("Neplatný čas!")


# varianta 2
if not (cas >= 0 and cas <= 24):
    print("Neplatný čas! Neplatný čas! Neplatný čas!")
else:
    if cas == 0:
        print("Je půlnoc.")
    elif cas < 6:
        print("Je noc.")
    elif cas < 10:
        print("Je ráno.")
    elif cas < 12:
        print("Je dopoledne.")
    elif cas == 12:
        print("Je pravé poledne.")
    elif cas < 18:
        print("Je odpoledne.")
    elif cas <= 22:
        print("Je večer.")
    elif cas < 24:
        print("Je pozdě večer.")
    elif cas == 24:
        print("Je půlnoc.")