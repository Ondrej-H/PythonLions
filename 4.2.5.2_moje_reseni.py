
# vytvoří seznam zaměstnanců a vypíše jej
seznam_zamestnancu = ["Karel", "David", "Petr", "Standa"]
print(f"Seznam zaměstnanců: {seznam_zamestnancu}")

# vyhledá zda je zaměstnanec v seznamu a na jakém indexu je umístěn
ukonceni_programu = ""
while ukonceni_programu != "k":
    hledany_zamestnanec = input("Napište jméno hledaného zaměstnance: ")
    if hledany_zamestnanec in seznam_zamestnancu:
        index = seznam_zamestnancu.index(hledany_zamestnanec)
        print(f"Hledaný zaměstnanec {hledany_zamestnanec} je v seznamu zaměstnanců na indexu číslo {index}")
        ukonceni_programu = input("Pro pokračování stiskněte enter, pro ukončení programu napište k a potvrďte enterem. >")
    else:
        print(f"Hledaný zaměstnanec {hledany_zamestnanec} se v seznamu zaměstnanců nenachází.")
        ukonceni_programu = input("Pro pokračování stiskněte enter, pro ukončení programu napište k a potvrďte enterem. >")




