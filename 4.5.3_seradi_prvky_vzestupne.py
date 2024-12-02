
# vytvoří seznam a vypíše jej
seznam_ovoce = ["jablko", "hruška", "banán"]
print(f"Původní seznam ovoce: {seznam_ovoce}")

# seřadí seznam vzestupně dle abecedy (pomocí funkce sorted()) a vypíše jej
serazeny_seznam = sorted(seznam_ovoce)      # sorted(seznam_ovoce, reverse=True) - vypíše pozpátku (sestupně)
print(f"Seřazený seznam s ovocem dle abecedy: {serazeny_seznam}")
print(f"Původní seznam ovoce: {seznam_ovoce}")

# seřadí seznam vzestupně dle abecedy a vypíše jej
seznam_ovoce.sort()
print(f"Seřazený seznam s ovocem dle abecedy: {seznam_ovoce}")