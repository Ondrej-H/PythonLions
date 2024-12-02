
# přednastaví heslo
heslo = "tajne"

# v cyklu načítá od uživatele heslo a vyhodnotí správnost hesla
while True:
    zadane_heslo = input("Zadejte heslo: ")
    if zadane_heslo == heslo:
        print("Vítejte!")
        break
    else:
        print(f"Nesprávné heslo - '{zadane_heslo}'")

