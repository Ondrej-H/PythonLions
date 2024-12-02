
# nastaví heslo
heslo = "tajne"

# přijme heslo od uživatele
zadane_heslo = input("Zadejte heslo: ")

# porovná hesla a vypíše příslušnou hlášku pomocí logického operátoru not
if not zadane_heslo == heslo:                   # != je nerovná se
    print("Neplatné heslo. Přístup zamítnut!")
else:
    print("Přístup povolen, heslo je správné. Vítejte!")