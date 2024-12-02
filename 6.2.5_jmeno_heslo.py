
# vytvoří slovník s uživatelským jménem a heslem
heslovnik = {"uzivatel": "heslo123"}

# vytvoří while cyklus
while True:
    # získá vstup od uživatele - uživatelské jméno nebo konec
    uzivatelske_jmeno = input("Zadejte uživatelské jméno nebo 'konec' pro ukončení programu: ")

    # podmínka - kontrola zda se jedná o řetezec "konec"
    if uzivatelske_jmeno == "konec":
        print("Program byl ukončen.")
        # break
        exit()             # funkce exit() okamžitě ukončí celý program

    # získá vstup od uživatele - heslo
    heslo = input("Zadejte heslo: ")

    # vyhodnotí správnost kombinace uživatelského jména a hesla
    #if uzivatelske_jmeno in heslovnik and heslo == heslovnik["uzivatelske_jmeno"]:
    #if uzivatelske_jmeno in heslovnik and heslovnik.get(uzivatelske_jmeno) == heslo:
    if (uzivatelske_jmeno, heslo) in heslovnik.items():       # metoda .items() -> vrátí tupl
        print("Přihlášení proběhlo úspěšně. Vítejte uživateli!")
        break
    else:
        print("Nesprávná kombinace uživatelského jména a hesla! Zkuste znovu.")
