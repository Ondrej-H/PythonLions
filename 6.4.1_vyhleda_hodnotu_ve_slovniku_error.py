
# vytvoří slovník a vypíše jej
slovnik = {
    "příjmení": "Novák",
    "věk": 30,
    "povolání": "programátor"
}
print(f"Můj slovník: {slovnik}")

# načte od uživatele hledaný klíč
zadany_klic = input("Napište klíč, ke kterému chcete hledat hodnotu: ")

# vytvoří proměnnou a přiřadí do ní hodnotu od klíče a vypíše

hledana_hodnota = slovnik[zadany_klic]
print(f"Zadaný klíč '{zadany_klic}' má hodnotu '{hledana_hodnota}'")


