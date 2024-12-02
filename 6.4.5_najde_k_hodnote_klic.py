
# vytvoří slovník a vypíše jej
slovnik = {
    "příjmení": "Novák",
    "věk": "30",
    "povolání": "programátor"
}
print(f"Můj slovník: {slovnik}")

# načte od uživatele hodnotu, aby mohl nalézt její klíč
zadana_hodnota = input("Napište hodnotu, u které chcete vyhledat její klíč: ")

# získá klíč pro danou hodnotu
# využije cyklus for - iteruje přes klíče
hledany_klic = None    # předefinuje proměnou pro daný klíč a potom využije ve čtvrtém bloku  # zjišťuji, že to funguje i bez předdefinování # ale nefunguje to při zadání hodnoty, která není ve slovníku
for key in slovnik.keys():
    # pro každý klíč zjistí jeho hodnotu a zkontroluje ji se zadanou hodnotou od uživatele
    if slovnik.get(key) == zadana_hodnota:
        hledany_klic = key
        break           # přeruší cyklus v případě nalezení

# vypíše výsledek jestli nalezl nebo nenalezl
if hledany_klic:    # None je vyhodnoceno vždy jako False,
                    # pokud má proměnná nějakou hodnotu (kromě False) je vyhodnoceno jako True     
                    # is not None:                # is -> kontroluje na celý jeden konkrétní objekt
                    # == kontroluje na stejnou hodnotu
    print(f"Hodnota {zadana_hodnota} je přiřazena ke klíči {hledany_klic}.")
else:
    print(f"Hodnota {zadana_hodnota} nebyla ve slovniku nalezena.")