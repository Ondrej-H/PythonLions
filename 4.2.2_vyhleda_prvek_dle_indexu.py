
# vytvoří seznam jmen a vytiskne původní seznam
seznam = list(["Matouš", "Marek", "Lukáš", "Jan"])
# -index         -4        -3       -2       -1
print(f"Původní seznam: {seznam}")

# získá index od uživatele
index = int(input("Napište index, který chcete vyhledat: "))

# vyhledá prvek dle zadaného indexu
hledany_prvek = seznam[index]

# vypíše prvek na hledaném indexu a index samotný
print(f"Prvek ze seznamu se zadaným indexem {index} je {hledany_prvek}.")
