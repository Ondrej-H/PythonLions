 
# importuje modul os
import os

# navolí cestu ke složce s fotkami
cesta_k_fotkam = r"C:\Programming\PythonLions\9.1.4_fotky"

#vytvoří seznam původních názvů fotek
seznam_nazvu_fotek = os.listdir(cesta_k_fotkam)

cislovani_fotek = 1
pripona = ".jpg"

# přejmenuje fotky
for fotka in seznam_nazvu_fotek:
    if fotka.lower().endswith(".jpg"):
        novy_nazev = f"{cislovani_fotek}_obrázek" + pripona
        nova_cesta = os.path.join(cesta_k_fotkam, novy_nazev)
        stara_cesta = os.path.join(cesta_k_fotkam, fotka)
        os.rename(stara_cesta, nova_cesta)
        print(f"Starý název fotky {fotka} byl změněn na nový název {novy_nazev}.")
        cislovani_fotek += 1