
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
    Vrací součet priorit v řádku (batohu) a společnou položku obou jeho polovin.\n
    Funkce rozdělí řádek (batoh) na dvě přihrádky,\n
    zjistí jakou položku(znak) mají obě přihrádky společnou a uloží ji,\n
    vypočte prioritu společné položky(znaku),\n
    zjistí počet výskytů společné položky v celém řádku(batohu)\n
    a sečte priority celého řádku(batohu).\n
    :param radek: string
    """
    polovina = len(radek) // 2
    první_prihradka = radek[:polovina]
    druha_prihradka = radek[polovina:]
    soucet_priorit_radku = 0
    spolecna_polozka_radku = []

    for znak in první_prihradka:
        if znak in druha_prihradka and znak not in spolecna_polozka_radku:
            priorita = vypocti_prioritu(znak)
            pocet_vyskytu = radek.count(znak)
            soucet_priorit_radku += priorita * pocet_vyskytu
            spolecna_polozka_radku.append(znak)

    return soucet_priorit_radku, spolecna_polozka_radku

# Získání cesty k programu
cesta_k_programu = os.path.abspath(__file__)

# Získání cesty ke vstupnímu souboru
cesta_k_souboru = os.path.join(os.path.dirname(cesta_k_programu), "batohy_test_2.txt")

# Načtení vstupního souboru
with open(cesta_k_souboru, "r") as soubor:
    batohy = soubor.readlines()

# Zpracování batohů a výpočet součtu priorit
soucet_vsech_priorit = 0
seznam_vsech_spolecnych_polozek = []
print("Vyhledání společných věcí v každém batohu")
print("*" * 30)
print("\nCesta k aktuálně spuštěnému programu:")
print(cesta_k_programu)
print("\nCesta ke vstupnímu souboru s popisem batohů:")
print(cesta_k_souboru)
print("\nObsah batohů v první a ve druhé polovině (odděleno mezerou)")
print("*" * 40)
for radek in batohy:
    polovina = len(radek.strip()) // 2
    print(f"{radek.strip()[:polovina]} {radek.strip()[polovina:]}")
    soucet_priorit_radku, spolecna_polozka_radku = zpracuj_batoh(radek.strip())
    seznam_vsech_spolecnych_polozek.extend(spolecna_polozka_radku)
    soucet_vsech_priorit += soucet_priorit_radku
    print(f"Společné položky: {spolecna_polozka_radku}")
    print(f"Seznam společných položek: {seznam_vsech_spolecnych_polozek}")


print("\nZjištěné informace o batozích")
print("*" * 25)
print(f"Seznam společných položek v každém batohu: {seznam_vsech_spolecnych_polozek}")
print(f"\nCelkový součet priorit u všech batohů: {soucet_vsech_priorit}")