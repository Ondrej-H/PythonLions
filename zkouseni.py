
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
hledane_povolani = input("Zadejte povolání, ke kterému chcete najít zaměstnance: ")

jmena_k_hledanemu_povolani = []
for key in zamestnanci:
    if zamestnanci[key]["povolání"] == hledane_povolani:
        jmena_k_hledanemu_povolani.append(zamestnanci[key]["povolání"])
        

