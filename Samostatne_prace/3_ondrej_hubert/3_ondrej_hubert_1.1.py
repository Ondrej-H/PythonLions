
"""
Identifikační údaje o autorovi projektu:
Jméno a Příjmení: Ondřej Hubert
tel.: 773 500 373
e-mail: ondrej.hubert@gmail.com
"""

print(40 * "-" + "\n")
# importuje modul os
import os
import math

# získá cestu k adresáři s tímto programem
cesta_k_adresari = os.path.dirname(os.path.abspath(__file__))
batohy_nazev_souboru = "batohy_test_2.txt"
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




#for i in range (ord("a"), (ord("z") + 1)):
#    print(chr(i), end="")



with open(cesta_k_batohum, "r") as batohy:
    seznam_batohu_bez_mezer = batohy.readlines()


#for item in seznam_batohu_bez_mezer:
#    print(f"{len(item)} {item}")

# tento blok se nejspíše nevyužije
seznam_batohu = []
for item in seznam_batohu_bez_mezer:
    slice_point = math.ceil(len(item) / 2)
    batoh = item.center(slice_point)   #item[0:slice_point]
    seznam_batohu.append(batoh)
print("*", seznam_batohu)

# 
posledni_batoh = seznam_batohu.pop()
print(f"Poslední batoh: {posledni_batoh}")
print(f"Seznam batohů bez posledního: {seznam_batohu}")
for batoh in seznam_batohu:
    batoh = item[0:(len(item)-1)]

print(f"Seznam batohů bez escape sekvencí: {seznam_batohu}")



