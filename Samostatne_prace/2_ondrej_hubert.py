
"""
Program vypočítá počet tvárnic na stavbu
Identifikační údaje o autorovi projektu:
Jméno a Příjmení: Ondřej Hubert
tel.: 773 500 373
e-mail: ondrej.hubert@gmail.com
Uživatelské jméno: stavebnik
Heslo: stavba
"""

# vypíše hlavičku programu
print("")
print("Konfigurátor zdícího systému")
print("****************************")
print("")

# nastaví uživatelské jméno a heslo
uzivatel = "stavebnik"
heslo = "stavba"

# přijme od uživatele přihlašovací údaje
zadany_uzivatel = input("Zadejte uživatelské jméno: ")
zadane_heslo = input("Zadejte heslo: ")
print("")

# zkontroluje správnost zadaných přihlašovacích údajů
if zadany_uzivatel == uzivatel and zadane_heslo == heslo:
    pass
else:
    print("Zadali jste chybné jméno nebo heslo. Program bude ukončen.")
    exit()

# načte od uživatele rozměry stěny a okna a plochu tvárnice
delka_steny = float(input("Zadejte délku stěny (metry): "))
vyska_steny = float(input("Zadejte výšku stěny (metry): "))
vyska_okna = float(input("Zadejte výšku okna (metry): "))
sirka_okna = float(input("Zadejte šířku okna (metry): "))
plocha_tvarnice = 0.1 # m2      # nebo: plocha_tvarnice = input("Zadejte plochu tvárnice v metrech čtverečních: ")   - nejasné zadání
print("")

# definuje funkci pro výpočty a výpis
def spocitej_tvarnice(stena_delka, stena_vyska, okno_vyska, okno_sirka):
    """
    Funkce spocitej_tvarnice() vypočítá plochu stěny včetně okna, plochu okna, plochu stěny bez okna a počet tvárnic a vypíše výsledky.
    Funkce vrátí počet tvárnic. \n
    :param stena_delka: délka stěny \n
    :param stena_vyska: výška stěny \n
    :param okno_vyska: výška okna \n
    :param okno_sirka: šířka okna
    
    """
    plocha_steny_vcetne_okna = stena_delka * stena_vyska
    plocha_okna = okno_vyska * okno_sirka
    plocha_steny_bez_okna = plocha_steny_vcetne_okna - plocha_okna
    pocet_tvarnic = int(plocha_steny_bez_okna / plocha_tvarnice)
    print(f"""Plocha stěny včetně okna: {plocha_steny_vcetne_okna} m^2
Plocha okna: {plocha_okna} m^2
Plocha stěny bez okna: {plocha_steny_bez_okna} m^2
Počet tvárnic potřebných k vyzdění plochy stěny: {pocet_tvarnic} ks""")
    return pocet_tvarnic


# zavolá funkci
pocet_tvarnic = spocitej_tvarnice(delka_steny,vyska_steny, vyska_okna, sirka_okna)

print("")

# vytvoří seznam poboček a kusů tvárnic na skladě
pobocky = [["Praha", "tvárnice", 500],
           ["Brno", "tvárnice", 300],
           ["Ostrava", "tvárnice", 700]]

# zobrazí v tabulce pobočky, které mají na skladě potřebné množství tvárnic
# vytvoří záhlaví tabulky
print("Dostupnost materiálu na pobočkách v ČR")
print("*" * 38)
zahlavi = "| {:8} | {:14} | {:22}|".format("Město", "Druh materiálu", "Počet kusů na pobočce")
print(zahlavi)

# vytvoří obsah tabulky
print(53 * "*")
for mesto, druh, pocet in pobocky:
    if pocet >= pocet_tvarnic:
        tabulka = "| {:8} | {:14} | {:<22}|".format(mesto, druh, pocet)
        print(tabulka)
