
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
    společné_položky = []

    for znak in první_prihradka:
        if znak in druha_prihradka and znak not in společné_položky:
            priorita = vypocti_prioritu(znak)
            pocet_vyskytu = radek.count(znak)
            soucet_priorit += priorita * pocet_vyskytu
            společné_položky.append(znak)

    return soucet_priorit, společné_položky

# Získání cesty k programu
cesta_k_programu = os.path.abspath(__file__)

# Získání cesty ke vstupnímu souboru
cesta_k_souboru = os.path.join(os.path.dirname(cesta_k_programu), "batohy_test_2.txt")

# Načtení vstupního souboru
with open(cesta_k_souboru, "r") as soubor:
    batohy = soubor.readlines()

# Zpracování batohů a výpočet součtu priorit
soucet_vsech_priorit = 0
seznam_společných_položek = []
print("Vyhledání společných věcí v každém batohu")
print("*" * 30)
print("\nCesta k aktuálně spuštěnému programu:")
print(cesta_k_programu)
print("\nCesta ke vstupnímu souboru s popisem batohů:")
print(cesta_k_souboru)
print("\nObsah batohů v první a ve druhé polovině (odděleno mezerou)")
print("*" * 40)
for radek in batohy:
    soucet_priorit, společné_položky = zpracuj_batoh(radek.strip())
    seznam_společných_položek.extend(společné_položky)
    print(f"{radek.strip()}")
    soucet_vsech_priorit += soucet_priorit

print("\nZjištěné informace o batozích")
print("*" * 25)
print(f"Seznam společných položek v každém batohu: {seznam_společných_položek}")
print(f"\nCelkový součet priorit u všech batohů: {soucet_vsech_priorit}")