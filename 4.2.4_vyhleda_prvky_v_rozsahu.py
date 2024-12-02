
# vytvoří seznam jmen a vytiskne původní seznam
seznam = list(["Matouš", "Marek", "Lukáš", "Pavel", "Jan"])
print(f"Původní seznam: {seznam}")

# vyhledá prvky dle rozsahu
nalezene_prvky = seznam[1:4]    # konec intervalu není zahrnut podobně jako u funkce range(1,4)
                                # slicing
# vypíše nalezené prvky
print(f"Prvky dle zadaného rozsahu indexů [1:4] jsou: {nalezene_prvky}")