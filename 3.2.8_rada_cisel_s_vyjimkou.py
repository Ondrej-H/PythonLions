
# načte od uživatele počáteční, koncové číslo řady a číslo, které vynechá
pocatecni_cislo = int(input("Zadejte počáteční číslo řady: "))
koncove_cislo = int(input("Zadejte koncové číslo řady: "))
vyjimka = int(input("Zadejte číslo, které chcete vynechat: "))

# vytvoří dočasnou proměnnou "cislo"
cislo = pocatecni_cislo

# pomocí while cyklu vypíše číselnou řadu
while cislo <= koncove_cislo:
    if cislo != vyjimka:        # if cislo == vyjimka:
        print(cislo)            #   cislo += 1
    cislo += 1                  #   continue
                                # print(cislo)
                                # cislo += 1