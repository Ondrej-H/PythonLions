
# vytvoří množinu největších měst ČR a vypíše ji
mesta = set(["Praha", "Brno", "Ostrava"])
print(f"Původní množina měst: {mesta}")

# načte od uživatele město, které chce odebrat
odstranovane_mesto = input("Napiš město, které chceš odstranit: ")

# zkontroluje zda je město v množině a případně jej odstraní a vypíše aktualizovaný seznam
if odstranovane_mesto in mesta:
    mesta.remove(odstranovane_mesto)
    print(f"Zadané město {odstranovane_mesto} bylo odstraněno z množiny měst.")
    print(f"V množině měst zůstala města: {mesta}")
else:
    print(f"Zadané město {odstranovane_mesto} se v množině měst nenachází a nelze odstranit.")



