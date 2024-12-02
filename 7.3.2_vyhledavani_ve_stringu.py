
# vytvoří řetězec ahoj světe a vypíše jej
muj_string = "Ahoj, světe!"
print(f"Prohledávaná věta: {muj_string}")

# získá hodnotu (hledaný podřetězec) od uživatele
hledany_text = input("Zadejte hledaný text: ")

# pomocí podmínky if rozhodne zda se hledaný podřetězec nachází ve větě
if hledany_text in muj_string:
    print(f"Hledaný text '{hledany_text}' byl nalezen v prohledávané větě.")
else:
    print(f"Hledaný text '{hledany_text}' NEBYL nalezen v prohledávané větě.")
