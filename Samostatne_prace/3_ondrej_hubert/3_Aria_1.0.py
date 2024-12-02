
# importuje modul os
import os

def vypocti_prioritu(znak):
    """
    Funkce pro výpočet priority znaku.
    """
    if znak.islower():
        return ord(znak) - ord('a') + 1
    elif znak.isupper():
        return ord(znak) - ord('A') + 27
    else:
        return 0

def zpracuj_batoh(radek):
    """
    Funkce pro zpracování jednoho řádku (batohu) ze vstupního souboru.
    """
    polovina = len(radek) // 2
    první_prihradka = radek[:polovina]
    druha_prihradka = radek[polovina:]
    soucet_priorit = 0

    for znak in první_prihradka:
        if znak in druha_prihradka:
            priorita = vypocti_prioritu(znak)
            pocet_vyskytu = radek.count(znak)
            soucet_priorit += priorita * pocet_vyskytu

    return soucet_priorit


# získá cestu k adresáři s tímto programem
cesta_k_adresari = os.path.dirname(os.path.abspath(__file__))
batohy_nazev_souboru = "batohy_test.txt"
cesta_k_batohum = os.path.join(cesta_k_adresari, batohy_nazev_souboru)

# Načtení vstupního souboru
with open(cesta_k_batohum, "r") as soubor:
    batohy = soubor.readlines()

# Zpracování batohů a výpočet součtu priorit
soucet_vsech_priorit = 0
for radek in batohy:
    soucet_vsech_priorit += zpracuj_batoh(radek.strip())

# Výpis výsledku
print(f"Součet všech priorit: {soucet_vsech_priorit}")