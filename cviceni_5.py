
# načte od uživatele vrchní a spodní hranici intervalu
vrchni_hranice = int(input("Zadejte vrchní hranici intervalu: "))
spodni_hranice = int(input("Zadejte spodni hranici intervalu: "))

# nastaví dočasnou proměnnou cislo
cislo = vrchni_hranice

# vypíše sestupný interval pomocí while cyklu
print("Výpis sestupného intervalu: ")
while spodni_hranice <= cislo:
    print(cislo, end=";")
    cislo -= 1