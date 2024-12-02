
import sys
sys.path.append(r"C:\Users\huber\AppData\Local\Programs\Python\Python312\Lib\site-packages")   # 'pip show prettytable' zapsat do konzole - vypíše nám cestu, kde se balíček nachází (a další info)
# sys.path... použijeme v případě, že nemáme nastavené prostředí (nemáme add to path)
               #r - raw řetězec
# importuje balíček prettytable
import prettytable as pt

# vytvoří tabulku a vypíše jí
tabulka = pt.PrettyTable()
tabulka.field_names = ["Jméno", "Věk"]      # vytvoří záhlaví tabulky
tabulka.add_rows(                           # vloží dva řádky do tabulky
    [
        ["Alice", 25],
        ["Bob", 30]
    ]
)
print(tabulka)
