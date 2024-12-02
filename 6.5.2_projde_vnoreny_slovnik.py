
# vytvoří vnořený slovník a vypíše jej
zamestnanci = {
    "zamestnanec_1": {
        "jméno": "Novák",
        "povolání": "programátor",
    },
    "zamestnanec_2": {
        "jméno": "Eva Svobodová",
        "povolání": "designer"
    },
    "zamestnanec_3": {
        "jméno": "Petr Dvořák",
        "povolání": "programátor"
    }
}
print(f"Slovník se zaměstnanci: {zamestnanci}")

# získá vstup od uživatele pro kterou hodnotu hledá zaměstnance
hledana_hodnota = input("Zadejte povolání, ke kterému chcete najít zaměstnance: ")

# program projde ve slovníku klíče spárované s danou hodnotou a vypíše informace
nalezeno = False            # příznak (flag)
for klic, hodnota in zamestnanci.items():
    if hodnota.get("povolání") == hledana_hodnota:
        print(f"{klic} Jméno: {hodnota.get('jméno')}, Povolání: {hodnota.get('povolání')}")
        nalezeno = True

# 
if nalezeno == False:
    print(f"Ve slovníku se nenachází žádný zaměstnanec s povoláním {hledana_hodnota}")








