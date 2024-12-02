
# vytvoří seznam a vypíše jej
seznam = [5, 1, 2, 3, 5, 5, 3, 3, 3]
print(f"Můj seznam je: {seznam}")

# načte od uživatele hledané číslo
hledane_cislo = int(input("Zadejte číslo, pro které chcete hledat počet výskytů v daném seznamu: "))

# najde počet výskytů čísla a vypíše výsledek
pocet_vyskytu = seznam.count(hledane_cislo)
print(f"Hledané číslo {hledane_cislo} se v seznamu nachází {pocet_vyskytu}x")

