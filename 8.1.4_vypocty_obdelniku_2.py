
# definuje funkci pro výpočet obvodu a obsahu obdélníku
def vypocti_obdelnik(a, b):
    obvod_vypocet = 2* (a + b)
    obsah_vypocet = a * b
    return obvod_vypocet, obsah_vypocet


# načte data od uživatele (strany a, b)
#try:
strana_a = int(input("Zadejte stranu a: ")) # muselo by být odsazeno
strana_b = int(input("Zadejte stranu b: "))
#except ValueError:
#    print("Zadejte pouze číslice!")
#    strana_a = int(input("Zadejte stranu a: "))
#    strana_b = int(input("Zadejte stranu b: "))

# zavolá funkci pro výpočet obvodu a obsahu obdélníku a vypíše výsledky
obvod, obsah = vypocti_obdelnik(strana_a, strana_b)
print(f"Obvod obdélníku je: {obvod} \nObsah obdélníku je: {obsah}")
