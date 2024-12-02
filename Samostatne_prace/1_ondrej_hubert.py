
"""
Identifikační údaje o autorovi projektu:
Jméno a Příjmení: Ondřej Hubert
tel.: 773 500 373
e-mail: ondrej.hubert@gmail.com
"""

# vypíše hlavičku programu
print("----------------------------------")
print("ZJISTÍ NEJČASTĚJŠÍ JMÉNA V SEZNAMU")
print("----------------------------------\n")
# 1. zkontroluje vložené heslo
# nastaví heslo pro přístup do programu
heslo = "hes123"

# vyzve uživatele k zadání hesla v maximálně třech pokusech - přijme vstup od uživatele (zadane_heslo):
# vytvoří proměnnou zadane_heslo a poprvé vyzve uživatele k zadání hesla
zadane_heslo = input("Zadejte heslo pro pokračování: ")     # první pokus

# nastaví zbývající počet pokusů
pocet_pokusu = 2                                            # zbylé dva pokusy
# pomocí while cyklu provede požadovanou akci dle vstupu uživatele
while True:
    # pokud uživatel namísto hesla napíše "konec", s hláškou o zkončení ukončí program
    if zadane_heslo == "konec":
        print("Program byl ukončený.")
        exit()
    # pokud je zadané heslo správné (odpovídá heslu), přivítá uživatele a ukončí while cyklus
    elif zadane_heslo == heslo:
        print("Vítejte, přihlášení proběhlo úspěšně!\n")
        break
    # provede případné další dva pokusy o zadání hesla, v případě vyčerpání pokusů s hláškou ukončí program
    else:
        pocet_pokusu -= 1
        zadane_heslo = input("Zadejte heslo pro pokračování: ")
        if pocet_pokusu == 0 and zadane_heslo != heslo:
            print("Program byl ukončený.")
            exit()


# 2. vytvoří vstupní seznam a vypíše jej
vstupni_seznam = ["Matouš", "Marek", "Lukáš", "Jan", "Pavel", "Marie", "Petra",
"Marek", "Jan", "Petra", "Monika", "David", "Lukáš", "Jan", "Marie", "Marie",
"Standa", "Marie", "Petra", "Marie", "Marie", "Jan", "Monika", "Marek", "Lukáš",
"Marek", "Jan", "Jan"]
print(f"Vstupní seznam: {vstupni_seznam}")


# 3. ze vstupního seznamu vytvoří seznam unikátních jmen, zjistí jejich počet a nový seznam i počet jmen vypíše
# pomocí převedení seznamu na množinu se zbaví duplikátů
seznam_unikatnich_jmen = set(vstupni_seznam)

# převede množinu zpět na seznam unikátních jmen
seznam_unikatnich_jmen = list(seznam_unikatnich_jmen)

# zjistí počet jmen v seznamu unikátních jmen
pocet_unikatnich_jmen = len(seznam_unikatnich_jmen)

# vypíše seznam unikátních jmen
print(f"Seznam unikátních jmen: {seznam_unikatnich_jmen}")

# vypíše počet jmen v seznamu unikátních jmen
print(f"Počet jmen v seznamu unikátních jmen: {pocet_unikatnich_jmen}\n")


# 4. zjistí počet výskytů pro každé unikátní jméno ve vstupním seznamu
# vypíše hlavičku (nadpis)
print("Kolikrát se vyskytuje každé jméno")
print("----------------------------------")
# zjistí počet výskytů a vypíše
for jmeno in seznam_unikatnich_jmen:
    pocet_vyskytu = vstupni_seznam.count(jmeno)
    print(f"Jméno {jmeno} se vyskytuje {pocet_vyskytu} x")
    print(pocet_vyskytu * '*')
print("\n")


# 5. zjistí, která jména se vyskytují nejčastěji ve vstupním seznamu
# vypíše hlavičku (nadpis)
print("Nejčastěji se vyskytují následující jména:")
print("------------------------------------------")

# vytvoří slovník, kde klíč bude jméno a hodnota bude počet výskytů - pomocí for cyklu
slovnik = dict()
for jmeno in seznam_unikatnich_jmen:
    pocet_vyskytu = vstupni_seznam.count(jmeno)
    slovnik[jmeno] = pocet_vyskytu
#print(slovnik)

# nastaví požadavek na tři nejčastější výskyty
i = 3
while i != 0:
    # přednastaví proměnnou nejvyssi_pocet(výskytů) a prázdný seznam jmen (s nejvyšším výskytem)
    nejvyssi_pocet = 0
    jmena_nejvyssi_vyskyt = []
    
    # projde hodnoty ve slovníku a proměnnou nejvyssi_pocet nastaví na nejvyšší z nich
    for value in slovnik.values():
        if value > nejvyssi_pocet:
            nejvyssi_pocet = value
    
    # do prázdného seznamu jmen s nejvyšším výskytem přidá jména s nejvyšším výskytem
    for key in slovnik.keys():
        if slovnik.get(key) == nejvyssi_pocet:
            jmena_nejvyssi_vyskyt.append(key)

    # vypíše kolikrát se které jméno vyskytuje
    print(f"{nejvyssi_pocet} x se vyskytuje:")
    for jmeno in jmena_nejvyssi_vyskyt:
        print(jmeno)

    # smaže ze slovníku klíče s nejvyšším výskytem,
    # aby bylo možno v dalších iteracích while cyklu nalézt druhý a třetí nejvyšší počet výskytu
    for jmeno in jmena_nejvyssi_vyskyt:
        del slovnik[jmeno]

    # sníží počet následujících iterací while cyklu
    i -= 1



print("")
print("")
print("KONEC PROGRAMU")
print("")
print("--------------------------------------------------------------------------------")
print("--------------------------------------------------------------------------------")
