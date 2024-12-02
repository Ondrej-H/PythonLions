
print("-" * 50)

# Určí heslo a počet pokusů
spravne_heslo = "hes123"
pocet_pokusu = 3

# Načte heslo od uživatele (3 pokusy)
for i in range (pocet_pokusu, 0, -1):
    zadane_heslo = input(f"Zadej heslo pro pokračování: ")

# Zkontroluje správnost hesla a vypíše hlášku
    if zadane_heslo == spravne_heslo:
        print("Vítej, přihlášení proběhlo úspěšně.")
        break
    else:
        print("Zadali jste špatné heslo.")
        if i == 1:
            print("Program byl ukončený. ")
            exit()

print("-" * 50)

# vytvoří seznam jmen
seznam_jmen = ["Matouš", "Marek", "Lukáš", "Jan", "Pavel", "Marie", "Petra",
"Marek", "Jan", "Petra", "Monika", "David", "Lukáš", "Jan", "Marie", "Marie",
"Standa", "Marie", "Petra", "Marie", "Marie", "Jan", "Monika", "Marek", "Lukáš",
"Marek", "Jan", "Jan"]

# vypíše seznam jmen
print(f"Vstupní seznam: {seznam_jmen}")

print("-" * 50)

# převede seznam na množinu a vypíše jí 
mnozina_jmen = set(seznam_jmen)

# vypíše seznam bez duplicit (převede množinu na seznam)
unikatni_seznam = list(mnozina_jmen)
print(f"Unikátní seznam: {unikatni_seznam}")

# Spočítá a vypíše počet prvků seznamu 
pocet_prvku = len(unikatni_seznam)
print(f"Počet jmen v unikátním seznamu je: {pocet_prvku}")

print("-" * 50)

# Najde počet výskytu hledaného jména a vypíše výsledek + vypíše počet výskytu pomocí *
znak = "*"
for jmeno in unikatni_seznam:
    pocet_jmen = seznam_jmen.count(jmeno)
    vypsani_znaku = znak * pocet_jmen
    print(f"Jméno {jmeno} se vyskytuje {pocet_jmen} x")
    print(vypsani_znaku)

