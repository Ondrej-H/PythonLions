
print("Přejmenuje fotky - modul os + os.listdir() + os.rename() + .endswith()")
print(40 * "-")
# ctrl ; --> pustí terminál (konzoli)
# importuje modul 'os' (operational system) - veškeré importy patří hned na začátek kódu
import os

# navolí cestu ke složce s fotkami a vytvoří seznam názvů fotek
cesta = "C:\\Programming\\PythonLions\\9.1.4_fotky"       # nebo r"..." - 'raw' řetězec
seznam_fotek = os.listdir(cesta)

# přejmenuje fotky
# vytvoří pomocnou proměnou pro číslování fotky
cislovani_fotek = 1
pripona = ".jpg"
    # postupně projde seznam fotek pomocí for cyklu
for stary_nazev in seznam_fotek:
    # zkontroluje, zda se jedná o soubor s příponou .jpg
    if stary_nazev.lower().endswith(".jpg"):
    # vytvoří nový název pro fotku a vytvoří novou cestu (s novým názvem pro fotku)
        novy_nazev = f"{cislovani_fotek} - Programování" + pripona
        nova_cesta = os.path.join(cesta, novy_nazev)
        stara_cesta = os.path.join(cesta, stary_nazev)
        # provede přejmenování fotky
        os.rename(stara_cesta, nova_cesta)
        print(f"Přejmenováno {stary_nazev} -> {novy_nazev}")

        cislovani_fotek += 1
