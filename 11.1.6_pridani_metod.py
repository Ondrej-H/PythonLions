
# definuje třídu "BankovniUcet" a vytvoří jeho konstruktor
class BankovniUcet():
    # společný atribut
    banka = "ČSOB"  # toto je atribut (společný atribut)

    def __init__(self, nazev="běžný", majitel=None, zustatek=0):     # do kulatých závorek píšeme vstupní atributy
        self.nazev = nazev
        self.majitel = majitel
        self.zustatek = zustatek

    # definuje metodu pro vklad peněz
    def vklad(self, castka):
        self.zustatek += castka
        print(f"Vloženo: {castka} Kč, nový zůstatek: {self.zustatek} Kč")

    # definuje metodu pro výběr peněz
    def vyber(self, castka):
        if castka > self.zustatek:      # jestli uživatel nevybírá více peněz než může
            print(f"Nedostatečná výše zůstatku, zůstatek: {self.zustatek} Kč")
        else:
            self.zustatek -= castka
            print(f"Vybráno: {castka} Kč, nový zůstatek: {self.zustatek} Kč")


# vytvoří instanci - přidá atributy název, majitel, zůstatek
ucet_1 = BankovniUcet("běžný", "Jan Novák", 5000)
#goguv_ucet = BankovniUcet("spořící", "Gogo", 8000)

# vypíše zůstatek, majitele a typ účtu
print("Vytvořili jsme bankovní účet.")
print(f"Zůstatek:   {ucet_1.zustatek}")
print(f"Majitel:    {ucet_1.majitel}")
print(f"Typ účtu:   {ucet_1.nazev}")
print(f"Banka:      {ucet_1.banka}")
#print(f"Gogův zůstatek: {goguv_ucet.zustatek}")

print()

# zavolá metodu pro vklad peněz na účet
ucet_1.vklad(5000)

# zavolá metodu pro výběr v případě dostatečného zůstatku
ucet_1.vyber(9000)

# zavolá metodu pro výběr v případě NEdostatečného zůstatku
ucet_1.vyber(9000)

#ucet_2 = BankovniUcet()
"""
print("Vytvořili jsme druhý bankovní účet.")
print(f"Zůstatek:   {ucet_2.zustatek}")
print(f"Majitel:    {ucet_2.majitel}")
print(f"Typ účtu:   {ucet_2.nazev}")
print(f"Banka:      {ucet_2.banka}")
"""

#ucet_1.vklad()
#castka = int(input("Kolik chcete vložit? "))

