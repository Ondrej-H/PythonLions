
# načtení věku uživatele
rok_narozeni = int(input("Zadejte rok narození: "))


# vypočítá věk uživatele a vypíše věk
vek = 2024 - rok_narozeni
print(f"Věk uživatele je: {vek}.")

# kontrola věku uživatele
if vek > 18 or vek == 18:                    # pravdivé když uživateli je 18 nebo více let
    print("Uživateli je 18 a více let.")
else:                                        # vykoná se pokud je mu méně let
    print("Uživateli je méně než 18 let.")