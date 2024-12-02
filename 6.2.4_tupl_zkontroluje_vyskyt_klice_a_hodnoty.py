
# vytvoří slovník a vypíše jej
slovnik = {
    "příjmení": "Novák",
    "věk": "30",
    "povolání": "programátor"
}

print(f"Můj slovník: {slovnik}")

# načte od uživatele hledaný klíč a zároveň hledanou hodnotu
hledany_klic = input("Napište klíč, který chcete zkontrolovat: ")
hledana_hodnota = input("Napište hodnotu, kterou chcete zkontrolovat: ")

# rozhodne zda se hodnota s klíčem nachází ve slovníku
if (hledany_klic, hledana_hodnota) in slovnik.items():      # v kulatých závorkách jsme vytvořili objekt tupl
    print(f"Hledaný klíč {hledany_klic} a hodnota {hledana_hodnota} jsou ve slovníku.")      # metoda .items() vrací také tupl
else:
    print(f"Hledaný tupl {hledany_klic, hledana_hodnota} se ve slovníku nenachází.")


print(slovnik.items())