
# načte od uživatele text a znak, který chce nalézt
text = input("Zadejte text, ve kterém chcete hledat: ")
znak = input("Zadejte znak, který chcete nalézt: ")

# projde postupně větu a určí, jestli se hledaný znak nachází ve větě a zjistí a vypíše na jakém indexu
if znak not in text:
    print(f"Hledaný znak '{znak}' se daném textu nenachází.")
else:
    for index, aktualni_znak in enumerate(text):
        if aktualni_znak == znak:
            print(f"Hledaný znak se v textu nachází na indexu {index}")
