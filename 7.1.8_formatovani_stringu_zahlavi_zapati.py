
# vytvoří seznam zaměstnanců (vstupní data do tabulky)
seznam_zamestnancu = list([["Jan Novák", "17.7.1977", "designer"],
                           ["Marie Šťastná", "3.3.2000", "inženýr"],
                           ["Petr Výborný", "25.12.1995", "programátor"]])

# vypíše záhlaví tabulky
print("-" * 49)
zahlavi = "| {:14} | {:14} | {:12}|".format("Jméno", "Datum narození", "Povolání")
print(zahlavi)
print("-" * 49)

# přistoupí k datům z tabulky a vypíše formátovaně
for jmeno, rok, pozice in seznam_zamestnancu:
    tabulka = "| {:-<14} | {:14} | {:12}|".format(jmeno, rok, pozice)
    print(tabulka)

# vypíše zápatí
print("-" * 49)
