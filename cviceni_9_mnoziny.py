
# vytvoří dvě prázdné množiny a vypíše je
mnozina_1 = set()
mnozina_2 = set()
print(f"Prádná množina 1: {mnozina_1}")
print(f"Prádná množina 2: {mnozina_2}\n")

# přidá do každé možiny jiné město a vypíše je
mnozina_1.add("Praha")
mnozina_2.add("Brno")
print(f"Naplněná množina 1: {mnozina_1}")
print(f"Prádná množina 2: {mnozina_2}\n")

# sjednotí množiny
sjednocena_mnozina = mnozina_1 | mnozina_2
print(f"Sjednocená množina : {sjednocena_mnozina}")








