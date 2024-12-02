
# importuje modul os
import os

# najde cestu k aktuálně otevřenému souboru, omezí ji na cestu ke složce a vypíše ji
oddelovac = 40 * "-"
print(oddelovac)
cesta_ke_slozce = os.path.dirname(os.path.abspath(__file__))
print(f"Toto je cesta ke složce s tímto programem:\n{cesta_ke_slozce}")
print(oddelovac)

# vytvoří seznam souborů ve složce, postupně jej projde a každý vypíše na vlastní řádek
seznam_souboru_ve_slozce = os.listdir(cesta_ke_slozce)
for item in seznam_souboru_ve_slozce:
    print(item)

print(oddelovac)
