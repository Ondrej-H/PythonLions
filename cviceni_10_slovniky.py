
# vytvoří seznam jmen
jmena = {"Jakub", "Petr", "Tomáš", "Marek", "Jan", "Michal"}
print(f"Toto je množina jmen: {jmena}")

# načte od uživatele hledané jméno
hledane_jmeno = input("Zadejte hledané jméno: ")

# prohledá množinu jmen, každé prohledávané jméno vypíše a pokud nalezene hledané jméno, oznámí to
for jmeno in jmena:
    print(f"Procházené jméno: {jmeno}")
    if jmeno == hledane_jmeno:
        print("Jméno nalezeno! Cyklus přerušen.")
        break

# pokud hledané jméno není v seznamu, oznámí to
if hledane_jmeno not in jmena:
    print(f"Jméno {hledane_jmeno} nenalezeno!")




