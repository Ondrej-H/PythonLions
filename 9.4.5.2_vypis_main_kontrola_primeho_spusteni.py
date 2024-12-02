
from modul_pozdrav import modul_pozdrav

print(__name__)

if __name__ == "__main__":      # pokud je ve speciální proměnné __name__ řetězec "__main__", tak byl program spuštěn napřímo; jinak by tam byl název importovaného modulu
    jmeno = input("Zadejte vaše jméno: ")
    print(modul_pozdrav.pozdrav(jmeno))
