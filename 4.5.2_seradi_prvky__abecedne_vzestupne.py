
# vytvoří seznam a vypíše jej
seznam_ovoce = ["jablko", "hruška", "banán"]
seznam_cisel = [10, 88, 50, 80]
print(f"Původní seznam ovoce: {seznam_ovoce}")

# seřadí seznam vzestupně dle abecedy a vypíše jej
seznam_ovoce.sort()
seznam_cisel.sort()
print(f"Seřazený seznam s ovocem dle abecedy: {seznam_ovoce}")
print(f"Vzestupně seřazený seznam čísel: {seznam_cisel}")

seznam_ovoce.sort(reverse=True)
seznam_cisel.sort(reverse=True)

print(f"Seřazený seznam s ovocem dle abecedy sestupně: {seznam_ovoce}")
print(f"Sestupně seřazený seznam čísel: {seznam_cisel}")

