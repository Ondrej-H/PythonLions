
# definuje funkci
def pozdrav(jmeno):
    return f"Ahoj, {jmeno}"


# kontrola jestli byl program spuštěn napřímo
if __name__ == "__main__":      # pokud je ve speciální proměnné __name__ řetězec "__main__", tak byl program spuštěn napřímo; jinak by tam byl název importovaného modulu
    jmeno = input("Zadejte vaše jméno: ")
    print(pozdrav(jmeno))
