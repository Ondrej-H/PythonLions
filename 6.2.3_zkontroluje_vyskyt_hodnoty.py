
# vytvoří slovník a vypíše jej
slovnik = {
    "příjmení": "Novák",
    "věk": "30",
    "povolání": "programátor"
}

print(f"Můj slovník: {slovnik}")

# načte od uživatele hledanou hodnotu
hledana_hodnota = input("Hodnota ke zkontrolování: ")

# rozhodne zda se hodnota nachází ve slovníku
if hledana_hodnota in slovnik.values():
    print(f"Hledaná hodnota {hledana_hodnota} ve slovníku nalezena!")
else:
    print(f"Hledaná hodnota {hledana_hodnota} není ve slovníku.")

