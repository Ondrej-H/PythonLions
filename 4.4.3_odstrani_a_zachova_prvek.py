
# vytvoří seznam a vypíše jej
seznam_ovoce = ["jablko", "hruška", "banán", "jahoda"]
print(f"Původní seznam ovoce: {seznam_ovoce}")


# načte od uživatele jaký prvek chce odstranit a vypsat
index = int(input("Zadejte index prvku, který chcete odebrat: "))


# odstraní prvek z indexu, vypíše jej a vypíše aktualizovaný seznam
odstraneny_prvek = seznam_ovoce.pop(index)              # odstraní ze seznamu prvek daného indexu a zároveň jej uloží do proměnné odtraneny_prvek
print(f"Aktualizovaný seznam ovoce: {seznam_ovoce}")
print(f"Odstraněný prvek je: {odstraneny_prvek}")
