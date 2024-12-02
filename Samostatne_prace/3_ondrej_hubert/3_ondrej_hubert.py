
"""
Identifikační údaje o autorovi projektu:
Jméno a Příjmení: Ondřej Hubert
tel.: 773 500 373
e-mail: ondrej.hubert@gmail.com
"""

print(40 * "-" + "\n")
# importuje modul os
import os

# vytvoří funkci pro sečtení priorit
def vypocitej_prioritu(znak):
    """
    Vrátí prioritu znaku
    :param znak: jedno písmeno abecedy
    """
    if znak.islower():
        return ord(znak) - ord("a") + 1
    elif znak.isupper():
        return ord(znak) - ord("A") + 27
    else:
        return 0


# vytvoří funkci 
def projdi_radek(radek):
    """
    Vrací součet priorit v řádku (batohu) a společnou položku obou jeho polovin.\n
    Funkce rozdělí řádek (batoh) na dvě přihrádky,\n
    zjistí jakou položku(znak) mají obě přihrádky společnou a uloží ji,\n
    vypočte prioritu společné položky(znaku),\n
    zjistí počet výskytů společné položky v celém řádku(batohu)\n
    a sečte priority celého řádku(batohu).\n
    :param radek: string
    """
    soucet_priorit_radku = 0
    spolecna_polozka_radku = []
    polovina = len(radek.strip()) // 2
    prihradka_1 = radek.strip()[:polovina]
    prihradka_2 = radek.strip()[polovina:]

    for znak in prihradka_1:
        if znak in prihradka_2 and znak not in spolecna_polozka_radku:
            spolecna_polozka_radku.append(znak)
            priorita = vypocitej_prioritu(znak)
            pocet_vyskytu = radek.count(znak)
            soucet_priorit_radku += pocet_vyskytu * priorita
    return soucet_priorit_radku, spolecna_polozka_radku


# získá cestu k adresáři s tímto programem
cesta_k_adresari = os.path.dirname(os.path.abspath(__file__))

# získá cestu k souru se vstupnimi daty
cesta_ke_vstupnimu_souboru = os.path.join(cesta_k_adresari, "batohy_vstup.txt")

# 
with open(cesta_ke_vstupnimu_souboru, "r") as f:
    batohy = f.readlines()

# vypíše úvod programu (nadpisy + cesty)
nadpis_1 = "Vyhledání společných věcí v každém batohu"
print(nadpis_1)
print(len(nadpis_1) * "*")
print("\nCesta k aktuálně spuštěnému programu (ke složce, ve které se nachází):")
print(cesta_k_adresari)
print("\nCesta ke vstupnímu souboru s popisem batohů:")
print(cesta_ke_vstupnimu_souboru)

nadpis_2 = "\nObsah batohů v první a ve druhé polovině (odděleno mezerou)"
print(nadpis_2)
print(len(nadpis_2) * "*")

# sečte všechny priority, vytvoří seznam společných položek
# a vypíše obsah batohů v první a ve druhé polovině (odděleno mezerou)
soucet_vsech_priorit = 0
seznam_spolecnych_polozek = []
for radek in batohy:
    soucet_priorit_radku, spolecna_polozka_radku = projdi_radek(radek)
    soucet_vsech_priorit += soucet_priorit_radku
    seznam_spolecnych_polozek.extend(spolecna_polozka_radku)
    polovina = len(radek.strip()) // 2
    print(f"\n{radek.strip()[:polovina]} {radek.strip()[polovina:]}")

# vypíše třetí nadpis
nadpis_3 = "\nZjištěné informace o batozích"
print(nadpis_3)
print(len(nadpis_3) * "*")
print(f"\nSeznam společných položek v každém batohu: {seznam_spolecnych_polozek}")
print(f"\nCelkový součet priorit u všech batohů: {soucet_vsech_priorit}")
