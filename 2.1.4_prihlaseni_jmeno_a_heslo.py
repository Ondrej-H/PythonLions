
# Stanoví uživatelské jméno a heslo
uzivatel = "Matouš"
heslo = "Mat123"


# Přijme od uživatele uživatelské jméno a heslo
zadane_jmeno = input("Zadejte uživatelské jméno: ")
zadane_heslo = input("Zadejte heslo: ")

# Porovná zadané údaje s přednastavenýma a vypíše hlášku
if zadane_jmeno == uzivatel and zadane_heslo == heslo:
    print("Zadané jméno a heslo je správné. Vítejte.")
else:
    print("Zadané jméno nebo heslo je chybné. Přístup odepřen.")

