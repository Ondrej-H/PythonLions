
role = input("Jste učitel nebo žák?: ")
if role == "učitel":
    jmeno_zaka = input("Zadejte jméno žáka, kterého chcete hodnotit: ")
    znamka = input("Zadejte známku: ")
    print(f"Žák {jmeno_zaka} dostal známku {znamka}")
elif role == "žák":
    predmet = input("Zadej předmět u kterého se chceš podívat na známku: ")
    if predmet == "čeština":
        print("1,2,3")
    elif predmet == "matika":
        print("3, 4, 5")
    else:
        print("Tento předmět nemáš zapsaný.")
else:
    print("Neplatný uživatel!")
