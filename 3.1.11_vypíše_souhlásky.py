
# načte od uživatele libovolné slovo
zadane_slovo = input("Zadejte libovolné slovo: ")

# zkontroluje a vypíše souhlásky obsažené v textu pomocí cyklu
for znak in zadane_slovo:
    if znak == "a" or znak == "e" or znak == "i" or \
    znak == "o" or znak == "u" or znak == "y":
        continue        # přeskočí daný znak a iteruje od začátku
    print(znak, end=" ")