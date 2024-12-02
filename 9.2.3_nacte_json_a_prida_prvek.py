
# importuje moduly json a os
import json
import os

# získá cesty - cestu k aktuálnímu adresáři(spuštěnému programu),
# cestu k počátečnímu seznamu a cestu k doplněnému seznamu
cesta_k_aktualnimu_adresari = os.path.dirname(os.path.abspath(__file__))
cesta_k_pocatecnimu_seznamu = os.path.join(cesta_k_aktualnimu_adresari, "9.2.1_seznam_cisel.json")
cesta_k_doplnovanemu_seznamu = os.path.join(cesta_k_aktualnimu_adresari, "9.2.3_seznam_cisel_2.json")

# otevře JSON soubor, načte počáteční seznam a vypíše jej
with open(cesta_k_pocatecnimu_seznamu, "r") as json_puvodni:    # zde se pouze přistupuje k souboru
    seznam_cisel = json.load(json_puvodni)      # zde probíhá deserializace z JSON formátu a uložení do Pythonovské proměné seznam_cisel
print(f"Počáteční seznam: {seznam_cisel}")

# doplní seznam a vypíše
seznam_cisel.append(4)
print(f"Doplněný seznam: {seznam_cisel}")

# převede seznam z Pythonu na JSON formát, zapíše do nového JSON souboru a vypíše hlášku
with open(cesta_k_doplnovanemu_seznamu, "w") as json_novy:
    json_novy.write(json.dumps(seznam_cisel) + "\n")     # metoda .write zapíše to co dostane jako argument do souboru nad kterým je volána # dumps == dump string

print("Doplněný seznam byl uložen!")
