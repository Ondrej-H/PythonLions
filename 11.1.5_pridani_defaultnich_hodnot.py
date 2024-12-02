

# definuje třídu "BankovniUcet" a vytvoří jeho konstruktor
class BankovniUcet():
    # společný atribut
    banka = "ČSOB"  # toto je atribut (společný atribut)

    def __init__(self, nazev="běžný", majitel=None, zustatek=0):     # do kulatých závorek píšeme vstupní atributy
        self.nazev = nazev
        self.majitel = majitel
        self.zustatek = zustatek

# vytvoří instanci - přidá atributy název, majitel, zůstatek
ucet_1 = BankovniUcet("běžný", "Jan Novák", 5000)
#goguv_ucet = BankovniUcet("spořící", "Gogo", 8000)

# vypíše zůstatek, majitele a typ účtu
print("Vytvořili jsme bankovní účet.")
print(f"Zůstatek:   {ucet_1.zustatek}")
print(f"Majitel:    {ucet_1.majitel}")
print(f"Typ účtu:   {ucet_1.nazev}")
print(f"Banka:      {ucet_1.banka}")
#print(f"Gogův zůstatek: {cizi_ucet.zustatek}")

print()

ucet_2 = BankovniUcet()
print("Vytvořili jsme druhý bankovní účet.")
print(f"Zůstatek:   {ucet_2.zustatek}")
print(f"Majitel:    {ucet_2.majitel}")
print(f"Typ účtu:   {ucet_2.nazev}")
print(f"Banka:      {ucet_2.banka}")
