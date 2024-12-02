
# získá data od uživatele(text ve kterém chce hledat a znak, který chce hledat) a uloží je do proměnných
text = input("Zadejte text, který chcete prohledat: ")
znak = input("Zadejte znak, který chcete vyhledat: ")

# vyhodnotí zda se znak v textu nachází, pokud ne vypíše znak nenalezen
if znak not in text:
    print(f"Hledaný znak {znak} se v textu nenachází")
# pokud se znak v textu nachází zjistí jeho index a vypíše
else:
    pozice = text.find(znak)        # metoda .find() při nenalezení vrací -1 (False)
#    pozice = text.index(znak)      # metoda .index() při nenalezení hodí ValueError
    print(pozice)








