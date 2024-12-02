
def pozdrav():
    print("Ahoj!")

nazev_modulu = __name__
print(f"Název modulu tisknutý v modulu samotném: {nazev_modulu}") # vypíše se vždy, když je modul volán, tedy i hned při importu

# při spuštění tohoto modulu s kód v podmínce vykoná, protože modul přímo spouštíme
if __name__ == "__main__":
    pozdrav()