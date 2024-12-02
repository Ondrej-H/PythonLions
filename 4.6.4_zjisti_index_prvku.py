
# vytvoří seznam ovoce a vypíše jej
seznam_ovoce = ["jablko", "hruška", "banán", "pomeranč", "kiwi"]
print(f"Seznam ovoce je: {seznam_ovoce}")

# načte od uživatele název ovoce, které chce vyhledat
hledane_ovoce = input("Napište název ovoce, u kterého chcete vědět index: ")

# vyhledá na jakém se ovoce nachází indexu a vypíše
if hledane_ovoce in seznam_ovoce:
    index = seznam_ovoce.index(hledane_ovoce)
    print(f"Ovoce {hledane_ovoce} se nachází na indexu {index}.")
else:
    print(f"Hledané ovoce {hledane_ovoce} se v seznamu nenachází.")



