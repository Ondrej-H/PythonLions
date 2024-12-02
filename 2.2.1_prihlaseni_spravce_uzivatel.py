# vytvoření hesla pro role
admin_heslo = "admin"
user_heslo = "user"

# přijme heslo od uživatele
zadane_heslo = input("Zadejte heslo: ")


# kontrola hesla a udělení rolí
if zadane_heslo == admin_heslo:         # varianta přihlášený jako správce
    print("Vítejte, správce!")
elif zadane_heslo == user_heslo:        # varianta přihlášený jako uživatel
    print("Vítejte, uživateli!")
else:                                   # varianta zadání špatného hesla
    print("Přihlášení neproběhlo úspěšně. Neplatné heslo.")