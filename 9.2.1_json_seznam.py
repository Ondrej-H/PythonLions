
# importuje json, os
import json
import os

# vytvoří seznam v Pythonu a vypíše jej
seznam_cisel_python = [1, 2, 3]
print(f"Počáteční seznam v Pythonu: {seznam_cisel_python}")

# získá cestu k aktuálnímu spuštěnému programu
cesta_slozky_s_aktualnim_spustenym_programem = os.path.dirname(os.path.abspath(__file__))           # v tomto případě se jedná o speciální proměnou, jiné "__název__" jsou zase dunder methods = double undescored methods
#                                                                              __file__ je speciální proměnná, která obsahuje cestu k aktuálnímu skriptu nebo modulu
#                                                              os.path.abspath() převede tuto cestu na absolutní cestu, která je nezávislá na pracovním adresáři
#                                              os.path.dirname() vrátí pouze adresářovou část cesty a odstraní název souboru nebo poslední část cesty

# vytvoří novou cestu k vytvářenému souboru
nova_cesta = os.path.join(cesta_slozky_s_aktualnim_spustenym_programem, "seznam_cisel.json")    # toto je pouze řetězec (string) - návod, kde má počítač hledat
#            os.path.join() spojí dvě nebo více částí cesty do jednoho řetězce; přijímá libovolný počet argumentů (které spojí správným zápisem pro daný operační systém)

# zakóduje seznam z Pythonu do json formátu a vytvoří soubor
# a vrátí zpětnou vazbu
# with je správce kontextu
# "w" je zkrácenina pro write (zápis), "r" - read, "a" - přidat(append?)
with open(nova_cesta, "w") as json_file:            # with open() as f:
# with - po ukončení bloku with se soubor zavře (což uvolní paměť)
#    open(nova_cesta, "w") otevře soubor pro zápis; pokud soubor takového názvu neexistuje, vytvoří jej; jinak jej přepíše
    json.dump(seznam_cisel_python, json_file)   # dump = vysypat/nasypat
print(f"Vytvořený soubor 'seznam_cisel.json' byl uložený do {nova_cesta}")
