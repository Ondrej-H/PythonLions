
# načte od uživatele slovo a vypíše z něj souhlásky - s použitím in, or a continue
slovo = input("Napište libovolné slovo: ")
nalezene_souhlasky = []
for znak in slovo:
    if znak == "a" or znak == "e" or znak == "i" or\
        znak == "o" or znak == "u" or znak == "y":
        continue
    nalezene_souhlasky.append(znak)
    
if nalezene_souhlasky != []:
    print(f"Souhlásky v zadaném slově jsou: {nalezene_souhlasky}")
else:
    print("Zadané slovo neobsahuje žádné souhlásky.")
