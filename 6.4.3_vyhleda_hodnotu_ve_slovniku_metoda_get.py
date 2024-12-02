
# vytvoří slovník a vypíše jej
slovnik = {
    "příjmení": "Novák",
    "věk": 30,
    "povolání": "programátor"
}
print(f"Můj slovník: {slovnik}")

# načte od uživatele klíč, který chce zkontrolovat
zadany_klic = input("Napište klíč, ke kterému chcete hledat hodnotu: ")

# získá hodnotu pro zadaný klíč pomocí metody .get()
hledana_hodnota = slovnik.get(zadany_klic, "žádná")  # přidáním druhého argumentu "žádná" se v případě že hodnota je None vypíše namísto None "žádná"
print(f"Zadaný klíč '{zadany_klic}' má hodnotu '{hledana_hodnota}'")




