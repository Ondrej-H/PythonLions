
# načte od uživatele text a znak, který chce nalézt
text = input("Zadejte text, ve kterém chcete hledat: ")
znak = input("Zadejte znak, který chcete nalézt: ")

# vytvoří pomocnou proměnnou (flag - příznak) pro určení, zda byl znak nalezen
nalezeno = False     # v angličtině bycho pojmenovali takto - isFound = False

# projde postupně větu a určí, jestli se hledaný znak nachází ve větě
for index, aktualni_znak in enumerate(text):    # enumarate("python") -> (0, p), (1, y), (2, t), (3, h), (4, o), (5, n)
    if aktualni_znak == znak:                   #            012345
        print(f"Hledaný znak se v textu nachází na indexu {index}")
        nalezeno = True

# zkontroluje jestli byl znak nalezen (původní hodnota příznaku - nenalezeno, změněná hodnota - nalezeno)
if not nalezeno:
    print(f"Hledaný znak '{znak}' se daném textu nenachází.")
