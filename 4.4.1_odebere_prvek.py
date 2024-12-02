
# vytvoří seznam a vypíše jej
seznam_ovoce = ["jablko", "hruška", "banán"]
print(f"Původní seznam ovoce: {seznam_ovoce}")

# odstraní konkrétní prvek ze seznamu
seznam_ovoce.remove("banán")            # odstraní konkrétní prvek "banán"
seznam_ovoce.remove(seznam_ovoce[0])    # odstraní prvek na indexu 0

print(f"Aktualizovaný seznam ovoce: {seznam_ovoce}")
