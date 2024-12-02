
# nastaví heslo a počet pokusů
spravne_heslo = "heslo"
pocet_pokusu = 3


# načte heslo od uživatele (max 3x)
for i in range(pocet_pokusu, 0, -1):
    zadane_heslo = input(f"Zadejte heslo, máte {i} pokusů: ")
    if zadane_heslo == spravne_heslo:
        print("Vítejte!")
        break
    print(f"Nesprávné heslo!")
    if i == 1:
        print("Pokusy vyčerpány. Zablokováno.")



    # zkontroluje správnost hesla ve třech pokusech
