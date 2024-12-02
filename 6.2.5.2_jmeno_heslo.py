
# vytvoří slovník 
slovnik = {"uzivatel123": "heslo123"}

while True:
    jmeno = input("Zadejte uživatelské jméno: ")
    if jmeno == "konec":
        print("Program byl ukončen.")
        exit()
    elif jmeno in slovnik:
        heslo = input("Uživatelské jméno přijato. Zadejte heslo: ")
        if heslo == slovnik[jmeno]:
            print("Heslo je správné. Vítejte!")
            break
        else:
            print("Nesprávné heslo! Zkuste znovu.")
    else:
        print("Neplatné uživatelské jméno! Zkuste znovu.")
