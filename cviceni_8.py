
# vytvoří seznam a vypíše jej
puvodni_seznam = [1, 2, 3, 4, 5, 6, 7]
print(f"Původní seznam je: {puvodni_seznam}")

# načte od uživatele číslo
pokracovat = ""
while pokracovat != "q":
    cislo = int(input("Zadejte číslo, které chcete zkontrolovat: "))

    # rozhodne zda se číslo nachází či nenachází v seznamu a zda se jedná o nejvyšší nebo nejnižší

    if cislo in puvodni_seznam:
        if cislo == max(puvodni_seznam):
            print(f"Číslo {cislo} je největší v seznamu.")
        elif cislo == min(puvodni_seznam):
            print(f"Číslo {cislo} je nejmenší v seznamu.")
        else:
            print(f"Číslo {cislo} se nachází v seznamu.")
    else:
        print(f"Číslo {cislo} se nenachází v seznamu.")
    
    pokracovat = input("""Pro ukončení programu napište q a potvďte entrem.
Pro pokračování stiskněte enter. > """)
