
# vytvoří seznam zaměstnanců (vstupní data do tabulky)
seznam_zamestnancu = list([["Jan Novák", "17.7.1977", "designer"],
                           ["Marie Šťastná", "3.3.2000", "inženýr"],
                           ["Petr Výborný", "25.12.1995", "programátor"]])

# vytvoří cyklus a bude procházet data
for jmeno, rok, pozice in seznam_zamestnancu:
    # vypíše do tabulky naformátovaně
    veta = "|{:<14}|{:^11}|{:>12}|".format(jmeno, rok, pozice)  # nalevo od dvojtečky je proměnná - zde posiční argument jmeno
    # ^ je altgr 33
    print(veta)