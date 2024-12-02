
slovnik_povolani = {
    "příjmení": "Novák",
    "věk": 30,
    "povolání": "programátor"
}
print(f"Můj slovník povolání: {slovnik_povolani}")

hledany_klic = input("Klíč ke zkontrolování: ")

if hledany_klic in slovnik_povolani.keys():
    print(f"Klíč {hledany_klic} je ve slovníku.")
else:
    print(f"Klíč {hledany_klic} není ve slovniku")