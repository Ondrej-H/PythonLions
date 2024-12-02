
# vytvoří seznam a vypíše jej
seznam_ovoce = ["jablko", "hruška", "banán"]
print(f"Původní seznam ovoce: {seznam_ovoce}")

puvodni_seznam_ovoce = list(seznam_ovoce)

# přidá prvek do seznamu na konkrétní pozici
seznam_ovoce.insert(2, "kiwi")      # vloží na index 2 string "kiwi"
print(f"Aktualizovaný seznam ovoce: {seznam_ovoce}")

print(f"Původní seznam ovoce: {puvodni_seznam_ovoce}")
