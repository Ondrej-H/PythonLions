
# přejmenuje "seznam_cisel.json" na "9.2.1_seznam_cisel.json"
import os

cesta_ke_slozce = os.path.dirname(os.path.abspath(__file__))
stary_nazev_souboru = "seznam_cisel.json"
stara_cesta = os.path.join(cesta_ke_slozce, stary_nazev_souboru)

novy_nazev_souboru = "9.2.1_seznam_cisel.json"
nova_cesta = os.path.join(cesta_ke_slozce, novy_nazev_souboru)

try:
    os.rename(stara_cesta, nova_cesta)
    print(f"Soubor {stary_nazev_souboru} byl přejmenován na:\n{nova_cesta}")
except FileNotFoundError:
    print(f"File {stary_nazev_souboru} was not found at {cesta_ke_slozce}")