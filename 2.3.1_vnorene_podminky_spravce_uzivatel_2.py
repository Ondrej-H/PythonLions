
# vytvoření přístupových hesel
heslo_admin = "admin"
heslo_user = "user"

# načtení hesla od uživatele
zadane_heslo = input("Zadejte heslo: ")

# nejlepší varianta:
# kontrola hesla pomocí vnořených podmínek
if zadane_heslo != heslo_admin and zadane_heslo != heslo_user:
    print("Neplatné heslo! Přístup odepřen.")
else:
    if zadane_heslo == heslo_admin:
        print("Vítejte, správce!")
    else:
        print("Vítejte, uživateli!")

# první varianta
# kontrola hesla pomocí vnořených podmínek
if zadane_heslo == heslo_admin or zadane_heslo == heslo_user:       #zadane heslo je admin nebo user
    if zadane_heslo == heslo_admin:
        print("Vítejte správce!")
    else:
        print("Vítejte uživateli!")
else:
    print("Zadali jste špatné heslo!")




# druhá varianta (moje):
# vytvoření přístupových hesel
heslo_admin = "admin"
heslo_user = "user"

# načtení hesla od uživatele
zadane_heslo = input("Zadejte heslo: ")

# kontrola hesla pomocí vnořených podmínek
if zadane_heslo == heslo_admin:
    print("Vítejte správce!")
else:
    if zadane_heslo == heslo_user:
        print("Vítejte uživateli!")
    else:
        print("Zadali jste špatné heslo!")