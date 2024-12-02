
# vytvoří seznam a vypíše jej
seznam = [4, 1, 5, 2, 3]
print(f"Můj seznam je: {seznam}")

# načte od uživatele číslo, které che vyhledat
hledane_cislo = int(input("Napište číslo, které chcete vyhledat: "))

# zjistí zda se číslo nachází nebo nenachází v seznamu a vypíše
if hledane_cislo in seznam:
    print("Hledané číslo se v seznamu nachází.")
elif hledane_cislo not in seznam:
    print("Hledané číslo se nenachází v daném seznamu.")

