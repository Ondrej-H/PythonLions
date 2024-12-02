
# vytvoří vnořený slovník s informacemi o zaměstnancích
zamestnanci = {
    "zamestnanec_1": {
        "jmeno": "Jan Novák",
        "povolání": "programátor"
    },
    "zamestnanec_2": {
        "jmeno": "Eva Svobodová",
        "povolání": "designér"
    },
    "zamestnanec_3": {
        "jmeno": "Petr Dvořák",
        "povolání": "programátor"
    }
}
print(f"Slovník se zaměstnanci: {zamestnanci}")

# získá vstup od uživatele, a to hledaný klíč
hledany_klic = input("Zadejte hledaný klíč (označení zaměstnance, kterého chcete vyhledat): ")

# zkontroluje zda se klíč nachází ve slovníku 
# a v případě že se nachází, vypíše jméno zaměstnance
if hledany_klic in zamestnanci:
    vnoreny_slovnik = zamestnanci.get(hledany_klic).get("jmeno")
    print(f"Jméno: {vnoreny_slovnik}")
else:
    print(f"Hledaný klíč {hledany_klic} není ve slovníku.")






