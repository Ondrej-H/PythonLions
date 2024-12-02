
# vytvoří seznam jmen a vypíše jej
seznam = ["Petr", "Karel", "Jan", "Lukáš", "Matouš"]
print(f"Původní seznam: {seznam}")

# odstraní ze seznamu jméno Petr a vypíše upravený seznam
seznam.remove("Petr")
print(f"Odstraněné jméno Petr - zbylý seznam: {seznam}")

# odstraní ze seznamu jméno na prvním indexu a vypíše upravený seznam
del seznam[0]
print(f"Odstraněné jméno Karel - zbylý seznam: {seznam}")

# odstraní ze seznamu jméno na prvním indexu a uloží jej do proměné jan a vypíše upravený seznam
jan = seznam.pop(0)
print(f"Odstraněné jméno Jan - zbylý seznam: {seznam}")
print(f"Odstraněný prvek ze seznamu: {jan}")

# odstraní vše ze seznamu
seznam.clear()
print(f"Odstraněný celý seznam: {seznam}")

