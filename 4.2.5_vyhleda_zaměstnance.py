
# vytvoří seznam zaměstnanců a vypíše jej
seznam_zamestnancu = list(["Karel", "David", "Petr", "Standa"])
print(f"Můj seznam zaměstnanců: {seznam_zamestnancu}")

# získá vstup od uživatele, o kterého zaměstnance má zájem
ukonceni_programu = ""
while ukonceni_programu != "k":
    hledany_zamestnanec = input("Napište jméno zaměstnance, kterého hledáte: ")

    # rozhodne (porovná) zda se hledané jméno nachází v seznamu
    if hledany_zamestnanec in seznam_zamestnancu:
        # vypíše hlášku o nalezení
        index = seznam_zamestnancu.index(hledany_zamestnanec)       # 
        print(f"Zaměstnanec {hledany_zamestnanec} je v seznamu zaměstnanců na indexu {index}.")
        break
    # vypíše hlášku o nenalezení
    else:
        print(f"Zaměstnanec {hledany_zamestnanec} se v seznamu nenachází.")

    # získá vstup od uživatele, zda chce pokračovat a podle toho se zachová
    ukonceni_programu = input("Pro pokračování napište 'p', pro ukončení programu napište 'k': ")       # pro pokračování stiskněte enter, pro ukončení 'k'
#    if ukonceni_programu == "p":
#        continue

print("""
Program byl ukončen!""")