
"""
Identifikační údaje o autorovi projektu:
Jméno a Příjmení: Ondřej Hubert
tel.: 773 500 373
e-mail: ondrej.hubert@gmail.com
"""

print(40 * "-" + "\n")
# importuje modul os
import os

# získá cestu k adresáři s tímto programem
cesta_k_adresari = os.path.dirname(os.path.abspath(__file__))
batohy_nazev_souboru = "batohy.txt"
cesta_k_batohum = os.path.join(cesta_k_adresari, batohy_nazev_souboru)

# vypíše úvod programu (nadpisy + cesty)
nadpis_1 = "Vyhledání společných věcí v každém batohu"
print(nadpis_1)
print(len(nadpis_1) * "*" + "\n")
print(f"Cesta k aktuálně spuštěnému programu:\n{cesta_k_adresari}\n")
print(f"Cesta ke vstupnímu souboru s popisem batohů:\n{cesta_k_batohum}\n")

nadpis_2 = "Obsah batohů v první a ve druhé polovině (odděleno mezerou)"
print(nadpis_2)
print(len(nadpis_2) * "*")

# 




with open(cesta_k_batohum, "r") as batohy:
    vstupni_data_string = batohy.read()
vstupni_data_radky = vstupni_data_string.replace(" ", "\n")

print(vstupni_data_radky)

with open(cesta_k_batohum, "w") as batohy:
    batohy.write(vstupni_data_radky)

print(batohy)



