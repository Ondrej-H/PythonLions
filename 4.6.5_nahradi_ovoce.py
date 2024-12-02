
# vytvoří seznam ovoce a vypíše jej
seznam_ovoce = ["jablko", "hruška", "banán", "pomeranč", "kiwi"]
print(f"Seznam ovoce je: {seznam_ovoce}")

# načte od uživatele název ovoce, které che ze seznamu odstranit
odstranovane_ovoce = input("Napište název ovoce, které chcete odstranit: ")

# načte od uživatele ovoce, které chce v seznamu nahradit
vkladane_ovoce = input("Napište název ovoce, které chcete odstranit: ")

# nahradí ovoce jiným ovocem a vypíše aktualizovaný seznam
index = seznam_ovoce.index(odstranovane_ovoce)  # zjistí index nahrazovaného ovoce
seznam_ovoce[index] = vkladane_ovoce
# ŘEŠIT TO POMOCÍ NASLEDUJÍCÍCH DVOU ŘÁDKŮ BY BYLO ZBYTEČNÉ A ZPOMALOVALO BY TO PROGRAM
# seznam_ovoce.remove(odstranovane_ovoce)
# seznam_ovoce.insert(index, vkladane_ovoce)
print(f"Nový seznam ovoce je: {seznam_ovoce}")

