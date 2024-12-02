
# vytvoří prázdný slovník a vypíše jej
slovnik = dict(povolání="programátor", jmeno="Petr")
print(f"Počáteční prázdný slovník: {slovnik}")

# přidá prvky do slovníku pomocí metody update
slovnik.update({        # přepisuje hodnoty se stejným klíčem, přidává items() které ve slovníku ještě nejsou
    "jmeno": "Jan",
    "prijmeni": "Novák",
    "vek": 30
})
print(f"Updatovaný slovník: {slovnik}")