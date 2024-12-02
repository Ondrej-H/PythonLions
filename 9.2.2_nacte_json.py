
# importuje moduly json a os
import json
import os

# najde cestu k seznamu
cesta_k_seznamu = os.path.dirname(os.path.abspath(__file__))
nazev_json_seznamu = "9.2.1_seznam_cisel.json"
cesta_k_json_souboru = os.path.join(cesta_k_seznamu, nazev_json_seznamu)

# načte data ze souboru seznam_cisel
with open(cesta_k_json_souboru, "r") as json_soubor:
    seznam_cisel = json.load(json_soubor)
print(f"Načtená data: {seznam_cisel}")

for item in seznam_cisel:
    print(item)
