
# načte od uživatele první a druhé slovo
prvni_slovo = input("Zadejte první slovo: ")
druhe_slovo = input("Zadejte druhé slovo: ")

# nastavení flagu (příznaku) na počáteční hodnotu False
nalezeno = False

# postupně projde obě slova a zjistí zda mají společné písmeno
for znak_1 in prvni_slovo:
    for znak_2 in druhe_slovo:
        if znak_1 == znak_2:
            nalezeno = True
            break
    if nalezeno:
        break

# vypíše výsledek uživateli - zda nalezl shodné písmeno a jaké
if nalezeno:
    print(f"Společné písmeno je: {znak_1}")
else:
    print(f"Zadaná slova nemají společné písmeno.")