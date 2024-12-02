
import json
import os

slovnik = {
    "Pandan": {
        "inventory": ["sword", "armor"],
        "stats": {
            "Dex": "20",
            "Str": "18"
        }
    },
    "Siram": {
        "inventory": ["book", "staff"],
        "stats": {
            "Int": "19",
            "Wis": "17"
            }
    }
}
print(slovnik)

json_soubor_nazev = "9.2.1.1_slovnik.json"
cesta_ke_slozce = os.path.dirname(os.path.abspath(__file__))
cesta_k_json = os.path.join(cesta_ke_slozce, json_soubor_nazev)

with open(cesta_k_json, "w") as json_file:
    json.dump(slovnik, json_file)

print(f"Vytvořený soubor '{json_soubor_nazev}' byl uložený do složky:\n{cesta_k_json}")
