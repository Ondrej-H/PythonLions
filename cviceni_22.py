
# importuje modul os
import os

# přijme data od uživatele a sestaví cestu k souboru
retezec = input("Zadejte řetězec, který chcete zapsat do souboru: ")
nazev_souboru = input("Zadejte název souboru, do kterého chcete zapsat (včetně přípony .txt): ")
cesta_k_adresáři = os.path.dirname(os.path.abspath(__file__))
cesta_k_souboru = os.path.join(cesta_k_adresáři, nazev_souboru)

# zapíše do souboru požadovaný řetězec
with open(cesta_k_souboru, "w", encoding="UTF-8") as f:
    f.write(retezec)
