
# načte od uživatele počáteční a koncové číslo řady
pocatecni_cislo = int(input("Zadejte počáteční číslo řady: "))
koncove_cislo = int(input("Zadejte koncové číslo řady: "))

# vytvoří dočasnou proměnnou "cislo"
cislo = pocatecni_cislo

# pomocí while cyklu vypíše číselnou řadu
while cislo <= koncove_cislo:
    print(cislo)
    cislo += 1

# to samé pomocí cyklu for
print("_____________________________")
for znak in range(pocatecni_cislo, koncove_cislo + 1):
    print(znak)