
# vytvoří množinu největších měst ČR a vypíše ji
nejvetsi_mesta = set(["Praha", "Brno", "Ostrava"])
print(f"Největší města ČR jsou: {nejvetsi_mesta}")

# načte od uživatele město
nove_mesto = input("Zadejte město, které chcete přidat: ")

# přidá město do množiny a vypíše ji
nejvetsi_mesta.add(nove_mesto)
print(f"Aktualizovaná množina měst: {nejvetsi_mesta}")
